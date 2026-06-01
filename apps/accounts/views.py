from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import seller_required

from .forms import RegisterForm

def register_view(request):
   if request.method == 'POST':

      form = RegisterForm(request.POST)

      if form.is_valid():
         form.save()

         messages.success(
            request, 'Account created successfully. Please log in.'
         )

         return redirect('login')
   
      else:
         form = RegisterForm()

      return render(
         request,
         'accounts/register.html',
         {
            'form': form
         }
      )


def login_view(request):
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = authenticate(
         request, 
         email=email,
         password=password
      )

      if user is not None:
         login(request, user)
         messages.success(request, 'Login successful.')
         return redirect('profile')
      else:
         messages.error(request, 'Invalid email or password.')

   return render(request, 'accounts/login.html')


def logout_view(request):
   logout(request)
   messages.success(request, 'Logged out successfully.')
   return redirect('login')


@login_required
def profile_view(request):
   return render(request, 'accounts/profile.html')


@login_required
@seller_required
def seller_dashboard(request):
   return render(
      request,
      'accounts/seller_dashboard.html'
   )