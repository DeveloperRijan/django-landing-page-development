from django.contrib import admin
from django.db import models
from .models import SiteInfo, MenuItem, HeroSection, Service, Package, PackageFeature, CTA


#altered the view in admin section
class SiteInfoUI(admin.ModelAdmin):
    list_display = ('app_title', 'brand_name', 'active')

class MenuItemUI(admin.ModelAdmin):
    list_display = ('item_name', 'item_link')

class HeroSectionUI(admin.ModelAdmin):
    list_display = ('label', 'title', 'description', 'active')

class ServiceUI(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_special', 'active')

class PackageUI(admin.ModelAdmin):
    list_display = ('package_name', 'price', 'active')

class PackageFeatureUI(admin.ModelAdmin):
    list_display = ('get_package', 'feature')
    
    def get_package(self, request):
        packageName = Package.objects.get(id=request.package.id)
        return packageName

class CTAUI(admin.ModelAdmin):
    list_display = ('title',)

# Register your models here.
admin.site.register(SiteInfo, SiteInfoUI)
admin.site.register(MenuItem, MenuItemUI)
admin.site.register(HeroSection, HeroSectionUI)
admin.site.register(Service, ServiceUI)
admin.site.register(Package, PackageUI)
admin.site.register(PackageFeature, PackageFeatureUI)
admin.site.register(CTA, CTAUI)



