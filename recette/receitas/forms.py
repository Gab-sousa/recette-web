from django import forms
from .models import Ingrediente, Receita

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome']

class ReceitaForm(forms.ModelForm):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Ingredientes existentes'
    )
    ingredientes_personalizados = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    imagem = forms.ImageField(required=False)  

    class Meta:
        model = Receita
        fields = ['titulo', 'descricao', 'ingredientes', 'ingredientes_personalizados', 'instrucoes', 'equipamentos', 'porcoes', 'imagem']

class GerarReceitaIAForm(forms.Form):
    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
)