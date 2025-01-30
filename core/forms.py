"""
Autor: Emerson ibañez
Fecha: 2025-01-30
Descripción: 
"""
"""
Autor: Emerson Ibañez
Fecha: 30
Proyecto: Sistema de Control Académico
Descripción:  ADV 2025
"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from accounts.models import Profile
from .models import Course,Materia
from .models import Schedule


class LoginForm(AuthenticationForm):
    pass
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
    def clean_email(self):
            email_field = self.cleaned_data['email']
            if User.objects.filter(email=email_field).exists():
                raise forms.ValidationError('Este correo electrónico ya está registrado')
            
            return email_field
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'address', 'location', 'telephone'] 

class CourseForm(forms.ModelForm):
    materias = forms.ModelMultipleChoiceField(
        queryset=Materia.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Materias'
    )
    # Restricción de longitud en el campo 'description'
    description = forms.CharField(
        max_length=20,  # Limitar la descripción a 20 caracteres
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}),
        label='Descripción'
    )
    class Meta:
        model = Course
        fields = ['name', 'description', 'materias']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Estilo para el campo 'name'
            'description': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}),  # Estilo para 'description'

        }
        
# FORMULARIO DE NUEVO USUARIO
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso. Por favor, elige otro.")
        return username
        
#form de teacher ateendence
class AttendanceForm(forms.Form):
    ci = forms.CharField(label='Código del Profesor', max_length=20)
    
#cambiar de profesor las materias
class EditMateriaForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='profesores').order_by('first_name'),
        label="Profesor",
        widget=forms.Select
    )

    def __init__(self, *args, **kwargs):
        super(EditMateriaForm, self).__init__(*args, **kwargs)
        # Personalizar las etiquetas del campo 'teacher' para mostrar nombre completo
        self.fields['teacher'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = Materia
        fields = ['name', 'description', 'teacher']


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = User.objects.filter(groups__name='profesores').order_by('first_name')
        self.fields['teacher'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        
        
#form de pdf horario
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['file']

#form libros
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'published_date', 'pdf']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'description': 'Categoria',
            'published_date': 'Fecha de publicación',
            'pdf': 'Archivo PDF',
        }
