# -- Project information -----------------------------------------------------

project = 'Python'
copyright = '2018'
author = 'tt'
version = '0.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.inlinesyntaxhighlight'
]

source_suffix = '.rst'
master_doc = 'index'
language = 'de'
exclude_patterns = ['docs', 'Thumbs.db', '.DS_Store']
rst_prolog = """
.. |br| raw:: html

    <br>
"""


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'prev_next_buttons_location': 'none',
    'display_version': False,
    'collapse_navigation': False,
    'sticky_navigation': False
}
html_last_updated_fmt = ""
html_copy_source = False
html_show_sourcelink = False
html_show_copyright = False
html_show_sphinx = False
