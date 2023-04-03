from django.db import models

from jabbariao.core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=140, null=True, blank=True)
    content = models.TextField(null=True)

    class Meta:
        indexes = [models.Index(fields=["title"], name="title_index")]
