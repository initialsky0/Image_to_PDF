from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from pdf_conv_app import forms

from os import remove as clean_file
from threading import Timer
from pathlib import Path
from pdf_conv_app.utils import pdf_convert, util_response

# Create your views here.
def index(request):
    form = forms.ConvertSelectForm
    if request.method == 'POST' and form(request.POST).is_valid:
        # redirecting
        return redirect(reverse(
            'convert', 
            kwargs={
                'mode': request.POST['conversion_mode']
            }
        ))
    return render(request, 'index.html', context={'form': form})

def convert(request, mode):
    print(mode)
    single_file = False
    # the boolean here is placeholder, will be replaced with a funtion to 
    # check for single or multi file form based on the mode
    if single_file:
        # this is when mode require one file
        form = forms.GetFileToConvert
    else:
        # else form is multi-files
        form = forms.GetMultiFilesToConvert

    # handle file conversion on post request
    if request.method == 'POST':
        post_form = form(request.POST, request.FILES)
        if post_form.is_valid():
            if(single_file):
                #  one file
                upload_content = request.FILES['target_file']
                # upload_content.temporary_file_path()
                file = pdf_convert.convImgToPdf([upload_content], settings.MEDIA_DIR)
            else:
                # else form is multi-files
                upload_content = request.FILES.getlist('target_files')
                file = pdf_convert.convImgToPdf(upload_content, settings.MEDIA_DIR)
                # Clean the file after 1 minute
                Timer(60, lambda : clean_file(settings.MEDIA_DIR / file)).start()
        return redirect('download', file_name=file)
                
    
    return render(request, 'convert.html', 
        context={
            'form': form, 
            'single_file': single_file
        }
    )

def download(request, file_name):
    path = settings.MEDIA_DIR / file_name
    file_exist = Path.exists(path)
    if(request.GET.get('download') == 'True'):
        # return download response
        return util_response.get_file_dl_res(path, file_name)
    return render(
        request, 
        'download.html', 
        context={ 
            'file_name': file_name, 
            'file_exist': file_exist 
        }
    )

