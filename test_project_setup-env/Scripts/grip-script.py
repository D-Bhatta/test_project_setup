#!J:\Education\Code\Python\Project-Setup\playground\test_project_setup\test_project_setup-env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'grip==4.5.2','console_scripts','grip'
__requires__ = "grip==4.5.2"
import re
import sys

from pkg_resources import load_entry_point

if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(load_entry_point("grip==4.5.2", "console_scripts", "grip")())
