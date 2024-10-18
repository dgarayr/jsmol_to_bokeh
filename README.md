*jsmol_to_bokeh*
Diego Garay-Ruiz, 2024

The main code of the extension has been adapted from the original jsmol-bokeh-extension code from Leopold Talirz (https://github.com/ltalirz/jsmol-bokeh-extension), and has been tested with Bokeh 2.4.0.

The repository contains three main elements:
- Minified pre-compiled JavaScript extension for connecting JSMol and Bokeh (`jsmol_to_bokeh.min.js`)
- Python-side extension defining typings for Bokeh. Installation files are included.
- Recipe and files for extension packaging/precompilation, to enable further extensions (`to_package/`).

