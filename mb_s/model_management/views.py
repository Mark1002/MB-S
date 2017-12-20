from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from model_management.services import ModelManagementServices

class ShowModelView(View):
    def get(self, request):
        model_list = ModelManagementServices.get_all_model()
        context = {"model_list": model_list}
        return render(request, 'model_management/model_list.html', context)

class DeleteModelView(View):
    def post(self, request):
        ModelManagementServices.delete_model_byId(request.POST['model_id'])
        return HttpResponseRedirect(reverse('model_management:show_model'))
