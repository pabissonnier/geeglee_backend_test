# -*- coding: utf-8 -*-

from .datas_manager import DatasManager

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        DatasManager.company_insertion()
        DatasManager.licence_insertion()
        DatasManager.customer_insertion()
        DatasManager.fk_insertion()

