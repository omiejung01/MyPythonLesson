from django.db import models

# Create your models here.
# Create your models here.
#ENUM
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class Account(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    account_id = models.CharField(max_length=20)
    account_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200,default="Liability")
    remarks = models.CharField(max_length=200,default="")

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.account_id


class Transfer(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    transfer_id = models.CharField(max_length=20)
    account_from = models.CharField(max_length=20)
    account_to = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    remark = models.CharField(max_length=200)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.transfer_id

