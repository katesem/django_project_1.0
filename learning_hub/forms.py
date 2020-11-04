from django import forms
from .models import Users, Questions, Quiz, Topic
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
            'email': 'Must contain only letters.', 
            'username': 'Must contain at least 6 including only letters, numbers or underscore. ',
            'password': 'Must contain at least 6 symbols including at least 1 letter and 1 number.',
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
            raise forms.ValidationError('Username must contain at least 4 symbols.')
         
        elif   re.search(r'[^a-zA-Z0-9_]', username ):
            raise forms.ValidationError('Username can contain only specified symbols.')
        
        
        if len(password) < 6:
            raise forms.ValidationError('Password must contain at least 6 symbols.')
        
        elif  not re.search('[A-Za-z]', password) or not  re.search('[0-9]', password) or re.search(r'[^a-zA-Z0-9_]', password):
            raise forms.ValidationError('Password can contain only specified symbols.')
        
        if ch_password != password:
            raise forms.ValidationError('Entered passwords don\'t match. Check your input.')
         
        return cleaned_data
    
    
    
class LoginForm(forms.Form):
    Username = forms.CharField( widget =  forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}))
    Password = forms.CharField( widget = forms.PasswordInput(attrs = { 'class' :'form-control','style': 'font-size: x-large'}))
            

    def get_user(self):
        return self.user or None
    
    
    
class QuestionSingleOrderForm(forms.ModelForm):
        
    class Meta:
        model = Questions
        fields = '__all__'
        fields_required = '__all__'
        
        help_texts = {'answer': 'Order a suitable option number'}

        widgets = {
            'question':forms.Textarea(attrs = { 'class' :'form-control','style': 'font-size: x-large', 'rows' : 3, 'cols' : 10}),
            'option1': forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'option2': forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'option3': forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'option4': forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}),
            'answer': forms.TextInput(attrs={'min': 1,'max': 4,'type': 'number','class' :'form-control','style': 'font-size: x-large'})
        }

    def __init__(self, *args, **kwargs):
        super(QuestionSingleOrderForm, self).__init__(*args, **kwargs)
  

# choice stucture for  QuizCreationForm multiplechoicefield 
quiz_choice = list()
for el in list(Questions.objects.all()):
    quiz_choice.append(tuple([el.id, el.question]))


topic_choice = list()
for el in list(Topic.objects.all()):
    topic_choice.append(tuple([el.id, el.topic_name]))
    
    
class QuizCreationForm(forms.ModelForm):
    
    questions = forms.MultipleChoiceField( choices = tuple(quiz_choice), help_text = 'Hold the "Ctrl" key to select more than 1 option')
    quiz_name = forms.CharField(widget = forms.TextInput)
    
    class Meta:
        model = Quiz
        fields = ['questions', 'quiz_name']
        fields_required = '__all__'

    
        

class TopicCreationForm(forms.ModelForm):
    
    topic_name = forms.CharField(label = 'Topic name', help_text = 'It should contain letters and possibly  numbers', widget = forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}))
    
    class Meta:
        model = Topic
        fields = ['topic_name']
        
    def clean(self):
        cleaned_data = super(TopicCreationForm, self).clean()
        n_topic = self.cleaned_data['topic_name']
        present_topic = Topic.objects.filter(topic_name = n_topic)
        
        if re.search(r'[^a-zA-Z0-9 ]', n_topic ) or n_topic.isdigit()  :
            raise forms.ValidationError('Topic name can contain only specified symbols.')
        if present_topic.exists():
            raise forms.ValidationError('Topic with this name already exists.')
        return cleaned_data


class TopicOrderForm(forms.Form):
    topic_id = forms.ChoiceField(label = 'Select suitable topic name ', choices = topic_choice, required = True)


class ContactForm(forms.Form):
    email = forms.EmailField(required = True, widget = forms.EmailInput(attrs={'class' :'form-control','style': 'font-size: x-large'}))
    subject = forms.CharField(required = True, widget = forms.TextInput(attrs={'class' :'form-control','style': 'font-size: x-large'}))
    message = forms.CharField(required = True , widget = forms.Textarea(attrs = { 'class' :'form-control','style': 'font-size: x-large', 'rows' : 3, 'cols' : 10}) )