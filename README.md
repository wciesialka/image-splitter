![](https://img.shields.io/badge/dynamic/json?color=informational&label=Python&prefix=v&query=python&url=https%3A%2F%2Fgithub.com%2Fwciesialka%2Fimage-splitter%2Fblob%2Fmaster%2Finfo.json) ![](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Version&prefix=v&query=version&url=https%3A%2F%2Fgithub.com%2Fwciesialka%2Fimage-splitter%2Fblob%2Fmaster%2Finfo.json)

# image-splitter
Split an image into multiple columns or rows and serve as a printable PDF.

## Getting Started

### Prerequisites

This project was made using **Python 3.8.5**. Also required is **pip**.

The following Python packages are required:

`Pillow`

These can be found in [requirements.txt] and can be installed using `pip install -r requirements.txt`.

## Usage

This project has a command line interface (CLI). To use it, please use

```
python main.py [options] image
options:
    -h                  Help
    -n, --columns       Number of columns to create (defaults to 3).
    -k, --rows          Number of rows to create (defaults to 3).
    -d, --dpi           DPI of printer (defaults to 300).
    -w, --paperwidth    Width of paper in inches (defaults to 8.5).
    -y, --paperheight   Height of paper in inches (defaults to 11).
    -o, --output        File to output to (defaults to out.pdf).
```

## Examples

Examples can be found in the [examples] directory.

## License

This project is licensed under the MIT License. See [LICENSE] for details.

## Authors

* William Ciesialka