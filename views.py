from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a super-minimal Django project.")
