from django.db import models
# Create your models here.
#ENUM
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class Movie(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    name = models.CharField(max_length=20)
    year = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)

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
        return self.name
