[![DOI](https://zenodo.org/badge/76043117.svg)](https://zenodo.org/badge/latestdoi/76043117)
[![PyPI version](https://badge.fury.io/py/retinex_for_mri.svg)](https://badge.fury.io/py/retinex_for_mri)


# Iphigen

Provides a simple commandline interface for multi-scale retinex image enhancement and color balancing. It supports 3D images too, such as magnetic resonance (MR) images.

<img src="visuals/visual_01.png">

# Getting started

## Dependencies

**[Python 3.6](https://www.python.org/downloads/release/python-363/)** or **[Python 2.7](https://www.python.org/download/releases/2.7/)** (compatible with both) and the following packages:

| Package                              | Tested version |
|--------------------------------------|----------------|
| [NumPy](http://www.numpy.org/)       | 1.14.2         |
| [SciPy](https://www.scipy.org/)      | 1.0.0          |
| [NiBabel](http://nipy.org/nibabel/)  | 2.2.0          |

## Installation

Clone this repository or download the latest release. In your commandline, change directory to folder of this package and run the following on your command line:
```
python setup.py install
```

## Usage
Apply retinex to an image with:
```
iphigen /path/to/image.png --retinex
```
<img src="visuals/visual_01.png">

Intensity balance:
```
iphigen_nifti /path/to/data.nii.gz --intensity_balance
```
<img src="visuals/visual_01.png">

Color balance:
```
iphigen_nifti /path/to/data.nii.gz --simplest_color_balance
```
<img src="visuals/visual_01.png">

Mix and match:
```
iphigen /path/to/image.png --retinex --intensity_balance --simplex_color_balance
```

For other options, see the help:
```
iphigen -h
```

# Support

Please use [github issues](https://github.com/ofgulban/iphigen/issues) to report bugs or make suggestions.

# License

The project is licensed under [GNU General Public License Version 3](http://www.gnu.org/licenses/gpl.html).

# References

This application is based on the following work:

* Jobson, D. J., Rahman, Z. U., & Woodell, G. A. (1997). A multiscale retinex for bridging the gap between color images and the human observation of scenes. IEEE Transactions on Image Processing, 6(7), 965–976. <http://doi.org/10.1109/83.597272>

* Petro, A. B., Sbert, C., & Morel, J. (2014). Multiscale Retinex. Image Processing On Line, 4, 71–88. <http://doi.org/10.5201/ipol.2014.107>

* Limare, N., Lisani, J., Morel, J., Petro, A. B., & Sbert, C. (2011). Simplest Color Balance. Image Processing On Line, 1(1), 125–133. <http://doi.org/10.5201/ipol.2011.llmps-scb>
