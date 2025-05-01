from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Supplier Name")
    contact_name = models.CharField(max_length=255, verbose_name="Contact Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = PhoneNumberField(
        null=True, blank=True, default="+12125552368", verbose_name="Telephone"
    )
    address = models.CharField(max_length=255, verbose_name="Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    
    def __str__(self):
        return self.name

    def clean(self):
        self.validate_name()
        self.validate_email()
        self.validate_phone()

    def validate_name(self):
        if not self.name.strip():
            raise ValidationError("Supplier name cannot be empty.")

    def validate_email(self):
        if not self.email:
            raise ValidationError("Email address cannot be empty.")

    def validate_phone(self):
        if self.phone:
            try:
                parsed_phone = phonenumbers.parse(str(self.phone), None)
                if not phonenumbers.is_valid_number(parsed_phone):
                    raise ValidationError("Phone number is invalid.")
            except phonenumbers.NumberParseException:
                raise ValidationError("Phone number could not be parsed.")


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('cancelled', 'Cancelled'),
    ]

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"PO#{self.id} - {self.supplier.name}"

    def total_amount(self):
        return sum(item.total_price() for item in self.items.all())

    @property
    def aggregate_total_quantity(self):
        return self.items.aggregate(total=Sum('quantity'))['total'] or 0

    class Meta:
        db_table = 'purchase_order'
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Orders'
        ordering = ['-created_at']


class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def total_price(self):
        return self.quantity * self.unit_price

    class Meta:
        db_table = 'purchase_order_item'
        verbose_name = 'Purchase Order Item'
        verbose_name_plural = 'Purchase Order Items'
        ordering = ['-created_at']