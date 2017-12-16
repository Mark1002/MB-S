import os
from django.db import models
from django.urls import reverse

class ImageFile(models.Model):
    model_pic = models.ImageField(upload_to='images/')

    def get_img_url(self):
        image_name = os.path.basename(str(self.model_pic))
        return reverse('image_management:images_url', args=[image_name])

class Challenge(models.Model):
    name = models.CharField(max_length=30)

    def get_delete_url(self):
        return reverse('challenge_management:delete_challenge', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('challenge_management:edit_challenge', args=[str(self.id)])

    def get_image_class_url(self):
        return reverse('image_class_management:show_image_class', args=[str(self.id)])

    def __str__(self):
        return self.name

class ImageClass(models.Model):
    name = models.CharField(max_length=30)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('image_class_management:delete_image_class', args=[str(self.challenge_id), str(self.id)])

    def get_edit_url(self):
        return reverse('image_class_management:edit_image_class', args=[str(self.challenge_id), str(self.id)])

    def __str__(self):
        return self.name

class ModelInfo(models.Model):
    name = models.CharField(max_length=30)
    train_challenge = models.CharField(max_length=30)
    model_path = models.CharField(max_length=100)
    label_dict = models.CharField(max_length=200)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('model_management:delete_model', args=[str(self.id)])
