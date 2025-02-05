#           План тестирования EmployeePositionsViewSet
#    1) Проверка корректной калькуляции процента сотрудников по должностям
#    2) Проверка сортировки
#    3) Проверка фильтров (см. модуль tests_filter_set.py)

from datetime import date, timedelta
from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestEmployeePositionsViewSet(APITestCase):

    view_name = "api:employee_positions-list"

    @classmethod
    def setUpTestData(cls):

        cls.position_1 = baker.make(
            "employees.Position",
            name="position_1",
        )
        cls.position_2 = baker.make(
            "employees.Position",
            name="position_2",
        )

        cls.employee_1 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1",
            position=cls.position_1,
        )
        cls.employee_2 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2",
            position=cls.position_1,
        )
        cls.employee_3 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="3",
            position=cls.position_2,
        )
        cls.rating_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
        )
        cls.rating_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
        )
        cls.rating_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
        )
        cls.url = reverse(cls.view_name)

    def test_employee_positions_percentage_calculating(self):
        """
        Проверяет, что процент сотрудников по должностям
         соответствует ожидаемому.
        """
        expected_response_data = [
            {
                'position': 'position_2',
                'position_employee_count': 1,
                'total_employee_count': 3,
                'percentage': 33.3
            },
            {
                'position': 'position_1',
                'position_employee_count': 2,
                'total_employee_count': 3,
                'percentage': 66.7
            }
        ]
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.data
        )
        self.assertEqual(
            response.data,
            expected_response_data,
        )


    def test_ordering(self):
        """
        Проверяет, что поменяется порядок списка сотрудников
        по должностям если добавить новых сотрудников на
         должность 'position_2'
        """
        employee_4 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="4",
            position=self.position_2,
        )
        employee_5 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="5",
            position=self.position_2,
        )
        rating_4 = baker.make(
            "ratings.Rating",
            employee=employee_4,
        )
        rating_5 = baker.make(
            "ratings.Rating",
            employee=employee_5,
        )
        expected_response_data = [
            {
                'position': 'position_1',
                'position_employee_count': 2,
                'total_employee_count': 5,
                'percentage': 40.0
            }, {
                'position': 'position_2',
                'position_employee_count': 3,
                'total_employee_count': 5,
                'percentage': 60.0}
        ]
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.data
        )
        self.assertEqual(
            response.data,
            expected_response_data,
        )
