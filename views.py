# smartscoreApp/views.py
from django.shortcuts import render
from .forms import UserAuthenticationForm

def index(request):
    # Your existing view logic
    return render(request, 'smartscoreApp/index.html')

def home(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Implement authentication logic as needed
    else:
        form = UserAuthenticationForm()

    return render(request, 'smartscoreApp/register.html', {'form': form})
