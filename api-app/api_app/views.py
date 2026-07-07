from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import datetime
import socket
import json

@csrf_exempt
def api_root(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    try:
        server_ip = socket.gethostbyname(socket.gethostname())
    except:
        server_ip = '127.0.0.1'
    
    return JsonResponse({
        'status': 'success',
        'message': 'API Server is running',
        'server': 'API Pool VMSS',
        'version': '1.0.0',
        'timestamp': datetime.datetime.now().isoformat(),
        'client_ip': client_ip,
        'server_ip': server_ip,
        'hostname': socket.gethostname(),
        'gateway': 'Accessed via Application Gateway' if x_forwarded_for else 'Direct access',
        'endpoints': {
            '/api/': 'API root information',
            '/api/health': 'Health check endpoint',
            '/api/users': 'Get list of users',
            '/api/products': 'Get list of products'
        },
        'documentation': 'https://github.com/your-repo/api-docs'
    }, status=200, json_dumps_params={'indent': 2, 'ensure_ascii': False})

def health_check(request):
    try:
        server_ip = socket.gethostbyname(socket.gethostname())
    except:
        server_ip = '127.0.0.1'
    
    return JsonResponse({
        'status': 'healthy',
        'service': 'API Service',
        'timestamp': datetime.datetime.now().isoformat(),
        'uptime': 'Running',
        'server': 'API Pool - Health Check',
        'server_ip': server_ip,
        'hostname': socket.gethostname(),
        'database': 'connected',
        'memory': 'ok',
        'disk': 'ok'
    }, status=200, json_dumps_params={'indent': 2, 'ensure_ascii': False})

@require_http_methods(["GET"])
def get_users(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    
    users = [
        {
            'id': 1,
            'name': 'Іван Петренко',
            'email': 'ivan.petrenko@example.com',
            'role': 'admin',
            'active': True,
            'created_at': '2024-01-15T10:30:00'
        },
        {
            'id': 2,
            'name': 'Марія Шевченко',
            'email': 'maria.shevchenko@example.com',
            'role': 'user',
            'active': True,
            'created_at': '2024-02-20T14:45:00'
        },
        {
            'id': 3,
            'name': 'Петро Сидоренко',
            'email': 'petro.sydorenko@example.com',
            'role': 'user',
            'active': False,
            'created_at': '2024-03-10T09:15:00'
        },
        {
            'id': 4,
            'name': 'Олена Коваленко',
            'email': 'olena.kovalenko@example.com',
            'role': 'moderator',
            'active': True,
            'created_at': '2024-04-05T16:20:00'
        },
        {
            'id': 5,
            'name': 'Андрій Бондаренко',
            'email': 'andriy.bondarenko@example.com',
            'role': 'user',
            'active': True,
            'created_at': '2024-05-12T11:00:00'
        }
    ]
    
    return JsonResponse({
        'status': 'success',
        'data': {
            'users': users,
            'total': len(users),
            'active': sum(1 for u in users if u['active'])
        },
        'timestamp': datetime.datetime.now().isoformat(),
        'server': 'API Pool - Users Endpoint',
        'client_ip': client_ip,
        'server_ip': socket.gethostbyname(socket.gethostname())
    }, status=200, json_dumps_params={'indent': 2, 'ensure_ascii': False})

@require_http_methods(["GET"])
def get_products(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    
    products = [
        {
            'id': 1,
            'name': 'Ноутбук Dell XPS 13',
            'category': 'Електроніка',
            'price': 34999.99,
            'currency': 'UAH',
            'in_stock': True,
            'rating': 4.8
        },
        {
            'id': 2,
            'name': 'Смартфон iPhone 15 Pro',
            'category': 'Електроніка',
            'price': 42999.00,
            'currency': 'UAH',
            'in_stock': True,
            'rating': 4.9
        },
        {
            'id': 3,
            'name': 'Навушники Sony WH-1000XM5',
            'category': 'Аудіо',
            'price': 11999.00,
            'currency': 'UAH',
            'in_stock': True,
            'rating': 4.7
        },
        {
            'id': 4,
            'name': 'Монітор LG UltraFine 5K',
            'category': 'Периферія',
            'price': 24999.00,
            'currency': 'UAH',
            'in_stock': False,
            'rating': 4.6
        },
        {
            'id': 5,
            'name': 'Клавіатура Logitech MX Keys',
            'category': 'Периферія',
            'price': 3999.00,
            'currency': 'UAH',
            'in_stock': True,
            'rating': 4.5
        }
    ]
    
    return JsonResponse({
        'status': 'success',
        'data': {
            'products': products,
            'total': len(products),
            'in_stock': sum(1 for p in products if p['in_stock']),
            'categories': list(set(p['category'] for p in products))
        },
        'timestamp': datetime.datetime.now().isoformat(),
        'server': 'API Pool - Products Endpoint',
        'client_ip': client_ip,
        'server_ip': socket.gethostbyname(socket.gethostname())
    }, status=200, json_dumps_params={'indent': 2, 'ensure_ascii': False})