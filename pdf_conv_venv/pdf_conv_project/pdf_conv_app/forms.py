from django import forms
from pdf_conv_app.utils.pdf_convert import CONVERT_MODE

class ConvertSelectForm(forms.Form):
    convert_option = tuple(
        [(key, CONVERT_MODE[key]['description']) for key in CONVERT_MODE.keys()]
    )
    conversion_mode = forms.ChoiceField(
        required=True, 
        choices=convert_option, 
        label='Select conversion format:', 
        # widget=forms.Select(attrs={ 'class': 'home-select-field' })
    )

class GetFileToConvert(forms.Form):
    target_file = forms.FileField(label='Choose file')

class GetMultiFilesToConvert(forms.Form):
    target_files = forms.FileField(
        label='Choose files',
        widget=forms.ClearableFileInput(attrs={ 'multiple': True })
    )