# Generated by Django 5.1.2 on 2024-11-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0008_alter_material_markup_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='markup_percentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='price_per_qty',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='material',
            name='qty',
            field=models.FloatField(),
        ),
    ]
