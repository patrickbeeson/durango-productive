from django.contrib import admin

from contact_form.models import Communication

def mark_contacted(modeladmin, request, queryset):
    queryset.update(contacted=True)
mark_contacted.short_description = 'Mark selected communications as ' \
                                   'contacted'

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent', 'contacted', 'contacted_date',)
    list_editable = ('contacted',)
    actions = [mark_contacted]
    readonly_fields = ('contacted_date', 'sent',)

admin.site.register(Communication, ContactFormAdmin)
