from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError

from django.core.files.storage import FileSystemStorage
from .DrinksApi import drinksdetection


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def index(request):
    message = ""
    prediction = ""
    # fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("image : ", image)


        # _image = fss.save(image.name, image)
        # print('_image : ', _image)
        # image_url = fss.url(_image)
        # print('image_url : ', image_url)


        path = str(settings.MEDIA_ROOT)+'/images' + "/" + image.name
        # image details

        print('path : ', path)
        # Read the image
        products, total_product_count = drinksdetection(path)
        print('total_product_count : ', total_product_count)
        print('products : ', products)
        # image_url = fss.url(_image)
        path_save = f'media/results/{image.name}'
        return TemplateResponse(
            request,
            "index.html",
            {
                "message": message,
                "total_product_count": total_product_count,
                "image_url": path_save,
                "prediction": products,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {"message": "No Image Selected"},
        )

