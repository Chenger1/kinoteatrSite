from django.shortcuts import render
from django.views.generic import View


class IndexAdmin(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)
