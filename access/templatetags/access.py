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
def find_hints(list_of_hints, value):
    hints = []
    if list_of_hints:
        for hint in list_of_hints:
            if hint.get("option_value", "") == value:
                hints.append(hint.get("text", ""))
            
    return hints
