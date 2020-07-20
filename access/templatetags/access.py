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
    return list_of_hints.get(value)


@register.filter
def find_common_hints(list_of_hints, checked):
    hints = []
    if list_of_hints:
        if len(checked) == 1 and list_of_hints.get('multiple'):
            hints.append(list_of_hints.get('multiple'))

        common_hints = list_of_hints.get('not')
        if common_hints:
            for hint_value in common_hints:
                if not hint_value in checked and common_hints.get(hint_value) not in hints:
                    hints.append(common_hints.get(hint_value))

    return hints