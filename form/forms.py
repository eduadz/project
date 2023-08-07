from django import forms
from .models import usuario

class formularioCadastro(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('nome', 'email')
    