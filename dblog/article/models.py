from django.db import models

class Category(models.Model):
    lmmc = models.CharField(max_length=20)



    class Meta:
        db_table = 'category'

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(null=True)
    fid = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now: 修改数据时，自动赋值为更新字段时的时间
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'article'


class Photo(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'photo'


