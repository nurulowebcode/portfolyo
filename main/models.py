from django.db import models


class Enterance(models.Model):
    img = models.ImageField(upload_to='enterance_photo/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=255)
    text_1 = models.TextField()
    text_2 = models.TextField()

    def __str__(self):
        return self.title


class About_me_photo(models.Model):
    img = models.ImageField(upload_to='about_phots/')


class Know_me(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    img = models.ImageField(upload_to='comment_photo/')
    short_text = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    jop = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class About_info(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.IntegerField()
    about_instagram = models.CharField(max_length=200)
    email = models.CharField(max_length=255)


class Info(models.Model):
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=200)
    contact_instagram = models.CharField(max_length=200)
    you_tube = models.CharField(max_length=200)


class Savollar(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()







