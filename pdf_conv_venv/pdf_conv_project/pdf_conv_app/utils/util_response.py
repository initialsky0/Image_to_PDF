from django.http import HttpResponse
import mimetypes

def get_file_dl_res(file_path, file_name):
    with open(file_path, 'rb') as file_handler:
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(file_handler.read(), content_type=mime_type)
        # Set HTTP header
        response['Content-Disposition'] = "attachment; filename={}".format(file_name)
        return response