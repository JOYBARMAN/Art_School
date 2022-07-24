from django.db import models
from django.contrib.auth.models import User


BLOOD_CHOICES=(
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("O+","O+"),
    ("O-","O-"),
    ("AB+","AB-")
)
GENDER_CHOICES=(
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)
PAYMENT_STATUS=(
    ("paid","paid"),
    ("not_Paid","not_paid"),
    ("not_updated_yet","not_updated_yet")
)

CLASSES_AGE=(
    ("1-5 Years","1-5 Years"),
    ("1-10 Years","1-10 Years"),
    ("1-15 Years","1-15 Years"),
    ("1-20 Years","1-20 Years"),
    ("All Ages Student","All Ages Student")
)

class Group(models.Model):
    group=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.group

class Student(models.Model):
    name =models.CharField(max_length=255)
    roll =models.CharField(max_length=255)
    group =models.ForeignKey(Group,on_delete=models.CASCADE)
    email =models.EmailField(max_length=255,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    mobile =models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/student/')
    blood =models.CharField(max_length=10,choices=BLOOD_CHOICES)
    address =models.CharField(max_length=255,null=True,blank=True)
    father_name =models.CharField(max_length=255,null=True,blank=True)
    mother_name =models.CharField(max_length=255,null=True,blank=True)
    admission_date =models.DateField()

    def __str__(self):
        return self.name + " | " + str(self.group.group)


class Payment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    january=models.CharField(max_length=255,choices=PAYMENT_STATUS,default="not_updated_yet")
    february = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    march = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    april = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    may = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    june = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    july = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    august = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    september = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    october = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    november = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")
    december = models.CharField(max_length=255, choices=PAYMENT_STATUS, default="not_updated_yet")

    def __str__(self):
        return self.student.name

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='images/blog/')
    video=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username+" | "+ str(self.title)

class Tutorial(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    video = models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='images/tutorial/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title +" | "+str(self.group.group)


class Feedback(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    date =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " | " + str(self.message[:50])



class Classes(models.Model):
    title=models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/classes/')
    age=models.CharField(max_length=255,choices=CLASSES_AGE)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.age)


class ArtGallery(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    art = models.ImageField(upload_to='images/art_gallery/')
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.description[:50])