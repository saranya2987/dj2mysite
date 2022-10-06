from django.http import HttpResponse

# Create your views here.

def index(request):
    d={
        "name": "Arun",
        "age": 20,

    }
    return HttpResponse("<b>Hello Worlds</b>")