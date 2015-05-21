from django.contrib import admin

from contact_form.models import Communication


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent',)

admin.site.register(Communication, ContactFormAdmin)
