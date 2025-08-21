from django.shortcuts import render
from .forms import registrationform

# Create your views here.
def register(request):
    if request.method == 'POST':
        
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = registrationform()
    context = {
        'form':form
    }
    return render(request,'register.html',context)