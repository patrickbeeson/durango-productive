from django.db import models


class Communication(models.Model):
    """
    Model for messages sent through the website contact form.
    """
    name = models.CharField(
        max_length=200,
    )
    email = models.EmailField()
    message = models.TextField()
    sent = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-sent',)
        verbose_name = 'Contact form submission'
        verbose_name_plural = 'Contact form submissions'

    def __str__(self):
        return self.name
