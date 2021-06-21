from django.shortcuts import redirect, render
from django.urls import reverse
from pdf_conv_app import forms

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'conversion_mode' in request.POST:
            print(request.POST['conversion_mode'])
            # redirecting
            return redirect('/{}'.format(request.POST['conversion_mode']))
    return render(request, 'index.html', context={'form': forms.ConvertSelectForm})