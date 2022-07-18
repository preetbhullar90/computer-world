from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def error_404(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)
