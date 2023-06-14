from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/welcome.html'

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

#used to create a login site for users that's not admin
class LoginInterfaceView(LoginView):
    #template name as variable 
    template_name = 'home/login.html'

#used to create a logout view
class LogoutInterfaceView(LogoutView):
    #template name
    template_name = 'home/logout.html'

#signup view 
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


#def home(request):
    #return render(request, 'home/welcome.html', {})

#@login_required
#def authorized(request):
    #return render(request, 'home/authorized.html', {})

