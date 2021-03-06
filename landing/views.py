from django.shortcuts import render
from .forms import *
from products.models import *


def home(request):
    # products_images = ProductImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
    # products_images_mot_masla = products_images.filter(Product__category_id=1)
    # products_images_indust_masla = products_images.filter(Product__category_id=3)
    # products_images_indust_transmis_masla = products_images.filter(Product__category_id=4)
    # products_images_gydra_masla = products_images.filter(Product__category_id=5)
    # products_images_prom_masla = products_images.filter(Product__category_id=6)
    # products_images_smazki = products_images.filter(Product__category_id=7)
    # products_images_tormoz_masla = products_images.filter(Product__category_id=8)
    # products_images_mot_mobil_masla = products_images.filter(Product__category_id=9)
    # products_images_prochee = products_images.filter(Product__category_id=10)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    return render(request, 'landing/home.html', locals())


def news(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'news/news.html', locals())


def asu(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'asu/asu.html', locals())


def epb(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'epb/epb.html', locals())


def pis(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'pis/pis.html', locals())


def kotli(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'kotli/kotli.html', locals())


def bmk(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'bmk/bmk.html', locals())


def about_us(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'about_us/about_us.html', locals())


def kvartiri(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
    products_images_1 = products_images.filter(Product__category__id=1)
    products_images_2 = products_images.filter(Product__category__id=2)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    return render(request, 'products/kvartiri.html', locals())
