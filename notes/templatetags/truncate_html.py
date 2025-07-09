from django import template
from django.utils.html import strip_tags
import re

register = template.Library()

@register.filter(name='truncate_words_html')
def truncate_words_html(value, arg):
    """
    Truncates HTML content to a certain number of words, preserving tags.
    """
    try:
        length = int(arg)
    except ValueError:
        return value  # Invalid argument

    text = strip_tags(value)
    words = re.findall(r'\\w+', text)
    if len(words) <= length:
        return value

    truncated_text = ' '.join(words[:length]) + '...'
    return truncated_text
