from rest_framework import viewsets
from .serializers import CompanySerializer, CustomerSerializer, LicenceSerializer
from .models import Company, Customer, Licence
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from urllib.request import urlopen
from django.http import HttpResponse
import json
import re


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        """ Overriding create function to ensure small caps for entries """
        company_data = request.data
        licence_url = company_data['licence']
        res = urlopen(licence_url).read()
        data = json.loads(res)
        licence_q = Licence.objects.get(id=data['id'])
        new_company = Company.objects.create(name=company_data['name'].lower(), area=company_data['area'].lower(),
                                             nb_employees=company_data['nb_employees'], licence=licence_q)

        new_company.save()

        factory = APIRequestFactory()
        request = factory.get('/')

        serializer_context = {
            'request': Request(request),
        }

        serializer = CompanySerializer(new_company, context=serializer_context)

        return Response(serializer.data)


class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all().order_by('type')
    serializer_class = LicenceSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    global new_customer
    queryset = Customer.objects.all().order_by('lname')
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        """ Overriding create function to ensure small caps for entries and format for email """
        customer_data = request.data
        company_url = customer_data['company']
        res = urlopen(company_url).read()
        data = json.loads(res)
        company_q = Company.objects.get(id=data['id'])

        email = customer_data['email']
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if re.search(email_regex, email):
            new_customer = Customer.objects.create(fname=customer_data['fname'].lower(),
                                                   lname=customer_data['lname'].lower(),
                                                   email=email, company=company_q)

            new_customer.save()

            factory = APIRequestFactory()
            request = factory.get('/')

            serializer_context = {
                'request': Request(request),
            }

            serializer = CustomerSerializer(new_customer, context=serializer_context)

            return Response(serializer.data)

        else:
            return HttpResponse("Email invalide")


