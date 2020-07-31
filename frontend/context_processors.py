from django.conf import settings


def general(request):
    context = {"PROD": settings.PROD}
    return context
