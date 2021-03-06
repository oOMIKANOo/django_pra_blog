from django.db import models

# Create your models here.


class SampleModel(models.Model):
    title = models.CharField(max_length=1000)
    number = models.IntegerField()


CATEGORY = (('business', 'ビジネス'), ('life', 'ライフ'), ('other', 'その他'))


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.title
