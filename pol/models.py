from django.db import models


class Category(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_uz

class Brand(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    p1_uz = models.CharField(max_length=200, null=True, blank=True)
    p1_ru = models.CharField(max_length=200, null=True, blank=True)
    p1_en = models.CharField(max_length=200, null=True, blank=True)
    p2_uz = models.CharField(max_length=200, null=True, blank=True)
    p2_ru = models.CharField(max_length=200, null=True, blank=True)
    p2_en = models.CharField(max_length=200, null=True, blank=True)
    p3_uz = models.CharField(max_length=200, null=True, blank=True)
    p3_ru = models.CharField(max_length=200, null=True, blank=True)
    p3_en = models.CharField(max_length=200, null=True, blank=True)
    p4_uz = models.CharField(max_length=200, null=True, blank=True)
    p4_ru = models.CharField(max_length=200, null=True, blank=True)
    p4_en = models.CharField(max_length=200, null=True, blank=True)
    p5_uz = models.CharField(max_length=200, null=True, blank=True)
    p5_ru = models.CharField(max_length=200, null=True, blank=True)
    p5_en = models.CharField(max_length=200, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    price = models.IntegerField(default=0)
    file = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name_uz


class About(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
