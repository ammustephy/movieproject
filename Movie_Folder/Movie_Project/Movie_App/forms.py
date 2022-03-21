from django import forms
from .models import picture

class movieform(forms.ModelForm):
    class Meta:
        model=picture
        fields=['name','desc','year','img']