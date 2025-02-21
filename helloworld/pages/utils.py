from django.core.files.storage import default_storage 
from django.http import HttpRequest 
from .interfaces import ImageStorage  
class ImageLocalStorage(ImageStorage): 
    def store(self, request: HttpRequest): 
        profile_image = request.FILES.get('profile_image', None) 
        if profile_image: 
            # Store the image 
            file_name = default_storage.save('uploaded_images/' + profile_image.name, profile_image) 
            return default_storage.url(file_name)