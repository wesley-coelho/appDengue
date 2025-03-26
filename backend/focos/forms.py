from django import forms
from .models import Foco

class FocoForm(forms.ModelForm):
    class Meta:
        model = Foco
        fields = ['bairro', 'endereco', 'numero', 'cep', 'foto', 'descricao']