from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'subject','email', 'message', 'submitted',)
    list_filter = ('submitted', 'subject',)
    readonly_fields = ('submitted',)

    fieldsets = (
        (None, {
            'fields':('fullname', 'subject', 'email', 'message',)
        }),
    )

admin.site.register(Contact, ContactAdmin)
