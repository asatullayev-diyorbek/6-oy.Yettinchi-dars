from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # User modeli bizda yo'qligi uchun djangoni user modeliga uladim
    # first_name = models.CharField(max_length=100) # User modelni ichida mavjud
    # last_name = models.CharField(max_length=100) # User modelni ichida mavjud
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "Xaridor"
        verbose_name_plural = "Xaridorlar"


class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    billing_address = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)

    def __str__(self):
        return self.customer.user.get_full_name()

    class Meta:
        verbose_name = "Xarid"
        verbose_name_plural = "Xaridlar"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = "Xarid elementi"
        verbose_name_plural = "Xarid elementlari"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


