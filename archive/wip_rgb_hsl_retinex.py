"""Example script for doing color preserving retines on RGB-like MRI data."""

from __future__ import division
import os
import numpy as np
from nibabel import load, save, Nifti1Image
from retinex_for_mri.core import multi_scale_retinex_3d
from retinex_for_mri.conversions import rgb2hsl, hsl2rgb
from retinex_for_mri.utils import truncate_and_scale
np.seterr(divide='ignore', invalid='ignore')

"""Load Data"""
#
vol1 = load('/path/to/file_T1w.nii.gz')
vol2 = load('/path/to/file_PDw.nii.gz')
vol3 = load('/path/to/file_T2w.nii.gz')

basename_vol1 = vol1.get_filename().split(os.extsep, 1)[0]
basename_vol2 = vol2.get_filename().split(os.extsep, 1)[0]
basename_vol3 = vol3.get_filename().split(os.extsep, 1)[0]

dirname = os.path.dirname(vol1.get_filename())
niiHeader, niiAffine = vol1.header, vol1.affine
shape = vol1.shape + (3,)

# Parameters
data_range = 500
retinex_scales = [1, 3, 10]

# Preprocess
vol1 = truncate_and_scale(vol1.get_data(), percMin=0, percMax=100, zeroTo=1.0)
vol2 = truncate_and_scale(vol2.get_data(), percMin=0, percMax=100, zeroTo=1.0)
vol3 = truncate_and_scale(vol3.get_data(), percMin=0, percMax=100, zeroTo=1.0)

rgb = np.zeros(shape)
rgb[:, :, :, 0] = np.nan_to_num(vol1)
del vol1
rgb[:, :, :, 1] = np.nan_to_num(vol2)
del vol2
rgb[:, :, :, 2] = np.nan_to_num(vol3)
del vol3

# RGB to HSL conversion and exports
flat = rgb.reshape(shape[0]*shape[1]*shape[2], shape[3])
hsl = rgb2hsl(flat)
hsl = hsl.reshape(shape)

out = Nifti1Image(np.squeeze(hsl[:, :, :, 0]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol1 + '_hue.nii.gz')
out = Nifti1Image(np.squeeze(hsl[:, :, :, 1]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol1 + '_sat.nii.gz')
out = Nifti1Image(np.squeeze(hsl[:, :, :, 2]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol1 + '_lum.nii.gz')
print('RGB to HSL conversion is done.')

# MSRCP (multiscale retinex with colour preservation)
lum = hsl[:, :, :, 2]
lum = multi_scale_retinex_3d(lum, scales=retinex_scales)
lum = truncate_and_scale(lum, percMin=0, percMax=100)

out = Nifti1Image(np.squeeze(lum),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol1 + '_lum_msr.nii.gz')
print('MSR on luminance is done.')

hsl[:, :, :, 2] = lum
del lum

# HSL to RGB
flat = hsl.reshape(shape[0]*shape[1]*shape[2], shape[3])
rgb = hsl2rgb(flat)
rgb = rgb.reshape(shape)
print('HSL to RGB conversion is done.')
rgb = rgb * data_range
print('Data range (0-1) is scaled with 500.')

out = Nifti1Image(np.squeeze(rgb[:, :, :, 0]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol1 + '_MSRCP.nii.gz')
out = Nifti1Image(np.squeeze(rgb[:, :, :, 1]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol2 + '_MSRCP.nii.gz', )
out = Nifti1Image(np.squeeze(rgb[:, :, :, 2]),
                  header=niiHeader, affine=niiAffine)
save(out, basename_vol3 + '_MSRCP.nii.gz')

print("Done.")