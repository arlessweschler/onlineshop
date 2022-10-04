from django import forms
from django.contrib.auth.models import User

def validator_phone(value):
    if not value.isnumeric():
        raise forms.ValidationError('Поле должно содержать только цифры')
    if len(value) < 9:
        raise forms.ValidationError('Некорректный номер')

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Логин')
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())
    email = forms.EmailField(label='Электронная почта')

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ChangeUserlnfoForm(forms.ModelForm):
    phone = forms.CharField( label='Телефон', validators=[validator_phone], required=False)
    postal_code = forms.CharField(max_length=20, label='Почтовый индекс', required=False)
    city = forms.CharField(max_length=100, label='Город', required=False)
    street = forms.CharField(max_length=100, label='Улица', required=False)
    house = forms.CharField(max_length=100, label='Дом', required=False)
    building = forms.CharField(max_length=100, label='Корпус', required=False)
    apartment = forms.CharField(max_length=100, label='Квартира', required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'postal_code', 'city', 'street', 'house', 'building', 'apartment')