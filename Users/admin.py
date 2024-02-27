from django.contrib import admin

from Users.models import Contact, Feedback, Registration

# Register your models here.
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Registration)
