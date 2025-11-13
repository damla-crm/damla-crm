from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerSerializer

# @login_required geçici olarak kapatıldı
def dashboard(request):
    # JavaScript tabanlı login kontrolü base.html'de yapılıyor
    return render(request, 'webapp/dashboard.html')

def login_view(request):
    # Basit bir login view'ı
    from django.contrib.auth import authenticate, login
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    
    return render(request, 'webapp/login.html')

def logout_view(request):
    from django.contrib.auth import logout
    
    logout(request)
    return redirect('login')

def calendar_view(request):
    return render(request, 'webapp/calendar.html')

def customers_view(request):
    return render(request, 'webapp/customers.html')


def document_tracking_view(request):
    return render(request, 'webapp/document_tracking.html')

def existing_data_view(request):
    return render(request, 'webapp/existing_data.html')

def add_data_view(request):
    return render(request, 'webapp/add_data.html')

def customer_detail_view(request):
    return render(request, 'webapp/customer_detail.html')

def sale_form_view(request):
    return render(request, 'webapp/sale_form.html')

def not_interested_view(request):
    return render(request, 'webapp/not_interested.html')


# ===== API VIEWS =====
class CustomerListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user).order_by('-createdDate')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)
