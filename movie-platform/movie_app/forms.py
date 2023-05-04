from django import forms
from .models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=('name','decscription','year','image')
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'decscription': forms.Textarea(attrs={'class': 'form-control'}),
        #     'year': forms.TextInput(attrs={'type':'number'}),
        #     'image': forms.TextInput(attrs={'type':'file'}),
        # }

