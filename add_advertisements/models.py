from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model # получаем модель пользователя
from django.utils import timezone
from django.utils.html import format_html
User=get_user_model()
class Advertisement(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    id = models.CharField("id", max_length=64, primary_key=True)
    title=models.CharField('заголовок', max_length=128)
    description=models.TextField('описание')
    price=models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField('изобажение', upload_to='advetisements/')
    def __str__(self):
        return '<Advertisement: Advertisement(id={}, title={}, price={})>.'.format(self.id, self.title, self.price)
    class Meta:
        db_table = "advertisements"
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date()==timezone.now().date():
            created_time=self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}', created_time)
        return format_html('<span style="color: green; font-weight: bold;"{}', self.created_at)
    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date()==timezone.now().date():
            up_time=self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}', up_time)
        return format_html('<span style="color: green; font-weight: bold;"{}', self.updated_at)
    @admin.display(description='Фото')
    def photo(self):
        if self.image:
            return format_html('<img src="{}" width="100px">', self.image.url)
        return format_html('<img src="http://127.0.0.1:8000/media/advertisements/rora.png" width="100px">')

