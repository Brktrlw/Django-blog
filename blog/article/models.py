from django.db import models

class ArticleType(models.Model):
    articleType=models.CharField(max_length=50)
    def __str__(self):
        return self.articleType
class Article(models.Model):
    author     = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title      = models.CharField(max_length=50,verbose_name="Başlık")
    content    = models.TextField(max_length=100,verbose_name="İçerik")
    createdDate= models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    articleImage=models.FileField(blank=True,null=True)
    Atype      = models.ForeignKey(ArticleType,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title



