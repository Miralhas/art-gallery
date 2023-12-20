from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView

from accounts.forms import AuthForm, RegisterForm
from accounts.models import User

# Create your views here.


class UserLoginView(LoginView):
    form_class = AuthForm
    template_name = "accounts/login.html"

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return reverse(self.next_page)
        else:
            return reverse("gallery:index")


class UserProfileView(View):
    model = User
    template_name = "accounts/profile.html"
    
    def get(self, request, username):
        try:
            username = User.objects.get(username=username)
        except User.DoesNotExist:
            username = None

        page_obj = {}
        if username is not None:
            User.objects.filter(pk=username.pk).update(views=F("views") + 1)
            galleries = username.galleries.all().order_by("-views")
            paginator = Paginator(galleries, 3)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, context={
            "user_profile":username,
            "page_obj": page_obj,
        })



class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.GET.get("path", "/"))


class UserSignUpView(View):
    form_class = RegisterForm
    template_name = "accounts/signup.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            profile_picture = request.FILES.get("profile_picture")
            if profile_picture:
                new_user.profile_picture = profile_picture
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse("gallery:index"))
        else:
            while (len(form.errors)) != 1:
                form.errors.popitem()
            return render(request, self.template_name, context={"form": form})