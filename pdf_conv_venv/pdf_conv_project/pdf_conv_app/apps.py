from django.apps import AppConfig
from django.conf import settings

from pdf_conv_app.utils.util_files import clean_all_files

class PdfConvAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdf_conv_app'

    def ready(self) -> None:
        # Clean all files in media when server start
        clean_all_files(settings.MEDIA_DIR)
        return super().ready()
