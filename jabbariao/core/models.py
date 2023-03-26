from django.db import models


class BaseModel(models.Model):
    """
    BaseModel is an abstract Django model that includes
    basic fields for all models to inherit.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
