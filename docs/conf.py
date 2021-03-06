import sys, os

extensions = []
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = u'anafero'
copyright = u'2011, Eldarion'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = []
htmlhelp_basename = 'anaferodoc'
latex_documents = [
  ('index', 'anafero.tex', u'anafero Documentation',
   u'Eldarion', 'manual'),
]
man_pages = [
    ('index', 'anafero', u'anafero Documentation',
     [u'Eldarion'], 1)
]
