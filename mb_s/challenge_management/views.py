import logging
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from challenge_management.services import ChallengeManagementServices

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class ShowChallengeView(View):
    def get(self, request):
        challenge_list = ChallengeManagementServices.select_all_challenge()
        log.debug(challenge_list)
        context = {'challenge_list': challenge_list}
        return render(request, 'challenge_management/show_challenge.html', context)


class AddChallengeView(View):
    def get(self, request):
        return render(request, 'challenge_management/add_challenge.html')

    def post(self, request):
        try:
            challenge_name = request.POST['challenge_name']
            ChallengeManagementServices.add_challenge(challenge_name)
            return HttpResponseRedirect(reverse('challenge_management:show_challenge'))
        except Exception as e:
            return render(request, 'challenge_management/add_challenge.html', {'error_message': str(e)})

class DeleteChallengeView(View):
    def post(self, request, challenge_id):
        ChallengeManagementServices.delete_challenge(challenge_id)
        return HttpResponseRedirect(reverse('challenge_management:show_challenge'))
