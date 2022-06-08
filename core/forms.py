from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.models import User    

class UserChangeForm(forms.ModelForm):
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
    
    username = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control','id': 'username','type':'text'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control','id': 'password','type':'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("")
        return self.cleaned_data
    
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=3, max_length=21, widget = forms.TextInput(attrs = {'class': 'form-control','id': 'username'}))
    first_name = forms.CharField(max_length=65, widget = forms.TextInput(attrs = {'class': 'form-control','id': 'first_name'}))
    last_name = forms.CharField(max_length=65, widget = forms.TextInput(attrs = {'class': 'form-control','id': 'last_name'}))
    email = forms.CharField(max_length=101, widget = forms.EmailInput(attrs = {'class': 'form-control','id': 'email'}))
    password1 = forms.CharField(max_length=51, widget = forms.PasswordInput(attrs = {'class': 'form-control','id': 'password1'}))
    password2 = forms.CharField(max_length=51, widget = forms.PasswordInput(attrs = {'class': 'form-control','id': 'password2'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']

        if commit:
            user.save()
        
        return user

class EditUserForm(RegisterForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        exclude = ['username']



class SoporteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'id': 'name'}))
    correo = forms.CharField(max_length=100, label="Correo electrónico", widget = forms.EmailInput(
        attrs = {'class': 'form-control',
                 'id': 'email'}))
    tipo_consulta = forms.IntegerField(label="Tipo de consulta", widget = forms.Select(
        choices = ( 
            (0, 'Sugerencia'),
            (1, 'Problema'),
            (2, 'Comentario'),
            (3, 'Otro') ),
        attrs = {'class': 'form-select',
                 'id': 'tipo_consulta'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.Textarea(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un mensaje aqui',
                 'id': 'message',
                 'rows': 4}))

    class Meta:
        model = Soporte
        fields = ["nombre", "correo", "tipo_consulta", "mensaje"]

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'id': 'name'}))
    correo = forms.CharField(max_length=100, label="Correo electrónico", widget = forms.EmailInput(
        attrs = {'class': 'form-control',
                 'id': 'email'}))
    telefono = forms.CharField(max_length=12, label="Telefono", widget = forms.NumberInput(
        attrs = {'class': 'form-control',
                 'placeholder': '569123456789',
                 'id': 'number'}))
    asunto = forms.CharField(max_length=100, label="Asunto", widget = forms.TextInput(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un asunto',
                 'id': 'asunto'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.Textarea(
        attrs = {'class': 'form-control',
                 'placeholder': 'Ingrese un mensaje aqui',
                 'id': 'message',
                 'rows': 4}))
    class Meta:
        model = Contacto
        fields = '__all__'

class RemoveForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)