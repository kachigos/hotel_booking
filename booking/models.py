from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Banner(models.Model):
    banner = models.TextField(verbose_name='Название банера')

    def __str__(self):
        return self.banner


class Desc(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    theme = models.CharField(max_length=50)
    desc = models.TextField()
    right = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100, verbose_name='Имя комментатора')
    text = models.TextField(verbose_name='Текст отзыва')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя комментатора')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.name

class Video(models.Model):
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='photo')

    def __str__(self):
        return self.title

class AboutImg(models.Model):
    images = models.ForeignKey(AboutUs, related_name='image', on_delete=models.CASCADE)


class Awards(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=250, verbose_name='Награда')
    sub_title = models.CharField(max_length=250, null=True, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    img = models.ImageField(upload_to='service_img')
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Add_service(models.Model):
    img = models.ImageField(upload_to='add_service_img')
    sub_title = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    img = models.ImageField(upload_to='blog_img')
    add_time = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=16)
    ws_number = models.CharField(max_length=16)
    address = models.CharField(max_length=200)

    def __str__(self):
        return '__all__'

class Questions(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.ImageField(null=True, blank=True)
    number = models.CharField(max_length=20)
    sms = models.TextField()

    def __str__(self):
        return self.sms