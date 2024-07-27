from django.db import models


class OurPurpose(models.Model):
    content = models.TextField(verbose_name="İçerik")
    created_at = models.DateTimeField(verbose_name='Oluştururma Tarihi', auto_now_add=True)

    def __str__(self) -> str:
        return "İçerik Eklendi"
    
    class Meta:
        db_table = 'our_purpose'
        managed = True
        verbose_name = 'Amacımız'
        verbose_name_plural = 'Amacımız alanı'
        ordering =["-id"]