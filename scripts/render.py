#!/usr/bin/python

import sys
from glob import glob

from mako.template import Template
from mako.lookup import TemplateLookup
from mako.runtime import Context

template_dir = 'templates/'
public_dir = 'public/'

lookup = TemplateLookup(directories=[template_dir], module_directory='/tmp/mako_modules')

def main():
    templates = glob(template_dir + "*.mako")
    for template in templates:
    	ofile = template.replace(template_dir,public_dir,1).replace('mako','html')
	buf = open(ofile,"w")
	ctx = Context(buf)
        print Template(filename=template, lookup=lookup).render_context(ctx)

if __name__ == "__main__":
    main()
