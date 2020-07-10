from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def ajax_url(context):
    request = context["request"]
    context["submission_url"] = request.GET.get('submission_url')
    context["submit_url"] = request.build_absolute_uri(reverse(
        'access.views.exercise_ajax',
        args=[context['course']['key'], context['exercise']['key']]
    ))
    return ""

@register.filter
def find_checkbox_hints(list_of_hints, value):
    hints = []
    if list_of_hints:
        for hint in list_of_hints:
            if hint.get('value') == value:
                hints.append(hint.get('label'))

    return hints

@register.filter
def find_common_hints(list_of_hints, checked):
    hints = []
    if list_of_hints:
        for hint in list_of_hints:
            if hint.get('not') and hint.get('value') not in checked and hint.get('label') not in hints:
                hints.append(hint.get('label'))

    return hints