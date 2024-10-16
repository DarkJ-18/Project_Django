# Generated by Django 5.1.1 on 2024-10-16 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_product_categoria_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(help_text='Fecha de Factura YYYY-MM-DD')),
                ('cliente', models.CharField(max_length=100)),
                ('num_factura', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.product')),
            ],
        ),
    ]