#!/usr/bin/python

import sys ,os

from mako.template import Template
from mako.lookup import TemplateLookup

lookup = TemplateLookup(directories=['templates'], module_directory='/tmp/mako_modules')

def main(argv):
    for arg in argv:
        print lookup.get_template(arg).render()

print os.getcwd()
if __name__ == "__main__":
    main(sys.argv[1:])
