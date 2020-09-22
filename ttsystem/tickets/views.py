from django.shortcuts import get_object_or_404
from django.views import generic 
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView

from .forms import TicketForm
from .models import Ticket

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tickets/index.html'
    context_object_name = 'latest_ticket_list'

    def get_queryset(self):
        """Return the last five published Tickets."""
        return Ticket.objects.order_by('-created_at')[:5]

class FormViews():
    model = Ticket
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:index')

class TicketCreate(FormViews, CreateView):
    template_name = 'tickets/ticket_create_form.html'
    model = Ticket
    form_class = TicketForm

class TicketUpdate(FormViews, UpdateView):
    model = Ticket 
    form_class = TicketForm
    template_name_suffix = '_update_form'

        
## create comment action


## create attachment action



# def ticket_edit_view(request, ticket_id):
#     ticket = get_object_or_404(Ticket, pk=ticket_id)
#     data = {
#         'ticketType': ticket.ticketType,
#         'subject': ticket.subject,
#         'project': ticket.project,
#         'description': ticket.description,
#         'priority': ticket.priority,
#         'owner': ticket.owner,
#         'status': ticket.status,
#         # 'creation_date': ticket.created_at,
#         # 'creator': ticket.creator,
#     }
#     form = TicketForm(data)
#     return render(request, 'tickets/detail.html', {'form': form, 'ticket':ticket})
    # return render(request, 'tickets/detail.html', {'ticket': ticket})             #this can be used for users with only read permissions

# def ticket_create_view(request):
#     form = TicketForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = TicketForm()

#     user = get_object_or_404(User, pk=1)
#     return render(request, 'tickets/ticket_create.html', {'form': form, 'user': user})

