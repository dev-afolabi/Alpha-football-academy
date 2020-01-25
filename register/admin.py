from django.contrib import admin
from .models import Register

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname','email', 'programe_option', 'submitted',)
    list_filter = ('submitted',)
    readonly_fields = ('submitted',)

    fieldsets = (
        (None, {
            'fields':('firstname', 'lastname', 'email', 'programe_option',)
        }),
    )

admin.site.register(Register, RegisterAdmin)
