import logging
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from mbs_db.models import ImageFile
from utils.image_utils import ImageUtils
from image_class_management.services import ImageClassManagementServices
from challenge_management.services import ChallengeManagementServices

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
image_dir = "images"


class ShowImageClassView(View):
    def get(self, request, challenge_id):
        imageclass_list = ImageClassManagementServices.select_image_class(challenge_id)
        challenge = ChallengeManagementServices.select_challenge_byId(challenge_id)
        context = {'imageclass_list': imageclass_list, 'challenge': challenge}
        return render(request, 'image_class_management/show_image_class.html', context)


class AddImageClassView(View):
    def get(self, request, challenge_id):
        return render(request, 'image_class_management/add_image_class.html', {'challenge_id': challenge_id})

    def post(self, request, challenge_id):
        image_class_name = request.POST['image_class_name']
        ImageClassManagementServices.add_image_class(challenge_id, image_class_name)
        return HttpResponseRedirect(reverse('image_class_management:show_image_class', args=[challenge_id]))
