This directory contains the source code required to compile the Bokeh extension jsmol-to-bokeh and avoid the 
dependence on a local NodeJS installation.

The code of the extension has been adapted from the original jsmol-bokeh-extension code from L. Talirz (https://github.com/ltalirz/jsmol-bokeh-extension).

A pre-compiled `jsmol_to_bokeh.min.js` extension is provided in the parent folder: re-packaging is only necessary in case the user desires to modify the extension.

To build the extension, the user should call `bokeh build` command in the `to_package/jsmol_to_bokeh` directory. From the resulting files,
either the minified (`jsmol_to_bokeh.min.js`) or the non-minified (`jsmol_to_bokeh.js`) JavaScript files can be used. 

In order to *use* the recompiled files, the Bokeh application should be provided with the corresponding path -> for HTML embedding, a Jinja2 postamble template including the corresponding `<script>` statement should be passed to the `bokeh.plotting.save` command. 
