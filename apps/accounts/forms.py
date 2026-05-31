
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
   password = forms.CharField(
      widget=forms.PasswordInput
   )
   class Meta:
      model = User
      fields = [
         'username',
         'email',
         'password'
      ]
   
   def clean_email(self):
      email = self.cleaned_data['email']
      if User.objects.filter(email=email).exists():
         raise forms.ValidationError(
            'Email already exists'
         )
      return email
   
   def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(
         self.cleaned_data['password']
      )
      if commit:
         user.save()
      
      return user 
   
