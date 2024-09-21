from django.http import HttpResponse # for simple data whitout templates
from django.template import loader # to load templates

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

