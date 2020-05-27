from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import *


class AttrKeyViewSet(viewsets.ModelViewSet):
    queryset = AttrKey.objects.all()
    serializer_class = AttrKeySerializer


class AttrValueViewSet(viewsets.ModelViewSet):
    queryset = AttrValue.objects.all()
    serializer_class = AttrValueSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    # def get_primary_categories(self):
    #     """
    #     获取一级产品分类
    #     :return:
    #     """
    #     return ProductCategory.objects.filter(parent_id=None)

    # def get_category_menu(self, cat_id=None):
    #     """
    #     获取满足antd要求的产品分类菜单
    #     :return:
    #     """
    #     cats = ProductCategory.objects.filter(parent_id=cat_id)
    #     if len(cats) == 0:
    #         return None
    #     menu = []
    #     for cat in cats:
    #         temp = {}
    #         temp["path"] = "/prodcut/category/" + str(cat.cat_id)
    #         temp["name"] = str(cat.cat_name)
    #         temp["icon"] = "cat"
    #         sub_cats = self.get_category_menu(cat_id=cat.cat_id)
    #         if sub_cats is not None:
    #             temp["routes"] = sub_cats
    #         else:
    #             temp["component"] = "./product/" + str(cat.cat_id)  # 路由到该类别下所有产品的页面
    #         menu.append(temp)
    #     return menu

    # @action(detail=False)
    # def menu(self, request, *args, **kwargs):
    #     rsp = {}
    #     rsp["result"] = self.get_category_menu()
    #     return Response(rsp)
    #
    # @action(detail=False)
    # def general(self, request, *args, **kwargs):
    #     """
    #     获取一级产品分类并回复
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     primary_categories = ProductCategory.objects.filter(parent_id=None)
    #     serializer = self.get_serializer(primary_categories, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False)
    # def category_menu(self, request, *args, **kwargs):
    #     """
    #     返回满足antd要求的菜单数据格式
    #     {
    #         result: [
    #             {
    #                 "path": "product/category/:id",
    #                 "name": ":cat_name"
    #                 "icon": "cat",
    #                 "routes": [
    #
    #                 ]
    #             },
    #         ],
    #     }
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     menu_categories = ProductCategory.objects.filter(parent_id=None)



class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSpecsViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecs.objects.all()
    serializer_class = ProductSpecsSerializer


class ProductSpecsToAttrValViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecsToAttrVal
    serializer_class = ProductSpecsToAttrValSerializer
