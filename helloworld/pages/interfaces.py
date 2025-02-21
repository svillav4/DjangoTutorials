from abc import ABC, abstractmethod 
from django.http import HttpRequest

class ImageStorage(ABC): 
    @abstractmethod 
    def store(self, request: HttpRequest): 
        pass