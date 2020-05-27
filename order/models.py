import uuid

from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.UUIDField(default=uuid.uuid4, editable=False)  # 提供给客户看的订单号
    order_status = models.TextField(max_length=10)  # 订单状态
    product_count = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
    ])  # 商品数量，最小值和默认值为1
    product_amount_total = models.DecimalField(max_digits=8, decimal_places=2)  # 商品总价
    order_date = models.DateField(auto_now_add=True)  # 下单时间
