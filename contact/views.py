from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact-us.html', {'form': ContactForm(), 'results': 'success'})
        else:
            return render(request, 'contact-us.html', {'form': form, 'results': 'fail'})
    else:
        form = ContactForm()
    
    return render(request, 'contact-us.html', {'form': form})

def about(request):
   return render(request,'about-us.html')

def ourservices(request):
    return render (request,'our-services.html')
