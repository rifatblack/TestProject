
from django.test import TestCase
from .models import Company, Employee

class CompanyModelTest(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(name="Company X")
        self.assertEqual(company.name, "Company X")

class EmployeeModelTest(TestCase):
    def test_employee_creation(self):
        company = Company.objects.create(name="Company Y")
        employee = Employee.objects.create(user=None, company=company)
        self.assertEqual(employee.company, company)
