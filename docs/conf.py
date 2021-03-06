#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# airr-standards documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 17 14:47:21 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Imports
import os
import sys
import yaml
import yamlordereddictloader
from unittest.mock import MagicMock
sys.path.append(os.path.abspath('.'))

# Mock modules for ReadTheDocs
if os.environ.get('READTHEDOCS', None) == 'True':
    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):  return MagicMock()

    mock_modules = ['numpy', 'pandas']
    sys.modules.update((mod_name, Mock()) for mod_name in mock_modules)


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinxcontrib.autoprogram',
              'rstjinjaext']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Enable Markdown content
from recommonmark.parser import CommonMarkParser
source_parsers = {'.md': CommonMarkParser}

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'airr-standards'
copyright = '2017-2018, AIRR Community'
author = 'AIRR Community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1.0'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML help
htmlhelp_basename = 'airr-standardsdoc'

# Alabaster options
html_theme = 'alabaster'
html_theme_options = {'github_user': 'airr-community',
                      'github_repo': 'airr-standards',
                      'github_button': True,
                      'sidebar_includehidden': True,
                      'extra_nav_links': {'AIRR Community': 'http://airr-community.org'}}
html_sidebars = {'**': ['about.html',
                        'navigation.html',
                        'searchbox.html']}

# Bootstrap options
# import sphinx_bootstrap_theme
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# html_sidebars = {'**': ['localtoc.html']}

# Theme options are theme-specific and customize the look and feel of a
# theme further.
# html_theme_options = {
#     # Navigation bar title. (Default: ``project`` value)
#     'navbar_title': 'AIRR Standards',
#
#     # Tab name for entire site. (Default: "Site")
#     'navbar_site_name': 'Contents',
#
#     # A list of tuples containing pages or urls to link to.
#     # Valid tuples should be in the following forms:
#     #    (name, page)                 # a link to a page
#     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
#     #    (name, "http://example.com", True) # arbitrary absolute url
#     # Note the "1" or "True" value above as the third argument to indicate
#     # an arbitrary url.
#     'navbar_links': [('AIRR Community', 'http://airr-community.org', True)],
#
#     # Render the next and previous page links in navbar. (Default: true)
#     'navbar_sidebarrel': True,
#
#     # Render the current pages TOC in the navbar. (Default: true)
#     'navbar_pagenav': True,
#
#     # Tab name for the current pages TOC. (Default: "Page")
#     'navbar_pagenav_name': 'Page',
#
#     # Global TOC depth for "site" navbar tab. (Default: 1)
#     # Switching to -1 shows all levels.
#     'globaltoc_depth': 3,
#
#     # Include hidden TOCs in Site navbar?
#     #
#     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
#     # non-hidden ``toctree`` directives in the same page, or else the build
#     # will break.
#     #
#     # Values: "true" (default) or "false"
#     'globaltoc_includehidden': 'true',
#
#     # HTML navbar class (Default: "navbar") to attach to <div> element.
#     # For black navbar, do "navbar navbar-inverse"
#     'navbar_class': 'navbar navbar-inverse',
#
#     # Fix navigation bar to top of page?
#     # Values: "true" (default) or "false"
#     'navbar_fixed_top': 'true',
#
#     # Location of link to source.
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     'source_link_position': 'None',
#
#     # Choose Bootstrap version.
#     # Values: "3" (default) or "2" (in quotes)
#     'bootstrap_version': '3',
# }

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'airr-standards.tex', 'airr-standards Documentation',
     'AIRR Community', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'airr-standards', 'airr-standards Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'airr-standards', 'airr-standards Documentation',
     author, 'airr-standards', 'One line description of project.',
     'Miscellaneous'),
]


# Load data for schemas
with open(os.path.abspath('../specs/airr-schema.yaml')) as ip:
    airr_schema = yaml.load(ip, Loader=yamlordereddictloader.Loader)
html_context = {'airr_schema': airr_schema}

# Write download spec files
import csv
dl_path = '_downloads'
if not os.path.exists(dl_path):  os.mkdir(dl_path)

# Build table for each spec
tables = ['Rearrangement', 'Alignment']
fields = ['Name', 'Type', 'Priority', 'Description']
for spec in tables:
    # Get specs
    required = airr_schema[spec]['required']
    properties = airr_schema[spec]['properties']
    # Write TSV
    with open(os.path.join(dl_path, '%s.tsv' % spec), 'w') as f:
        writer = csv.writer(f, dialect='excel-tab')
        rows = ([k, v['type'], 'required' if k in required else 'optional', v['description'].strip()] \
                for k, v in properties.items())
        writer.writerow(fields)
        writer.writerows(rows)
