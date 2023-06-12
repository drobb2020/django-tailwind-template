from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'core/index.html', context)


def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)


def pricing(request):
    context = {}
    return render(request, 'core/pricing.html', context)


def services(request):
    context = {}
    return render(request, 'core/services.html', context)


def about(request):
    context = {}
    return render(request, 'core/about.html', context)
