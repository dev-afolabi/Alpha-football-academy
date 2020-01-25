from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {'form': form, 'submitted': submitted})


    