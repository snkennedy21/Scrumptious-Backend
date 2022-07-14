# Generated by Django 4.0.6 on 2022-07-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_fooditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=9, max_digits=10)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.fooditem')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.measure')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
        ),
    ]