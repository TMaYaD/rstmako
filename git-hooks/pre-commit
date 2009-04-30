#!/usr/bin/python

from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['../templates'], module_directory='/tmp/mako_modules')

def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    print mytemplate.render(**kwargs)

#here we read all the makos and render them

