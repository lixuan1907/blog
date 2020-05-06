
from django.db import models
class BaseModel(models.Model):
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True

class JokeDz(BaseModel):
    title = models.CharField(max_length=30)
    nvum = models.PositiveIntegerField(blank=True, null=True)
    like_num = models.PositiveIntegerField(blank=True, null=True)
    no_like = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    is_hot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joke_Dz'


class JokeTU(BaseModel):
    img = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=30)
    nvum = models.PositiveIntegerField(blank=True, null=True)
    like_num = models.PositiveIntegerField(blank=True, null=True)
    no_like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joke_TU'
