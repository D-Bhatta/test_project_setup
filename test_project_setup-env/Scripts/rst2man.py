#!J:\Education\Code\Python\Project-Setup\playground\test_project_setup\test_project_setup-env\Scripts\python.exe

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py
======

This module provides a simple command line interface that uses the
man page writer to output from ReStructuredText source.
"""

import locale

try:
    locale.setlocale(locale.LC_ALL, "")
except:
    pass

from docutils.core import default_description, publish_cmdline
from docutils.writers import manpage

description = "Generates plain unix manual documents.  " + default_description

publish_cmdline(writer=manpage.Writer(), description=description)
