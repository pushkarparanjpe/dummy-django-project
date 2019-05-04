from django.contrib import admin
import helloapp.models


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(helloapp.models.Message, MessageAdmin)
