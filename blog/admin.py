from django.contrib import admin
from blog.models import User, Article, Comments, Reading_List

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(Reading_List)