from pathlib import Path
from PIL import Image
from random import randint
from .progress_bar import ProgressBar

def convImgToPdf(img_list, save_path):
    '''
        covert the image to a single pdf file, takes list of image files and path to save result. 
        Return dict of file path and name if success and return error message if there is any exception
    '''
    convert_list = []
    try:
        first_img = Image.open(img_list[0])
        first_conv = first_img.convert('RGB')
        
        # starting progress bar here
        prog_bar = ProgressBar(len(img_list), 'Converting')
        prog_bar.next_step(0)

        for index, img_path in enumerate(img_list[1:]):
            img = Image.open(img_path)
            img_conv = img.convert('RGB')
            convert_list.append(img_conv)
            # index for progress bar is 1 than actual index bc it's not the first page
            prog_bar.next_step(index + 1)
        filename = 'converted{}.pdf'.format(randint(1, 1000))
        final_path = save_path / filename
        first_conv.save(final_path, save_all=True, append_images=convert_list)
        return { 'path': final_path, 'name': filename }
    except Exception as error: 
        print('\n{}'.format(error))
        return { 'error': 'Error occurred during conversion. Check if the file you uploaded is in proper image format.' }

CONVERT_MODE = {
    'img_to_pdf': {
        'description': 'one or more images to PDF', 
        'instruction': 'Please select one or more image files to convert to a PDF file. Page number is order by file name.',
        'multi_input': True, 
        'convert_func': convImgToPdf
    }, 
    'placeholder1': {
        'description': 'placeholder1', 
        'multi_input': False, 
        'convert_func': lambda a, b : {}
    }, 
    'placeholder2': {
        'description': 'placeholder2', 
        'multi_input': False, 
        'convert_func': lambda a, b : {}
    },
}