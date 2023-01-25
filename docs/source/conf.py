# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Peritia'
copyright = '2023, Scalabli'
author = 'Gerrishon Sirere'

release = '2023.x'
version = '2023.1-beta'
import os
# -- General configuration
os.system("pip install secretum_sphinx_theme")
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'secretum_sphinx_theme',
    'notfound.extension'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'collapse_navigation': False, 'logo_only': True}


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "images/peritia.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ['css/quo_theme.css']

html_show_sphinx = False
# -- Options for EPUB output
epub_show_urls = 'footnote'
