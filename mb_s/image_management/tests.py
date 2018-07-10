import os
from django.test import TestCase
from io import BytesIO
from mbs_db.models import ImageFile
from PIL import Image

class ImageManagementTestCase(TestCase):
    def create_image(self, image_name):
        size = (150, 150)
        color = (255, 0, 0, 0)
        image = Image.new("RGB", size, color)
        data = BytesIO()
        image.save(data, 'jpeg')
        data.seek(0)
        data.name = image_name
        return data

    def test_upload_image(self):
        image_name = 'unittest.jpg'
        test_image = self.create_image(image_name)
        self.client.post('/upload-images/', {'image': test_image})
        self.assertEqual(ImageFile.objects.count(), 1)
        os.remove("images/" + image_name)
