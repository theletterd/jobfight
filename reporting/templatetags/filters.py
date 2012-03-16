from django.template.defaultfilters import register

@register.filter(name='lookup')
def lookup(dict, index):
    return dict[index]
