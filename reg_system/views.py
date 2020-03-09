from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .models import Physician, Patient
from .forms import PhysicianSignupForm, PhysicianLoginForm, PatientSignupForm


def index(request):
    if request.session.has_key('username'):
        messages.add_message(request, messages.ERROR, 'You are already logged in.')
        return redirect('login')
    else:
        if request.method == 'GET':
            form = PhysicianLoginForm()
            return render(request, 'index.html', {'form': form, 'logout': False})

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
        physician = Physician.objects.get(email_id=posts)
        patients = Patient.objects.filter(physician_id=physician.id)
        return render(request, 'login.html', {"patients": patients, "physician": physician, 'logout': True})
    else:
        messages.add_message(request, messages.ERROR, 'You have to log in first.')
        return redirect('index')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect("index")


def signup(request):
    if request.session.has_key('username'):
        messages.add_message(request, messages.ERROR, 'You are already logged in.')
        return redirect('login')

    else:
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
                return render(request, "signup.html", {'form': details, 'logout': False})
        else:

            # If the request is a GET request then,
            # create an empty form object and
            # render it into the page
            form = PhysicianSignupForm()
            return render(request, 'signup.html', {'form': form, 'logout': False})


def edit(request):
    if not request.session.has_key('username'):
        messages.add_message(request, messages.ERROR, 'You have to log in first.')
        return redirect('login')
    else:
        if request.method == 'GET':
            patient_id = request.GET.get('id')
            patient = Patient.objects.get(pk=patient_id)
            form = PatientSignupForm(instance=patient)
            return render(request, 'edit.html', {'form': form, 'logout': True, 'patient_id': patient_id})

        elif request.method == 'POST':

            # Pass the form data to the form class
            patientid = request.POST.get('patient_id')
            patient = Patient.objects.get(id=patientid)
            details = PatientSignupForm(request.POST, instance=patient)

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

                return redirect("login")
            else:

                # Redirect back to the same page if the data
                # was invalid
                return render(request, "edit.html", {'form': details, 'logout': True})


def delete(request):
    if not request.session.has_key('username'):
        messages.add_message(request, messages.ERROR, 'You have to log in first.')
        return redirect('index')
    else:
        patient_id = request.GET.get('id')
        instance = Patient.objects.get(id=patient_id)
        instance.delete()
        return redirect('login')


def addpatient(request):

    if not request.session.has_key('username'):
        messages.add_message(request, messages.ERROR, 'You have to log in first.')
        return redirect('index')

    else:
        # check if the request is post
        if request.method == 'POST':

            # Pass the form data to the form class
            details = PatientSignupForm(request.POST)

            # In the 'form' class the clean function
            # is defined, if all the data is correct
            # as per the clean function, it returns true
            if details.is_valid():

                # Temporarily make an object to be add some
                # logic into the data if there is such a need
                # before writing to the database
                post = details.save(commit=False)
                physician = Physician.objects.get(email_id=request.session['username'])
                post.physician_id_id = physician.id
                # Finally write the changes into database
                post.save()

                # redirect it to some another page indicating data
                # was inserted successfully

                return redirect("login")

            else:

                # Redirect back to the same page if the data
                # was invalid
                return render(request, "addpatient.html", {'form': details, 'logout': True})
        else:

            # If the request is a GET request then,
            # create an empty form object and
            # render it into the page
            form = PatientSignupForm()
            return render(request, 'addpatient.html', {'form': form, 'logout': True})
