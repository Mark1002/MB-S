import os
from django.db import models
from django.urls import reverse

class ImageFile(models.Model):
    model_pic = models.ImageField(upload_to='images/')

    def get_img_url(self):
        image_name = os.path.basename(str(self.model_pic))
        return reverse('image_management:images_url', args=[image_name])
