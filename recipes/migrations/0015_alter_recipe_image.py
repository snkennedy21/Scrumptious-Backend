# Generated by Django 4.0.3 on 2022-07-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='post_image'),
        ),
    ]
