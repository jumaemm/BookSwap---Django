from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Book(models.Model):
    title = models.CharField(max_length = 50, blank = False)
    description = models.TextField(blank = False, null = False)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    owner = models.ForeignKey(User, related_name = "book_owner", on_delete = models.CASCADE)
    listed_date = models.DateTimeField(default = timezone.now())
    posted_date = models.DateTimeField(blank=True, null=True)

    def post_book(self):
        self.posted_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("book_detail", kwargs = {'pk':self.pk})


    def __str__(self):
        return self.title
