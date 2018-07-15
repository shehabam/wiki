from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "The Title is %s \nThe Content is %s\nUpdated On: %s" % (self.title, self.content, self.last_update)
