# Generated by Django 4.2 on 2023-04-19 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0011_productvariants_productoptions_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('processing', 'PROCESSING'), ('shipped', 'SHIPPED'), ('delivered', 'DELIVERED'), ('canceled', 'CANCELED'), ('unknown', 'UNKNOWN')], default=('unknown', 'UNKNOWN'))),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.billingaddresses')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.coupons')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.shippingaddresses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Optionvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.productoptions')),
            ],
            options={
                'db_table': 'option_values',
                'managed': True,
            },
        ),
    ]