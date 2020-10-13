from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


from . import views


# attr_key_list = views.AttrKeyViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# attr_key_detail = views.AttrKeyViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# attr_val_list = views.AttrValueViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# attr_val_detail = views.AttrValueViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# product_category_list = views.ProductCategoryViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_category_detail = views.ProductCategoryViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# brand_list = views.BrandViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# brand_detail = views.BrandViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# product_list = views.ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_detail = views.ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# product_specs_list = views.ProductSpecsViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_specs_detail = views.ProductSpecsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# product_specs_to_attr_val_list = views.ProductSpecsToAttrValViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# product_specs_to_attr_val_detail = views.ProductSpecsToAttrValViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = [
#     path('attr/key/', attr_key_list, name='product-attr-key-list'),
#     path('attr/key/<int:pk>/', attr_key_detail, name='product-attr-key-detail'),
#     path('attr/val/', attr_val_list, name='product-attr-val-list'),
#     path('attr/val/<int:pk>/', attr_val_detail, name='product-attr-val-detail'),
#     path('category/', product_category_list, name='product-category-list'),
#     path('category/<int:pk>/', product_category_detail, name='product-category-detail'),
#     path('brand/', brand_list, name='brand-list'),
#     path('brand/<int:pk>/', brand_detail, name='brand-detail'),
#     path('', product_list, name='product-list'),
#     path('<int:pk>/', product_detail, name='product-detail'),
#     path('specs/', product_specs_list, name='product-specs-list'),
#     path('specs/<int:pk>/', product_specs_detail, name='product-specs-detail'),
# ]

router = DefaultRouter()
router.register(r'category', views.ProductCategoryViewSet)
router.register(r'spu', views.ProductViewSet)
urlpatterns = router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)

