from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Code
from django.forms import ModelForm

class UserRegister(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = ['username','email','phone','password1','password2']


class UserChange(UserChangeForm):
    class Meta:
        model= CustomUser
        fields = ['username','email','phone']


class CodeForm(ModelForm):
    class Meta:
        model = Code
        fields = ('otp',)


