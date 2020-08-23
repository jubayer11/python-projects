from django.shortcuts import render


# Create your views here.
def index(request):
    content_text = {'name': 'hello world', 'number': 100}
    return render(request, 'index.html',content_text)


def other(request):
    return render(request, 'other.html')


def relative(request):
    return render(request, 'relatives_url_template.html')
