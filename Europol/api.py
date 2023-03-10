from pol.views import *
from rest_framework import routers

router = routers.DefaultRouter()


router.register('categories', CategoryView, basename='categories')
router.register('sub_categories', SubCategoryView, basename='sub_categories')
router.register('products', ProductView, basename='products')
router.register('about', AboutView, basename='about')
router.register('brands', BrandView, basename='brands')