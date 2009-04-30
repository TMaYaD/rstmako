<% testvar="somenting unique" %>

<%def name="callable()">
    I am the callable
</%def>

<%def name="embeddable()">
    This is embeddable begin
    ${caller.body()}
    embeddable end
</%def>

example mako template
I expect tags around this whole thing
and ${testvar} substitution

callable ${callable()} substitution

<%self:embeddable>
 embedded content
 </%self:embeddable>
