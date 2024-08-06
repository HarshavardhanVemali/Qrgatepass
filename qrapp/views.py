from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import FailedLoginAttempts, Register
from django.contrib.auth import authenticate, login
import uuid
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

MAX_FAILED_ATTEMPTS = 3

def set_device_cookie(response, device_id):
    response.set_cookie('device_id', device_id, max_age=365 * 24 * 60 * 60)

def get_device_id(request):
    return request.COOKIES.get('device_id', str(uuid.uuid4()))

def is_device_blocked(device_id):
    try:
        failed_attempt = FailedLoginAttempts.objects.get(device_id=device_id)
        if failed_attempt.is_active:
            return True
    except FailedLoginAttempts.DoesNotExist:
        return False
    return False

def adminlogin(request):
    if request.method == 'POST':
        device_id = get_device_id(request)
        if is_device_blocked(device_id):
            return render(request, 'adminlogin.html', {'blocked': True, 
                                                        'error_message': 'Your device is permanently blocked due to multiple failed login attempts.'})

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser or (user.is_staff and not user.is_active):
                FailedLoginAttempts.objects.filter(device_id=device_id).update(attempts=0, is_active=False)
                response = redirect('adminpage')
                set_device_cookie(response, device_id)
                login(request, user)
                return response
            else:
                return render(request, 'adminlogin.html', {'error_message': 'You do not have permission to access the admin page.'})
        else:
            failed_attempt, created = FailedLoginAttempts.objects.get_or_create(device_id=device_id)
            if not created:
                failed_attempt.attempts += 1
                failed_attempt.save()
                if failed_attempt.attempts >= MAX_FAILED_ATTEMPTS:
                    failed_attempt.is_active = True
                    failed_attempt.save()
                    return render(request, 'adminlogin.html', {'blocked': True, 
                                                            'error_message': 'Your device is permanently blocked due to multiple failed login attempts.'})
            else:
                failed_attempt.attempts = 1
                failed_attempt.save()
            return render(request, 'adminlogin.html', {'error_message': 'Invalid username or password'})
    else:
        response = render(request, 'adminlogin.html')
        if 'device_id' not in request.COOKIES:
            device_id = get_device_id(request)
            set_device_cookie(response, device_id)
        return response

@login_required(login_url='adminlogin')
def adminpage(request):
    return render(request,'adminpage.html')

@login_required(login_url='adminlogin')
@csrf_exempt
def createvisitor(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        person_phone = request.POST.get('person_phone')
        purpose = request.POST.get('purpose')  
        try:
            visitor = Register(
                person_name=person_name,
                phone_no=person_phone, 
                purpose_of_visit=purpose,
                visite_time=timezone.now()
            )
            visitor.save()
            return JsonResponse({'success': True, 'visitor_data': {
                'name': visitor.person_name,
                'phone': str(visitor.phone_no),  
                'visit_id': visitor.visit_id,
                'visit_time':visitor.visite_time,
            }, 'message': 'Visitor registered successfully!'})

        except Exception as e: 
            return JsonResponse({'success': False, 'message': str(e)})

    return redirect('adminpage') 

@login_required(login_url='adminlogin')
@csrf_exempt
def adminscan(request):
    return render(request,'adminscan.html')