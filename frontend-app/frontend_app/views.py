from django.shortcuts import render
from datetime import datetime
import socket

def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    
    hostname = socket.gethostname()
    try:
        server_ip = socket.gethostbyname(hostname)
    except:
        server_ip = '127.0.0.1'
    
    context = {
        'title': 'Головна сторінка Frontend',
        'server': 'Frontend Pool VMSS',
        'timestamp': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
        'version': '1.0.0',
        'client_ip': client_ip,
        'server_ip': server_ip,
        'hostname': hostname,
        'gateway_ip': 'Запит через Application Gateway'
    }
    return render(request, 'frontend_app/index.html', context)