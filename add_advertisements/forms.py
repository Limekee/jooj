from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model=Advertisement
        fields=['title', 'description', 'price', 'auction', 'image', 'id']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'title':forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description' : forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price':forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image' : forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }
    def clean_title(self):
        title=self.cleaned_data['title']
        if title[0]=='?':
            raise ValidationError('заголовок не может начинаться с вопросительного знака')
        return title
