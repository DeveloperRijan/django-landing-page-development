from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteInfo, MenuItem, HeroSection, Service, Package, PackageFeature, CTA

# Create your views here.
def index(request):
    site_info = SiteInfo.objects.filter(active=True).first()
    menus = MenuItem.objects.all()
    hero_section = HeroSection.objects.filter(active=True).first()
    services_special = Service.objects.filter(active=True).filter(is_special=True).all()
    services = Service.objects.filter(active=True).filter(is_special=False).all()
    packages = Package.objects.filter(active=True).all()
    cta = CTA.objects.first()

    return render(request, "index.html", {
        "site_info":site_info,
        "menus":menus,
        "hero_section" : hero_section,
        "services_special" : services_special,
        "services" : services,
        'packages':packages,
        'cta':cta
    })
