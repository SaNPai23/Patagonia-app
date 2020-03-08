from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .models import Physician, Patient
from .forms import PhysicianSignupForm, PhysicianLoginForm


def index(request):
    if request.method == 'GET':
        context = ''
        form = PhysicianLoginForm()
        return render(request, 'index.html', {'form': form})

    elif request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        details = PhysicianLoginForm(request.POST)

        if details.is_valid():
            username = details.cleaned_data['email_id']
            password = details.cleaned_data['password']
            post = Physician.objects.filter(email_id=username, password=password)
        else:
            post = None

        if post:
            # username = request.POST['username']
            request.session['username'] = username
            return redirect("login")
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Username or Password.')
            return render(request, "index.html", {'form': details})
    return render(request, 'index.html', {})


def login(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = Physician.objects.filter(email_id=posts)
        return render(request, 'login.html', {"query": query})
    else:
        return render(request, 'index.html', {})


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect("index")


def signup(request):
    # p = Physician(email_id=username, password=password, first_name="Test", last_name="name")
    # p.save()
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = PhysicianSignupForm(request.POST)

        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid():

            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database
            post = details.save(commit=False)

            # Finally write the changes into database
            post.save()

            # redirect it to some another page indicating data
            # was inserted successfully
            username = details.cleaned_data['email_id']
            request.session['username'] = username
            return redirect("login")

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "signup.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = PhysicianSignupForm()
        return render(request, 'signup.html', {'form': form})
