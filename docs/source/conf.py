# -*- coding: utf-8 -*-
#
# Python cfunits muodule documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 3 16:28:25 2011.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented
# out serve to show the default.

import re
import sys
import os
import datetime
import cfunits

def _read(fname):
    """Returns content of a file.

    """
    fpath = os.path.dirname(__file__)
    fpath = os.path.join(fpath, fname)
    with open(fpath, 'r') as file_:
        return file_.read()

def _get_version():
    """Returns library version by inspecting __init__.py file.

    """
    return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                     _read("../../cfunits/__init__.py"),
                     re.MULTILINE).group(1)

def _get_year():
    '''
    '''
    return str(datetime.datetime.now().year)

def _get_date():
    '''Get the current calendar year.

    '''
    return str(datetime.date.today())

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory
# is relative to the documentation root, use os.path.abspath to make
# it absolute, like shown here.  sys.path.insert(0,os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '2.3.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
#              'sphinx.ext.viewcode',
              'sphinx.ext.linkcode',
#              'sphinx.ext.pngmath',
#              'sphinx.ext.mathjax',
              'sphinx.ext.graphviz',
#              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.intersphinx',
              'sphinx.ext.doctest',
              'sphinx.ext.githubpages',
              'sphinx_copybutton',
              'sphinx_toggleprompt',
              ]

# Boolean indicating whether to scan all found documents for
# autosummary directives, and to generate stub pages for each
# (http://sphinx-doc.org/latest/ext/autosummary.html)
autosummary_generate = True

# Both the class’ and the __init__ method’s docstring are concatenated
# and inserted.
autoclass_content = 'both'

#inheritance_graph_attrs = {'rankdir': "TB",
#                           'clusterrank': 'local'}
#inheritance_node_attrs  = {'style': 'filled'}

# This value selects how automatically documented members are sorted
# (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_member_order = 'groupwise'

# This value is a list of autodoc directive flags that should be
# automatically applied to all autodoc
# directives. (http://sphinx-doc.org/latest/ext/autodoc.html)
autodoc_default_options = {'members': True,
                           'inherited-members': True,
                           'show-inheritance': True,
}

intersphinx_cache_limit = 5     # days to keep the cached inventories
intersphinx_mapping = {
    'sphinx':     ('http://sphinx.pocoo.org',  None),
    'python':     ('http://docs.python.org/3', None),
    'numpy':      ('http://docs.scipy.org/doc/numpy', None),
    'cftime':     ('http://unidata.github.io/cftime', None),
    }

# The name of the default domain. Can also be None to disable a
# default domain. The default is 'py'.
#primary_domain = 'cfunits'

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates', '../_templates', '../../_templates']
templates_path = ['../_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Python cfunits package'
copyright = _get_year()+', NCAS | Page built on '+_get_date()
author = 'David Hassell'

# The version info for the project you're documenting, acts as
# replacement for |version| and |release|, also used in various other
# places throughout the built documents.
#
# The short X.Y version.
version = _get_version()
# The full version, including alpha/beta/rc tags.
release = _get_version()

# The language for content autogenerated by Sphinx. Refer to
# documentation for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today
# to some non-false value, then it is used:
#today = ''
#Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
#documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all
# description unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in
# the output. They are ignored by default.
show_authors = True # False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# The default language to highlight source code
highlight_language = 'python'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the
# documentation for a list of builtin themes.
#html_theme = 'default'
html_theme = 'alabaster' #'default' #'haiku' #'default'

# Theme options are theme-specific and customize the look and feel of
# a theme further.  For a list of options available for each theme,
# see the documentation.
html_theme_options = {
    "show_related"    : 'true',
    "sidebar_collapse": 'true',
    'fixed_sidebar'   : 'true',
    'page_width'      : '85%',
    'seealso_bg'      : 'transparent',
    'seealso_border'  : 'transparent',
    'shadow'          : 'false',
     'show_powered_by': 'true',
    'font_size'       : '13pt',
    'code_font_size'  : '10pt',
    'font_family'     : 'Arial',
    'head_font_family': 'Arial',
    'link_hover'      : '#6b0000',
    'github_button'   : 'true',
    'github_type'     : 'star',
    'github_repo'     : 'cfunits',
    'github_user'     : 'NCAS-CMS',
    'pre_bg'          : '#ecf2f9',
    'code_bg'         : '#ecf2f9',
    'description'     : 'A Python interface to the UDUNITS-2 library with CF extensions',
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Documentation"

# A shorter title for the navigation bar.  Default is the same as
# html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at
# the top of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style
# sheets) here, relative to this directory. They are copied after the
# builtin static files, so a file named "default.css" will overwrite
# the builtin "default.css".
html_static_path = ['_static']

# Paths (filenames) here must be relative to (under) html_static_path as above:
html_css_files = [
    'customise-alabaster.css',
]

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {'**': ['my_con.html', 'globaltoc.html', 'sourcelink.html']}
html_sidebars = { '**': ['about.html',
                         'searchbox.html',
                         'globaltoc.html',
                         'relations.html',
#                         'sourcelink.html',
                         ]
}

# Additional templates that should be rendered to pages, maps page
# names to template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default
# is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is
# True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all
# pages will contain a <link> tag referring to it.  The value of this
# option must be the base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'cfunitsdoc'


# -- Options for LaTeX output -------------------------------------------------

## The paper size ('letter' or 'a4').
#latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples (source
# start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index', 'cfunits.tex', 'cfunits Documentation',
     'NCAS', 'manual'),
    ]

# The name of an image file (relative to this directory) to place at
# the top of the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are
# parts, not chapters.
latex_use_parts = True

# If true, show page references after internal links.
latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

# A dictionary that contains LaTeX snippets that override those Sphinx
# usually puts into the generated .tex files.
latex_elements = {'papersize': 'a4paper'}

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples (source start file, name,
# description, authors, manual section).
man_pages = [
    ('index', 'cfunits', 'cfunits Documentation',
     'NCAS', 1)
    ]

# Configure copybutton
# Note the below, skipping of text via copybutton, is no longer required for
# Python prompts as those can be included or excluded in copied code via the
# toggle button (sphinx-toggleprompt). So we skip console prompts which we
# also have in the docs as the second most-common case.
copybutton_prompt_text = "$ "   # prompt to skip automatically on copying

# Configure toggleprompt
toggleprompt_offset_right = 25  # stops toggle and copy buttons overlapping

# This is a function which should return the URL to source code
# corresponding to the object in given domain with given information.

import inspect
from os.path import relpath, dirname

link_release = re.search('(\d+\.\d+\.\d+)', release).groups()[0]

def linkcode_resolve(domain, info):
    
    #=================================================================
    # Must delete all .doctrees directories in build for changes to be
    # picked up. E.g.:
    #
    # >> rm -fr build/.doctrees build/*/.doctrees build/*/*/.doctrees
    #=================================================================

    online_source_code = True

    if domain != 'py':
        return None
    if not info['module']:
        return None
    
    modname = info['module']
    fullname = info['fullname']
    
    submod = sys.modules.get(modname, None)
    if submod is None:
        return None
    
    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None
    
    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        return None
    
    try:
        source, lineno = inspect.findsource(obj)
        nlines = len(inspect.getsourcelines(obj)[0])
    except:
        lineno = None
    
    fn = relpath(fn, start=dirname(cfunits.__file__))
    
    if lineno:
        linespec = "#L{0}".format(lineno+1)
        # Can add range when jump-to feature is enable in bitbucket
    else:
        linespec = ""
    
    # ----------------------------------------------------------------
    # NOTE: You need to touch the .rst files to get the change in
    # ----------------------------------------------------------------
    if online_source_code:
         url = "https://github.com/NCAS-CMS/cfunits/blob/v{0}/cfunits/{1}{2}".format(
             link_release, fn, linespec)
         print(url)
         return url
    else:
        # Point to local source code relative to this directory
        return "../../../cfunits/%s%s" % (fn, linespec)
