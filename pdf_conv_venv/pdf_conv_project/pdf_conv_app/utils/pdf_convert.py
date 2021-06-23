from pathlib import Path
from PIL import Image
from random import randint

def convImgToPdf(img_list, save_path):
    # covert the image to a single pdf file
    convert_list = []
    first_img = Image.open(img_list[0])
    first_conv = first_img.convert('RGB')
    for img_path in img_list[1:]:
        img = Image.open(img_path)
        img_conv = img.convert('RGB')
        convert_list.append(img_conv)
    filename = 'converted{}.pdf'.format(randint(1, 1000))
    first_conv.save(save_path / filename, save_all=True, append_images=convert_list)
    return filename