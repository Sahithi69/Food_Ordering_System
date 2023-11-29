# Generated by Django 3.1.3 on 2021-05-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20210525_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_type',
            field=models.CharField(blank=True, choices=[('HOME DELIVERY', 'HOME DELIVERY'), ('DINE IN', 'DINE IN')], default='HOME DELIVERY', max_length=100, null=True),
        ),
    ]