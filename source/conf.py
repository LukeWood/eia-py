import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "eia-py-api"
copyright = "2022, Luke Wood, & {add yourself}"
author = "2022, Luke Wood, & {add yourself}"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "/eia-py/"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
extensions = [
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    "sphinx_automodapi.automodapi",
]
