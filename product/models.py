import uuid


from django.db import models


# 属性
class AttrKey(models.Model):
    """
    属性key表
    """
    attr_key_id = models.AutoField(primary_key=True)
    attr_name = models.CharField(max_length=20)
    # cat_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attr_name


# 属性选项
class AttrValue(models.Model):
    """
    属性value表
    """
    attr_val_id = models.AutoField(primary_key=True)
    attr_value = models.CharField(max_length=20)
    attr_key_id = models.ForeignKey(AttrKey, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_attr_key(self):
        return str(self.attr_key_id)

    def __str__(self):
        return self.get_attr_key() + '-' + self.attr_value


# 分类
class ProductCategory(models.Model):
    """
    商品分类表
    """
    cat_id = models.AutoField(primary_key=True)
    # parent_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    # 设置parent_id可以为None
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    cat_name = models.CharField(max_length=20)
    cat_code = models.UUIDField(default=uuid.uuid4, editable=False)
    attr_list = models.ManyToManyField(AttrKey)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name


class Brand(models.Model):
    """
    品牌
    """
    bnd_id = models.AutoField(primary_key=True)
    bnd_name = models.CharField(max_length=20)
    bnd_code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.bnd_name


# SPU
class Product(models.Model):
    """
    商品表
    """
    pdt_id = models.AutoField(primary_key=True)
    pdt_name = models.CharField(max_length=20)
    pdt_code = models.UUIDField(default=uuid.uuid4, editable=False)
    pdt_desc = models.TextField(max_length=100, null=True, blank=True)
    cat_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdt_name


# SKU
class ProductSpecs(models.Model):
    """
    商品规格表
    """
    pdt_spec_id = models.AutoField(primary_key=True)
    pdt_spec_name = models.CharField(max_length=20)
    pdt_spec_code = models.UUIDField(default=uuid.uuid4, editable=False)
    pdt = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_product_name(self):
        name = self.pdt.pdt_name
        return name

    def __str__(self):
        return self.pdt_spec_name


class ProductSpecsToAttrVal(models.Model):
    """
    商品规格-属性选项关联
    """
    pdt_specs_attr_val_id = models.AutoField(primary_key=True)
    pdt_spec_id = models.ForeignKey(ProductSpecs, on_delete=models.CASCADE)
    attr_val_id = models.ForeignKey(AttrValue, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pdt_spec_id) + '-' + str(self.attr_val_id)
