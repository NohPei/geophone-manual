# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'GeoMCU'
copyright = '2024, Regents of the University of Michigan'
author = 'Jesse R Codling'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_dark_mode',
    'sphinx_toolbox.wikipedia',
    'sphinx_toolbox.github'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'pio': ('https://docs.platformio.org/en/latest/', None),
}
intersphinx_disabled_domains = ['std']

napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True

autodoc_default_options = {
    "members": True,
    "undoc-members": True
}

templates_path = ['_templates']

manpages_url = 'https://man.archlinux.org/man/{page}.{section}'

github_username = "NohPei"
github_repository = "NohPei/GeoMCU"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
