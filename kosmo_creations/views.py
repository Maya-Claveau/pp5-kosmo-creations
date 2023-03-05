from django.shortcuts import render


def handler400(request, exception):
    """ Error 400 - Bad Request """
    return render(request, "errors/400.html", status=400)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request, *args, **argva):
    """ Error handler 500 - internal server error """
    return render(request, "errors/500.html", status=500)
