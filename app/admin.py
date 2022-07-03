from django.contrib import admin

from app.models import Fetured

# Register your models here.
@admin.register(Fetured)
class feturedAdmin(admin.ModelAdmin):
    list_display=['name','img','info','writter','avatar']