# Generated by Django 4.0.6 on 2022-07-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='directions',
            field=models.CharField(max_length=300),
        ),
    ]
