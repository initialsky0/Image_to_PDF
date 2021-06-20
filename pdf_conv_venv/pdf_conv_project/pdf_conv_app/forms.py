from django import forms

class ConvertSelectForm(forms.Form):
    convert_option = (
        ('test1', 'Test1'), 
        ('test2', 'Test2'), 
        ('test3', 'Test3'),
    )
    conversion_mode = forms.ChoiceField(
        required=True, 
        choices=convert_option, 
        label='Select the conversion:', 
        widget=forms.Select(attrs={ 'class': 'home-select-field' })
    )