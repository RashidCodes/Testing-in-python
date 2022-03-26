"""Importing * From a Package 

The author has to provide an explicit index of the package. The import staement uses the following convention:
    if a package's __init__.py code defines a list named __all__, it is taken to be the list of module names
    that should be imported when

    from package import * 

    is encountered. It is up to the package author to keep this list up-to-date when a new version of the package
    is released.
"""

# This is taken to be the list of module names that should be imported when 'from package import *' is encountered.
__all__ = ["my_code"]
