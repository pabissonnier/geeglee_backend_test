from django.db import models


class Licence(models.Model):
    type = models.CharField(max_length=200, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='licence_company')

    def __str__(self):
        return self.type


class Company(models.Model):
    name = models.CharField(max_length=200, null=False)
    area = models.CharField(max_length=200, null=False)
    nb_employees = models.IntegerField(null=False)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, null=True, related_name='company_licence')

    def __str__(self):
        return self.name


class Customer(models.Model):
    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
