# Generated by Django 4.0.6 on 2022-07-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_step_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=100, unique=1),
        ),
    ]