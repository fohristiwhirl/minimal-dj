from django.http import HttpResponse

hits = 0

def index(request):
    global hits; hits += 1
    return HttpResponse("This is a super-minimal Django project. Hits: {}".format(hits))
