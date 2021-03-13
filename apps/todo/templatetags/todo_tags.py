from datetime import datetime

from django import template
from django.utils import timezone

register = template.Library()


# @register.filter(name='sencase')
# def sencase(arg):
#     return arg.title()
@register.filter(name='sencase')
def sencase(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)
    capitalized_sentence = " ".join(capitalized_words)
    return capitalized_sentence

@register.simple_tag(name='deltadate')
def deltadate(due):
    delta = due.date() - datetime.now().date()
    return delta.days
