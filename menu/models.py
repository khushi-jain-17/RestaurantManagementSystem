from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey('Category',models.SET_NULL,null=True)
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self) -> str:
        return self.name    



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name       


