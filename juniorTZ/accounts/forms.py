from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
User=get_user_model()

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Ism',
                               widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'ismingizni yozing'}))

    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput(
                               attrs={'class': 'form-control', 'placeholder': 'parolni yozing'}))
    password2 = forms.CharField(label='Parol tasdiqlang',
                               widget=forms.PasswordInput(
                               attrs={'class': 'form-control', 'placeholder': 'parolni qayta yozing'}))
    class Meta:
        model=User
        fields=['username','password','password2']

    def clean_password2(self):
        password=self.cleaned_data['password']
        password2=self.cleaned_data['password2']
        if password!=password2:
            raise ValidationError('Parollar togri emas!')
        return password2



class UserLoginForm(forms.Form):
    username=forms.CharField(label=mark_safe('Ism'),
                             widget=forms.TextInput(
                             attrs={'class':'form-control','placeholder':'ismingizni yozing'}))

    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput(
                               attrs={'class': 'form-control', 'placeholder': 'parolni yozing'}))

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            qs=User.objects.filter(username=username)
            if not qs.exists():
                raise ValidationError('Foydalanuvchi topilmadi')
            if not check_password(password,qs[0].password):
                raise ValidationError('parol xato!')
            user=authenticate(username=username,password=password)
            if not user:
                raise ValidationError('Foydalanuvchi active emas')
        return super().clean(*args,**kwargs)