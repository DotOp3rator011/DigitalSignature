from django.shortcuts import render, redirect
from django.contrib.auth import login
from signature.forms import RegisterForm, SignatureForm
from backend import *


def index(request):
    return render(request, 'signature/index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            create_profile(form)
            user = authentication(form)
            login(request, user)
            return redirect('signature:index')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def dashboard(request):
    userSignatures = get_user_signatures(request)
    context = {"userSignatures": userSignatures}
    return render(request, 'signature/dashboard.html', context)


def signature(request):
    context = dict()
    if request.method == "POST":
        form = SignatureForm(request.POST)
        if form.is_valid():
            details = get_details(request)
            hashText = get_hash_text(details)
            form.save(details, hashText)
            context = {'form': form, 'hashText': hashText}
    else:
        form = SignatureForm()
        context = {'form': form}
    return render(request, 'signature/signature.html', context)


def identify(request):
    return render(request, 'signature/identify.html')
