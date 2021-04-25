from django.shortcuts import render
from django.views import View
from core.models import GhostName
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

def home(request):
    """
    Simple view that provides all ghosts in random order in the context
    """
    context = {
        'ghost_names' : GhostName.objects.order_by('?').all()
    }
    return render(request, 'home.html', context)


class PickName(View):

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        context = {
            'names_options' : GhostName.objects.filter(
                user__isnull=True).order_by('?')[:3]
        }
        return render(request, 'name-picker.html', context)

    @method_decorator(login_required(login_url='/'))
    def post(self, request):
        ghost_id = request.POST.get('picked_ghost')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        selected_ghost = GhostName.objects.filter(pk=ghost_id).first()

        if selected_ghost and not selected_ghost.user:

            # If user already had a name assigned remove it
            prev_user_name = GhostName.objects.filter(user=request.user).first()
            if prev_user_name:
                prev_user_name.user = None
                prev_user_name.first_name = None
                prev_user_name.last_name = None
                prev_user_name.save()

            # Set user details to ghost instance
            selected_ghost.user = request.user
            selected_ghost.first_name = first_name
            selected_ghost.last_name = last_name
            selected_ghost.save()

            return redirect(home)
