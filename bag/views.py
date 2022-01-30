from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the user bag content"""

    return render(request, 'bag/bag.html')
