from django.test import TestCase
from . models import Image,Profile
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.photo = Image(name='image',caption='cool image',comment='cool comment') 

    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Image))

    # # save
    def test_save_method(self):
        self.photo.save_photo()
        photos = Image.objects.all()
        self.assertTrue(len(photos)>0)

        