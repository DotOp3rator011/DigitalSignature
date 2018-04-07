from django.contrib.auth import authenticate
from signature.models import UserProfile, Signature
from django.contrib.auth.models import User
from datetime import datetime
from hashlib import md5


# identify
def get_identity(request):
    hashText = request.POST.get('hash')
    try:
        signature = Signature.objects.get(hash=hashText)
    except:
        return {"error": "Signature not found. Please check the value entered"}
    user = User.objects.get(email=signature.email)
    identity = {"First Name": user.first_name,
                "Last Name": user.last_name,
                "Email": user.email,
                "Phone": user.userprofile.phone,
                "Aadhaar": user.userprofile.aadhaar,
                "Addressed to": signature.addressedTo,
                "Subject": signature.subject,
                "Signature": signature.hash}
    return identity


# dashboard
def get_user_signatures(request):
    userSignatures = Signature.objects.filter(email=request.user.email)
    return userSignatures


# signature
def get_hash_text(details):
    text = str(datetime.now())
    for key in details.keys():
        text += details[key]
    hashText = md5(text.encode()).hexdigest()
    return hashText


def get_details(request):
    user = User.objects.get(email=request.user.email)
    details = {"firstName": user.first_name,
               "lastName": user.last_name,
               "email": user.email,
               "phone": user.userprofile.phone,
               "aadhaar": user.userprofile.aadhaar,
               "subject": request.POST.get('subject'),
               "addressedTo": request.POST.get('addressedTo')}
    return details


# register
def create_profile(form):
    user = User.objects.get(username=form.cleaned_data['username'])
    up = UserProfile(user=user,
                     phone=form.cleaned_data['phone'],
                     aadhaar=form.cleaned_data['aadhaar'])
    up.save()


def authentication(form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password1']
    user = authenticate(username=username, password=password)
    return user
