from django.views.generic.list import ListView

from cinema.models.user import User


class ListUser(ListView):
    model = User
    template_name = 'user/list_user.html'
    paginate_by = 10
    context_object_name = 'users'
