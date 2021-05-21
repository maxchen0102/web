from django.http import HttpResponse



# Create your views here.
def hello1(request):
    return HttpResponse("Hello Django")

