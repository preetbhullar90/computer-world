from django.db import models


class NewsletterUsers(models.Model):
    """Newsletter Model"""

    class Meta:
        verbose_name_plural = 'NewsletterUsers'
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
