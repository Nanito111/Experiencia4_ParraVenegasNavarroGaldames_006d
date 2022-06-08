from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User

class CuentaForm(ModelForm):
    
    class Meta:
        model = Cuenta
        fields = ['usuario', 'nombre', 'apellido','correo','password']
    
    

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('username', 'password', 'groups', 'user_permissions', 'is_staff', 'is_active',
                   'is_superuser', 'last_login', 'date_joined')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].label = 'Nombre'
        self.fields["last_name"].label = 'Apellido'
        self.fields["email"].label = 'Correo electrónico'
            

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget = forms.TextInput(
        attrs= {'class': 'form-control',
                'placeholder': '',
                'id': 'hello',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {'class': 'form-control',
                'placeholder': '',
                'id': 'hi'}))

class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(min_length=3, max_length=20, label="Nombre de usuario", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'juanperez',
                 'id': 'username',
                 'onkeyup': 'testing()'}))
    first_name = forms.CharField(max_length=50, label="Nombre", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Juan',
                 'id': 'name'}))
    last_name = forms.CharField(max_length=50, label="Apellido", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Perez',
                 'id': 'surname'}))
    email = forms.CharField(max_length=100, label="Correo electrónico", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'juan_perez@email.com',
                 'id': 'mail'}))
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput(
        attrs = {'class': 'form-control',
                 'placeholder': '',
                 'id': 'password1'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget = forms.PasswordInput(
        attrs = {'class': 'form-control',
                 'placeholder': '',
                 'id': 'password2'}))
    def clean_username(self):
        username = self.cleaned_data["username"]
        existe = User.objects.filter(username = username).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        return username
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
        
        for fieldName in ['username', 'password1', 'password2']:
            self.fields[fieldName].help_text = None

class EditUserForm(CustomUserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        exclude = ['username']



class SoporteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Juan',
                 'id': 'name'}))
    correo = forms.CharField(max_length=100, label="Correo electrónico", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'juan_perez@email.com',
                 'id': 'mail'}))
    tipo_consulta = forms.IntegerField(label="Tipo de consulta", widget = forms.Select(
        choices = ( 
            (0, 'Sugerencia'),
            (1, 'Problema'),
            (2, 'Comentario'),
            (3, 'Otro') ),
        attrs = {'class': 'form-select',
                 'id': 'name'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.Textarea(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un mensaje aqui',
                 'id': 'name',
                 'rows': 4}))

    class Meta:
        model = Soporte
        fields = ["nombre", "correo", "tipo_consulta", "mensaje"]

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Juan',
                 'id': 'name'}))
    correo = forms.CharField(max_length=100, label="Correo electrónico", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'juan_perez@email.com',
                 'id': 'mail'}))
    telefono = forms.CharField(max_length=12, label="Telefono", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': '569123456789',
                 'id': 'name'}))
    asunto = forms.CharField(max_length=100, label="Asunto", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un asunto',
                 'id': 'name'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.Textarea(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un mensaje aqui',
                 'id': 'name',
                 'rows': 4}))
    class Meta:
        model = Contacto
        fields = '__all__'

class RemoveForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)