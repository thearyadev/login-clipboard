from distutils.core import setup

import py2exe, sys, os
sys.argv.append("py2exe")
setup(
    data_files=[("", ["icon.ico", "logins.json"])],
    windows=[{"script": "main.py", "icon_resources": [(1, "icon.ico")], "dest_base": "Battle.net Login Clipboard"}]
)
