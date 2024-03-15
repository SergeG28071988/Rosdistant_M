from .models import Man, Woman
from django.forms import ModelForm, TextInput


class ManForm(ModelForm):
    class Meta:
        model = Man
        fields = ['name', 'surname', 'date_birth', 'place_residence']
        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),

            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),

            "date_birth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),

            "place_residence": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите место проживания'
            }),
        }


class WomanForm(ModelForm):
    class Meta:
        model = Woman
        fields = ['name', 'surname', 'date_birth', 'place_residence']
        widgets = {

            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),

            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),

            "date_birth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),

            "place_residence": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите место проживания'
            }),
        }
