from django import forms
from .models import Users
from django.contrib.auth import logout, authenticate, login, get_user_model
import re


Users = get_user_model()

class UserCreationForm(forms.ModelForm):
    check_password = forms.CharField(label = "Repeat password ", widget = forms.PasswordInput(attrs = { 'class' :'form-control','style': 'font-size: x-large'}))
    class Meta:
        model = Users
        fields = ['email', 'username', 'password']
        fields_required = '__all__'
         
        help_texts = {
            'email': 'Must contain only letters', 
            'username': 'Must contain at least 6 including only letters, numbers or underscore ',
            'password': 'Must contain at least 6 symbols including at least 1 letter and 1 number',
        }
        
        widgets = {
            'email': forms.EmailInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'username': forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'password':forms.PasswordInput(attrs = { 'class' :'form-control','style': 'font-size: x-large'})
        }
         
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        ch_password = self.cleaned_data['check_password']
        
        if  len(username) < 4  :
            raise forms.ValidationError('Username must contain at least 4 symbols')
         
        elif   re.search(r'[^a-zA-Z0-9_]', username ):
            raise forms.ValidationError('Username can contain only specified symbols.')
        
        
        if len(password) < 6:
            raise forms.ValidationError('Password must contain at least 6 symbols')
        
        elif  not re.search('[A-Za-z]', password) or not  re.search('[0-9]', password) or re.search(r'[^a-zA-Z0-9_]', password):
            raise forms.ValidationError('Password can contain only specified symbols')
        
        if ch_password != password:
            raise forms.ValidationError('Entered passwords don\'t match. Check your input.')
         
        return cleaned_data
    
    
    
class LoginForm(forms.Form):
    Username = forms.CharField( widget =  forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}))
    Password = forms.CharField( widget = forms.PasswordInput(attrs = { 'class' :'form-control','style': 'font-size: x-large'}))
            

    def get_user(self):
        return self.user or None
    
    
''' 

    def clean(self):                                        #provide additional validation
        cleaned_data = super(LoginForm, self).clean()
        
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError('Invalid entered data. Repeat input.')
            self.user = user
        
        return cleaned_data

    def get_user(self):
        return self.user or None
   
'''
    
        
    