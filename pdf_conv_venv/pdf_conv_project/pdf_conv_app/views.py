from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from django.http import Http404
from pdf_conv_app import forms

from os import remove as clean_file
from threading import Timer
from pathlib import Path
from pdf_conv_app.utils import util_response
from pdf_conv_app.utils.pdf_convert import CONVERT_MODE

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
    convert_mode = CONVERT_MODE[mode]
    single_file = not convert_mode['multi_input']

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
                # upload_content.temporary_file_path()
                # one file
                upload_content = request.FILES['target_file']
                file = convert_mode['convert_func']([upload_content], settings.MEDIA_DIR)
            else:
                # else form is multi-files
                upload_content = request.FILES.getlist('target_files')
                file = convert_mode['convert_func'](upload_content, settings.MEDIA_DIR)
            
            # Clean the file after 1 minute
            Timer(60, lambda : clean_file(settings.MEDIA_DIR / file)).start()
        return redirect('download', file_name=file)
                
    
    return render(request, 'convert.html', context={ 'form': form })

def download(request, file_name):
    path = settings.MEDIA_DIR / file_name
    if(not Path.exists(path)):
        # file not found, raise 404 error
        raise Http404('file')
    elif(request.GET.get('download') == 'true'):
        # return download response
        return util_response.get_file_dl_res(path, file_name)

    return render(
        request, 
        'download.html', 
        context={ 
            'file_name': file_name, 
            'file_exist': 'true' 
        }
    )

def handler404(request, exception):
    not_found_type = exception if isinstance(exception.args[0], str) else 'page'
    response = render(request, '404.html', context={ 'not_found_type': not_found_type })
    response.status_code = 404
    return response