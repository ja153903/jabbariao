from django.db import models

from jabbariao.core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
