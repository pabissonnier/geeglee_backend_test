from rest_framework import viewsets
from .serializers import CompanySerializer, CustomerSerializer, LicenceSerializer
from .models import Company, Customer, Licence


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer


class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all().order_by('type')
    serializer_class = LicenceSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('lname')
    serializer_class = CustomerSerializer
