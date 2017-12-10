import os
from django.test import TestCase
from django.test import Client
from io import BytesIO
from mbs_db.models import ImageFile
from PIL import Image

def create_image(image_name):
    size = (150, 150)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    data = BytesIO()
    image.save(data, 'jpeg')
    data.seek(0)
    data.name = image_name
    return data

class ImageManagementTestCase(TestCase):
    def test_upload_image(self):
        image_name = 'unittest.jpg'
        test_image = create_image(image_name)
        client = Client()
        client.post('/upload-images/', {'image': test_image})
        self.assertEqual(ImageFile.objects.count(), 1)
        os.remove("images/" + image_name)
