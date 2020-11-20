from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Localizacion, Categoria

class UserForm(UserCreationForm):
    # django.contrib.auth.User attributes
    primer_nombre = forms.CharField(max_length=150, required=False)
    apellidos = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(max_length=150)

    # Profile attributes
    DNI = forms.CharField(max_length=8)
    fecha_de_nacimiento = forms.DateField()
    estado = forms.CharField(max_length=3)
    ## Opciones de genero
    MASCULINO = 'MA'
    FEMENINO = 'FE'
    NO_BINARIO = 'NB'
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (NO_BINARIO, 'No Binario')
    ]
    genero = forms.ChoiceField(choices=GENERO_CHOICES)

    # Cliente attributes
    preferencias = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)



    class Meta:
        model = User
        fields = ['username',
        'primer_nombre',
        'apellidos',
        'email',
        'DNI',
        'fecha_de_nacimiento',
        'estado',
        'genero',
        'preferencias',
        ]







