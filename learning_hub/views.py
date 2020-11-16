from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, QuestionSingleOrderForm, QuizCreationForm , TopicCreationForm, TopicOrderForm, ContactForm
from .models import Users, Topic, Quiz, Questions
from django.contrib import messages
from django.contrib.auth import  logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER 
from django.core.paginator import EmptyPage, InvalidPage, Paginator

Users = get_user_model()


def homepage(request):
    return render(request, 'homepage.html')


def about_page(request):
    return render(request, 'about.html' )


def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = Users.create(form.cleaned_data['email'], form.cleaned_data['username'], form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['Username'], password = form.cleaned_data['Password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'log_in.html', {'form':  LoginForm(), 'u_error':'Your entered wrong data. Check your input and repeat log in.'})

    return render(request, 'log_in.html', {'form':  LoginForm()})


def log_out(request):
    logout(request)
    return redirect('/')


def my_account(request):
    return render(request, 'my_account.html')


@login_required()
def create_question(request):
    if request.method == "POST":
        form = QuestionSingleOrderForm(request.POST)

        if form.is_valid():
            if form.instance.answer == '1':                    # needs some js for better working
                form.instance.answer = form.instance.option1
            elif form.instance.answer == '2':
                form.instance.answer = form.instance.option2
            elif form.instance.answer == '3':
                form.instance.answer = form.instance.option3
            else:
                form.instance.answer == form.instance.option4
            form.save()
            return redirect('/my_account')
    return render(request, 'c_question.html', {'form' : QuestionSingleOrderForm()})



@login_required
def create_quiz(request):
    if request.method == "POST":
        quiz_form = QuizCreationForm(request.POST)
        select_form = TopicOrderForm(request.POST)
        if select_form.is_valid():
            if quiz_form.is_valid():
                quiz = Quiz.create(select_form.cleaned_data['topic_id'], quiz_form.cleaned_data['questions'], quiz_form.cleaned_data['quiz_name'])
            return redirect('/my_account')
    return render(request, 'c_quiz.html', {'form1': QuizCreationForm, 'form2':  TopicOrderForm, 'options': Questions.objects.all()})


def topic_by_id(request, topic_id):
    return render(request, 'topic_by_id.html', context = {'qz': Quiz.objects.filter(topic_id_id = topic_id)})


def create_topic(request):
    if request.method == "POST":
        creation_form = TopicCreationForm(request.POST)
        if creation_form.is_valid() :
            creation_form.save()
            return redirect('/create_quiz')
    return  render(request, 'c_topic.html', {'creation_form': TopicCreationForm })



def take_a_quiz(request, quiz_id):
    if request.method == "POST":
        request.session['quiz_id'] = quiz_id
        request.session['answers'] = request.POST.getlist('answer')
        return redirect('/quiz_results')
    else:
        questions_list = [ Questions.objects.get(id = q) for q in Quiz.objects.get(id = quiz_id).questions]
        
        return render(request,'take_a_quiz.html', {'quests': questions_list, 
                                                   'quiz_name' : Quiz.objects.get(id = quiz_id).quiz_name
                                                   })
    
    
    
def quiz_results(request):
    score, answer_list = 0, []
    answers = request.session['answers']
    quests = Quiz.objects.get(id = request.session['quiz_id']).questions 
    
    for ans,que in zip(answers, quests):
        answer_list.append(Questions.objects.get(id = int(que)).answer)
        if Questions.objects.get(id = int(que)).answer == ans:
            score += 1

    score = score / len(Quiz.objects.get(id = request.session['quiz_id']).questions) * 100

    return render(request, 'quiz_res.html', {'score': int(score),
                                             'answer_list': zip(answer_list, answers)})




def password_redirect(request):
    return redirect('/log_in')



def all_topics(request):
    return render(request, 'all_topics.html', {'topics': Topic.objects.all()})

    
    
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            send_mail(
            form.cleaned_data['subject'],
            form.cleaned_data['message'],
            form.cleaned_data['email'],
            [EMAIL_HOST_USER],
            fail_silently=False,
        )
            return redirect('/')
    return render(request, 'contact.html', {'contact_form': ContactForm})


send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    [EMAIL_HOST_USER],
    fail_silently=False,
)
