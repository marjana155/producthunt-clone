from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
