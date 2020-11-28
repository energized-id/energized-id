from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:itemadmin"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:itemadmin"}
]

@login_required
def applicationadmin(request):
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all, "AdminItems":AdminItems, })

@login_required
def itemadmin(request,slug):
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == slug:
            AdminItem = item
    fields = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
    fieldTypes = []
    values = []
    for i, value in enumerate(eval(AdminItem.get('model') + '.objects.values()'), start=0):
        fieldTypes.append([])
        for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
            fieldTypes[i].append(field.get_internal_type())
        fieldTypes[i] = tuple(fieldTypes[i])
        values.append([])
        for item in list(value.values()):
            values[i].append(item)
        values[i] = tuple(values[i])
        
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/itemadmin.html',
    context = {"fields":fields, "fieldTypes":fieldTypes, "results":dict(zip(values, fieldTypes)), "BadgeTemplate":BadgeTemplate.objects.all, "AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})