#!/usr/bin/python

import sys ,os

from mako.template import Template
from mako.lookup import TemplateLookup

template_dir = 'templates/'
public_dir = 'public/'

rst2html="""
def rst2html(rst):
    return "<rst>" + rst + "</rst>"
"""

lookup = TemplateLookup(directories=[template_dir], default_filters=['rst2html'], imports=[rst2html])

def main(argv):
    for arg in argv:
        print lookup.get_template(arg).render()

print os.getcwd()
if __name__ == "__main__":
    main(sys.argv[1:])
