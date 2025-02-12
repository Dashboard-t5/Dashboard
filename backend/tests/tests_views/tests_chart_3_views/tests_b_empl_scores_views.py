#           План тестирования EmployeeScoresViewSet
#    1) Проверка корректного отображения балов сотрудников
#    по навыкам и датам
#    2) Проверка сортировки
#    3) Проверка фильтров (см. модуль tests_filter_set.py)

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestEmployeeScoresViewSet(APITestCase):

    view_name = "api:employee_scores-list"

    @classmethod
    def setUpTestData(cls):

        cls.domain_1 = baker.make(
            "ratings.Domain",
            name="Hard skills",
        )
        # cls.domain_2 = baker.make(
        #     "ratings.Domain",
        #     name="Soft skills",
        # )

        cls.competence_1 = baker.make(
            "ratings.Competence",
            name="Competence_#1",
            domain=cls.domain_1,
        )

        cls.skill_1 = baker.make(
            "ratings.Skill",
            competence = cls.competence_1,
            name="Skill_#1",
        )
        cls.skill_2 = baker.make(
            "ratings.Skill",
            competence = cls.competence_1,
            name="Skill_#2",
        )
        cls.skill_3 = baker.make(
            "ratings.Skill",
            competence = cls.competence_1,
            name="Skill_#3",
        )

        cls.employee_1 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1",
        )
        cls.employee_2 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2",
        )
        cls.employee_3 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="3",
        )
        cls.rating_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_1,
            rating_value=4,
        )
        cls.rating_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_1,
            rating_value=5,
        )
        cls.rating_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_2,
            rating_value=3,
        )
        cls.url = reverse(cls.view_name)

    def test_scores(self):
        """
        Проверяет, что балы сотрудников выводятся корректно
        """
        expected_response_data = [
            {
                'employee': 'employee 1',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#1',
                'rating_date': '2025-02-12',
                'rating_value': 4
            }, {
                'employee': 'employee 2',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#1',
                'rating_date': '2025-02-12',
                'rating_value': 5
            }, {
                'employee': 'employee 3',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#2',
                'rating_date': '2025-02-12',
                'rating_value': 3
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
        Проверяет, что поменяется порядок сотрудников
        если изменить имя сотрудника с 'employee 3'
        на 'employee 0'.
        """

        self.employee_3.first_name = "0"
        self.employee_3.save()
        expected_response_data = [
            {
                'employee': 'employee 0',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#2',
                'rating_date': '2025-02-12',
                'rating_value': 3
            },
            {
                'employee': 'employee 1',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#1',
                'rating_date': '2025-02-12',
                'rating_value': 4
            }, {
                'employee': 'employee 2',
                'domain': 'Hard skills',
                'competence_name': 'Competence_#1',
                'skill_name': 'Skill_#1',
                'rating_date': '2025-02-12',
                'rating_value': 5
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
