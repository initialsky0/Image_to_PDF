from django import forms

class ConvertSelectForm(forms.Form):
    convert_option = (
        ('test1', 'Test1'), 
        ('test2', 'Test2'), 
        ('test3', 'Test3'), 
        ('test4', 'Test4'), 
        ('test5', 'Test5'),
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