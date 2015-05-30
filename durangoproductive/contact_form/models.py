from datetime import datetime

from django.db import models
from django.utils.html import strip_tags, escape
from django.utils import timezone

now = timezone.now()


class Communication(models.Model):
    """
    Model for messages sent through the website contact form.
    """
    name = models.CharField(
        max_length=200,
    )
    email = models.EmailField()
    message = models.TextField(
        help_text='Note: Plain text only. All HTML will be stripped and '
        'content escaped on submission.'
    )
    sent = models.DateTimeField(
        auto_now_add=True,
        help_text='Date when this communication was sent.'
    )
    contacted = models.BooleanField(
        help_text='Indicates whether the sender has been contacted in '
        'response to their message.',
        default=False
    )
    contacted_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Date when this communication was marked as contacted.'
    )

    class Meta:
        ordering = ('-sent',)
        verbose_name = 'Contact form submission'
        verbose_name_plural = 'Contact form submissions'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        On save, sanitize the message field and set the contacted_date if
        needed.
        """
        self.message = escape(strip_tags(self.message))
        if self.contacted:
            self.contacted_date = now
        else:
            self.contacted_date = None
        super(Communication, self).save(*args, **kwargs)
