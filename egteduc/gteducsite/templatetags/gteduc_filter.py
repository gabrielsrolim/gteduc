from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = Library()

@register.filter("gteducfixedwidth")
def gteducfixedwidth(value, arg):
	"""
	Truncates or pads a string to be a certain length

	Argument: Desired length of string
	"""

	try:
		length = int(arg)
		print 'length %s' % length
	except ValueError: # invalid literal for int()
		return value # Fail silently
	if not isinstance(value, basestring):
		value = str(value)

	if len(value) > (length):
		truncated = value[:length - 3]
		if not truncated.endswith('...'):
			truncated += '...'
		return truncated
	if len(value) <= length:
		padded = value
		spaces_needed = (length - len(value)) + 1
		for space_needed in range(1, spaces_needed):
			padded = "%s " % padded
		print 'padded: %s--' % padded	
		return padded

	return value

@stringfilter
def spacify(value, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(re.sub('\s', '&'+'nbsp;', esc(value)))
spacify.needs_autoescape = True
register.filter(spacify)

register.filter('gteducfixedwidth', gteducfixedwidth)