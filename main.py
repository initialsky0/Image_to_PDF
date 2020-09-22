import sys
from pathlib import Path
from PIL import Image


def get_drop_file():
    # return a list for files inside a directory drop onto the bat file
    f_handler = Path(sys.argv[1]).glob('**/*')
    files_list = [file for file in f_handler if file.is_file()]
    return files_list


def convert_to_pdf(img_list, save_path):
    # covert the image to a single pdf file
    convert_list = []
    first_img = Image.open(img_list[0])
    first_conv = first_img.convert('RGB')
    for img_path in img_list[1:]:
        img = Image.open(img_path)
        img_conv = img.convert('RGB')
        convert_list.append(img_conv)
    first_conv.save(save_path, save_all=True, append_images=convert_list)
    return 0


def main():
    img_list = get_drop_file()
    pdf_path = Path.cwd().joinpath(input('Enter the name of your pdf: ') + '.pdf')
    convert_to_pdf(img_list, pdf_path)
    return 0


if __name__ == "__main__":
    main()
