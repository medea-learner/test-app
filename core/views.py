from django.shortcuts import render, redirect
from django.contrib.auth import logout

from task_manager.models import Task

from .forms import SignupForm
from .models import Role

def anonymous_user(func):
    def wrap(request):
        if request.user.is_authenticated:
            return redirect("core:index")
        return func(request)
    return wrap


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        user_is_manager = request.user.roles.filter(name="manager").first()
    else:
        tasks = []
        user_is_manager = None

    return render(request, 'core/index.html', {
        'tasks': tasks,
        'user_is_manager': user_is_manager
    })

@anonymous_user
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            for role_pk in form.data.getlist("roles"):
                user.roles.add(Role.objects.get(pk=role_pk))
            user.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def log_out(request):
    logout(request)
    return redirect('/login/')