from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def create_user(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "User created successfully")

    return render(
        request=request,
        template_name="login_signup.html",
        context={"signup_form": SignUpForm},
    )
