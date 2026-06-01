
from django.shortcuts import redirect
from django.contrib import messages 

def seller_required(view_func):
   def wrapper(request, *args, **kwargs):
      if request.user.role != 'seller':
         messages.error(
            request,
            'Seller access only. so seller access required this page.'
         )
         return redirect('profile')
      return view_func(
         request,
         *args,
         **kwargs
      )
   return wrapper


