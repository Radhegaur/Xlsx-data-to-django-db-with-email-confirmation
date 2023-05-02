# Generated by Django 4.2 on 2023-04-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_menu_calories_per_serving_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='calories_per_serving',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='serving_quantity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]