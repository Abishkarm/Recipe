# Generated by Django 5.0.6 on 2024-05-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_ingrdients_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
