# Generated by Django 3.0.6 on 2020-05-04 11:52

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_no', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('order_status', models.TextField(max_length=10)),
                ('product_count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('product_amount_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
