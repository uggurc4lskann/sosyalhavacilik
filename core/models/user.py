from django.db import models


class Title(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Tarih', auto_now_add=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'titles'
        managed = True
        verbose_name = 'Başlık'
        verbose_name_plural = 'Başlıklar'


class UserInfo(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='items')
    content = models.CharField(verbose_name='Madde', max_length=300, null=True, blank=True)


    def __str__(self) -> str:
        return "eklendi"
    
    class Meta:
        db_table = 'userinfo'
        managed = True
        verbose_name = 'Yolcular'
        verbose_name_plural = 'Yolcu uyarıları'