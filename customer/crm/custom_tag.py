from django import template

register = template.Library()

@register.simple_tag
def print_to_terminal(value):
    print("Debug:", value)  # This prints to the terminal
    return ""  # Returns an empty string to avoid breaking the template
