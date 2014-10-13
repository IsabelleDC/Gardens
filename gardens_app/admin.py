from django.contrib import admin

# Register your models here.
from gardens_app.models import Visitor, Feed, Category

admin.site.register(Visitor)
admin.site.register(Feed)
admin.site.register(Category)
