# Generated by Django 4.0.6 on 2022-07-14 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('directions', models.CharField(max_length=2000)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.recipe')),
            ],
        ),
    ]