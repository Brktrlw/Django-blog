from django.contrib import admin
from .models import Article

#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","createdDate"]
    class Meta:
        model=Article

# Register your models here.
