import uuid
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from apps.supplier.models import Supplier
from cloudinary.models import CloudinaryField
import cloudinary.uploader


def validate_image_size(value):
    limit = 1500 * 1024  # 1,500 KB (1.5 MB)
    if value.size > limit:
        raise ValidationError("Image size should not exceed 1.5 MB.")


# Define choices for product status
STATUS_CHOICES = [
    ("", "-- Choose status --"),
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
]


# Define choices for product type
PRODUCT_TYPE_CHOICES = [
    ("", "-- Choose product type --"),
    ("Roll-On", "Roll-On"),
    ("Spray", "Spray"),
    ("Diffuser", "Diffuser"),
]


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Name",
    )
    description = models.CharField(
        max_length=100, blank=True, verbose_name="Description"
    )

    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=256, verbose_name="Product Name")
#     description = models.TextField(verbose_name="Product Description")
#     status = models.CharField(
#         choices=STATUS_CHOICES, max_length=10, verbose_name="Status"
#     )
#     category = models.ForeignKey(
#         Category,
#         related_name="products",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         verbose_name="Category",
#     )
#     quantity = models.IntegerField(default=0)
#     cost = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Cost Price"
#     )
#     price = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Selling Price"
#     )
#     supplier = models.ForeignKey(
#         Supplier,
#         related_name="products",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         verbose_name="Supplier",
#     )
#     discount_value = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         verbose_name="Discount Value",
#     )
#     is_featured = models.BooleanField(default=False, verbose_name="Is Featured")
#     expiring_date = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
#     updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

#     class Meta:
#         db_table = "product"

#     def __str__(self):
#         return f"{self.name}: (Cost: {self.cost}, Price: {self.price})"


#     def to_json(self):
#         item = model_to_dict(self)
#         item.update(
#             {
#                 "id": self.id,
#                 "text": self.name,
#                 "category": self.category.name if self.category else None,
#                 "quantity": (
#                     self.inventory.quantity if hasattr(self, "inventory") else 0
#                 ),
#                 "total_product": 0,
#             }
#         )
#         return item

#     def apply_discount(self):
#         """Apply the percentage discount to the price of the product."""
#         if self.discount_value:  # Assume all discounts are percentages
#             self.price -= self.price * self.discount_value / 100

#             # Ensure the price doesn't go below zero
#             self.price = max(0, self.price)
#             self.save()

#     def get_discounted_price(self):
#         """Get the discounted price with a percentage discount applied."""
#         discounted_price = self.price
#         if self.discount_value:  # Assume all discounts are percentages
#             discounted_price -= self.price * self.discount_value / 100

#         return max(0, discounted_price)
    
#     @property
#     def prefixed_id(self):
#         return f"SKU{self.pk:03d}"


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Product Name"
    )
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU", blank=True)
    description = models.TextField(
        verbose_name="Product Description"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        verbose_name="Status"
    )
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Category"
    )
    supplier = models.ForeignKey(
        Supplier,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Supplier"
    )
    quantity = models.IntegerField(
        default=0
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cost Price"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Selling Price"
    )
    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Discount Value"
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Is Featured"
    )
    expiring_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Expiring Date"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: (Cost: {self.cost}, Price: {self.price})"

    def to_json(self):
        item = model_to_dict(self)
        item.update(
            {
                "id": self.id,
                "text": self.name,
                "category": self.category.name if self.category else None,
                "quantity": (
                    self.inventory.quantity if hasattr(self, "inventory") else 0
                ),
                "total_product": 0,
            }
        )
        return item

    def apply_discount(self):
        """Apply the percentage discount to the price of the product."""
        if self.discount_value:  # Assume all discounts are percentages
            self.price -= self.price * self.discount_value / 100

            # Ensure the price doesn't go below zero
            self.price = max(0, self.price)
            self.save()

    def get_discounted_price(self):
        """Get the discounted price with a percentage discount applied."""
        discounted_price = self.price
        if self.discount_value:  # Assume all discounts are percentages
            discounted_price -= self.price * self.discount_value / 100

        return max(0, discounted_price)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = str(uuid.uuid4()).split('-')[0].upper()  # e.g., 'F3D9A7'
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = CloudinaryField(
        "image",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            validate_image_size,
        ],
        null=True,
        blank=True,
    )
    is_default = models.BooleanField(default=False, verbose_name="Is Default")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "product_image"
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Image for {self.product.name} (Default: {self.is_default})"

    def clean(self):
        # Ensure only one default image is set per product
        if self.is_default:
            default_image_exists = (
                ProductImage.objects.filter(product=self.product, is_default=True)
                .exclude(id=self.id)
                .exists()
            )

            if default_image_exists:
                raise ValidationError("Only one default image can be set per product.")

    def save(self, *args, **kwargs):
        # Ensure no other images are marked as default if this one is set as default
        if self.is_default:
            ProductImage.objects.filter(product=self.product, is_default=True).update(
                is_default=False
            )

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.image and not str(self.image).startswith("http"):
            upload_result = cloudinary.uploader.upload(
                self.image.file, folder="stock_track_product_images"
            )
            self.image = upload_result["url"]
        super().save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField(
        choices=[(i, f"{i} Stars") for i in range(1, 6)]
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user} for {self.product.name}"
