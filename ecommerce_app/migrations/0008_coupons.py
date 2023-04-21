# Generated by Django 4.2 on 2023-04-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0007_wishlists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('discount_type', models.CharField(max_length=255)),
                ('discount_amount', models.IntegerField(default=0)),
                ('minimum_purchase', models.IntegerField(default=1)),
                ('expiration_date', models.DateTimeField()),
                ('usage_limit', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'coupons',
                'managed': True,
            },
        ),
    ]
