from django.db import models


class About(models.Model):
    content = models.TextField(verbose_name="İçerik")
    created_at = models.DateTimeField(verbose_name='Oluştururma Tarihi', auto_now_add=True)

    def __str__(self) -> str:
        return "İçerik Eklendi"
    
    class Meta:
        db_table = 'about'
        managed = True
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızda Ayarları'
        ordering =["-id"]