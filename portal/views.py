from django.shortcuts import render
from .models import Cliente, Ticket

def index(request):
    clientes = Cliente.objects.all()
    tickets = Ticket.objects.all()
    return render(request, 'portal/index.html', {'clientes': clientes, 'tickets': tickets})
