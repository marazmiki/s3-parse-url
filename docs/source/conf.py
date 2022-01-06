project = "s3-parse-url"
copyright = "2021, Mikhail Porokhovnichenko <marazmiki@gmail.com>"
author = 'Mikhail Porokhovnichenko <marazmiki@gmail.com>'

release = "0.2.0"
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
source_suffix = ".rst"

master_doc = "index"    # It's important for RTFD
exclude_patterns = []

# HTML
html_theme = "alabaster"    # sphinx
html_static_path = ["_static"]
html_split_index = True
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_search_language = "en"
htmlhelp_basename = project + "doc"

# MAN
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "s3-parse-url", "s3-parse-url Documentation", [author], 1)
]
