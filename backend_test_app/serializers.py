from rest_framework import serializers

from .models import Customer, Company, Licence


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'fname', 'lname', 'email', 'company')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'area', 'nb_employees', 'licence')


class LicenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Licence
        fields = ('id', 'type', 'start_date', 'end_date', 'company')
