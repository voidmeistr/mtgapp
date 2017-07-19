from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .forms import UserForm
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'magic/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'magic/detail.html'

# registration page / registration itself


class UserFormView(View):
    form_class = UserForm
    template_name = 'magic/registration_form.html'

    # blank
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # data to process
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # normalization of data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns USer object if everything is ok
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:

                    login(request, user)
                    return redirect('magic:index')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_posts = Post.objects.all()
                return render(request, 'magic/index.html', {'all_posts': all_posts})
            else:
                return render(request, 'magic/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'magic/login.html', {'error_message': 'Invalid login'})
    return render(request, 'magic/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'magic/login.html', context)