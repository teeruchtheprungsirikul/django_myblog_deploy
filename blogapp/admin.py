from django.contrib import admin
from .models import Blog, Author, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Blog)

# class BlogAdmin(admin.ModelAdmin):
#     """Register model by Modeladmin"""
    
#     list_display = ('title', 'post', 'date_created', 'date_updated')
    
# admin.site.register(Blog, BlogAdmin)


# Register your SummernoteModelAdmin here.

class BlogAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'date_created', 'date_updated', 'author')
    summernote_fields = '__all__'
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Contact)
