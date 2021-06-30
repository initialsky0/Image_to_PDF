from pdf_conv_app.utils.pdf_convert import CONVERT_MODE

def access_nav_category(request):
    '''
        Context processor for nav category for template base block
    '''
    pdf_info = { key: CONVERT_MODE[key]['description'] for key in CONVERT_MODE }
    return {
        'nav_categories': {    
            'pdf': pdf_info, 
            'placeholder': { 'key': 'new category mode' }
        }
    }