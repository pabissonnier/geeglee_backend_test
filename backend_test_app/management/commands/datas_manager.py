# -*- coding: utf-8 -*-

from backend_test_app.models import Customer, Company, Licence
from .datas import customer, company, licence
from datetime import datetime, timedelta


class DatasManager:
    """ Insertion scripts for initial datas through Django Custom Commands"""
    def __init__(self):
        pass

    @staticmethod
    def licence_insertion():
        for data in licence:
            start_date = datetime.strptime(data["start_date"], "%Y-%m-%d %H:%M:%S")
            end_date = start_date + timedelta(days=730)
            company = Company.objects.get(name=data['company'])
            Licence.objects.create(type=data["type"], start_date=start_date, end_date=end_date, company=company)


    @staticmethod
    def company_insertion():
        for key, value in company.items():
            name = key
            area = value["area"]
            employees = value["employees"]
            data_already = Company.objects.filter(name=name)
            if not data_already:
                Company.objects.create(name=name, area=area, nb_employees=employees)


    @staticmethod
    def customer_insertion():
        for data in customer:
            company = Company.objects.get(name=data["company"])
            Customer.objects.create(fname=data["lname"], lname=data["fname"], email=data["email"], company=company)


    @staticmethod
    def fk_insertion():
        from .datas import company
        for key, value in company.items():
            name = key
            company_q = Company.objects.get(name=name)
            company_q.licence = Licence.objects.get(id=value["licence"])
            company_q.save()



