from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    app_title = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)


class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    item_link = models.CharField(max_length=250)


class HeroSection(models.Model):
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=150)
    active = models.BooleanField(default=False)


class Service(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=3000)
    is_special = models.BooleanField(default=False)
    active = models.BooleanField(default=False)


class Package(models.Model):
    package_name = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.package_name

class PackageFeature(models.Model):
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
    )
    feature = models.CharField(max_length=60)

    def __str__(self):
        return self.package.package_name


class CTA(models.Model):
    title = models.CharField(max_length=50)
