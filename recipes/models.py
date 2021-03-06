from enum import unique
from tkinter import TRUE
from django.db import models
from django.forms import CharField



class Recipe(models.Model):
  name = models.CharField(max_length=125)
  author = models.CharField(max_length=100)
  description = models.TextField()
  image = models.URLField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
class Ingredient(models.Model):
  amount = models.DecimalField(decimal_places=1, max_digits=2)
  recipe = models.ForeignKey("Recipe", related_name="ingredients", on_delete=models.CASCADE)
  measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
  food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

  def __str__(self):
    return f'{self.amount} {self.measure} {self.food}'


class Measure(models.Model):
  name = models.CharField(max_length=30, unique=True)
  abbreviation = models.CharField(max_length=10, unique=True)

  def __str__(self):
    return self.name

class FoodItem(models.Model):
  name = models.CharField(max_length=100, unique=TRUE)

  def __str__(self):
    return self.name

class Step(models.Model):
  recipe = models.ForeignKey("Recipe", related_name="steps", on_delete=models.CASCADE)
  order = models.PositiveSmallIntegerField()
  directions = models.CharField(max_length=300)
  food_items = models.ManyToManyField("FoodItem", null=True, blank=True)

  def __str__(self):
    return f"step {self.order}"
