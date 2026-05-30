from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


User = get_user_model()

def register_view(request):
   if request.method == 'POST':

      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')

      if User.objects.filter(email=email).exists():
         messages.error(request, 'Email already exists.')
         return redirect('register')
      
      user = User.objects.create_user(
         username=username,
         email=email,
         password=password
      )
      messages.success(request, 'Account created successfully. Please log in.')
      return redirect('login')
   
   return render(request, 'accounts/register.html')


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
