#           План тестирования SuitabilityPositionViewSet
#    1) Проверка калькуляции средней оценки
#    2) Проверка сортировки
#    3) Проверка фильтров (см. модуль tests_filter_set.py)

#           План тестирования EmployeeSkillsAverageRatingViewSet
#    1) Проверка корректной калькуляции средней оценки
#    2) Проверка сортировки
#    3) Проверка фильтров (см. модуль tests_filter_set.py)

from datetime import date, timedelta
from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestSuitabilityPositionViewSet(APITestCase):

    view_name = "api:suitability_position-list"
    skills = None
    skills_number = 5

    @classmethod
    def setUpTestData(cls):

        cls.team_1 = baker.make(
            "employees.Team",
            name="team_1",
        )
        cls.team_2 = baker.make(
            "employees.Team",
            name="team_2",
        )

        cls.employee_1 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1",
            team=cls.team_1,
        )
        cls.employee_2 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2",
            team=cls.team_2,
        )

        cls.skills = baker.make(
            "ratings.Skill",
            name=(f"Skill_#{i}" for i in range(cls.skills_number)),
            _quantity=cls.skills_number
        )

        cls.rating_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[2],
            suitability="да",
        )
        cls.rating_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[0],
            suitability="нет",
        )
        cls.rating_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[1],
            suitability="да",
        )
        cls.rating_4 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[0],
            suitability="да",
        )
        cls.rating_5 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[2],
            suitability="да",
        )
        cls.rating_6 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[3],
            suitability="да",
        )
        cls.rating_7 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[4],
            suitability="нет",
        )
        cls.rating_8 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[4],
            rating_date=date.today() - timedelta(days=1),
            suitability="нет",
        )
        cls.rating_9 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[4],
            rating_date=date.today() - timedelta(days=2),
            suitability="нет",
        )
        cls.url = reverse(cls.view_name)

    def test_suitability_calculating(self):
        """
        Проверяет, что количество оценок и средний процент
        положительных оценок соответствует ожидаемому.
        """
        expected_response_data = [
            {
                'employee_id': '2',
                'employee': 'employee 2',
                'total_yes': 3,
                'total': 6,
                'percentage': 50.0
            },
            {
                'employee_id': '1',
                'employee': 'employee 1',
                'total_yes': 2,
                'total': 3,
                'percentage': 66.0
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
        Проверяет, что поменяется порядок сотрудников в
        выборке, если 'employee 1' опустить среднюю оценку
        ниже чем у 'employee 2'
        """
        baker.make(
            "ratings.Rating",
            employee=self.employee_1,
            skill=self.skills[3],
            rating_date=date.today() - timedelta(days=1),
            suitability="нет",
        )
        baker.make(
            "ratings.Rating",
            employee=self.employee_1,
            skill=self.skills[3],
            rating_date=date.today() - timedelta(days=2),
            suitability="нет",
        )
        expected_response_data = [
            {
                'employee_id': '1',
                'employee': 'employee 1',
                'total_yes': 2,
                'total': 5,
                'percentage': 40.0
            },
            {
                'employee_id': '2',
                'employee': 'employee 2',
                'total_yes': 3,
                'total': 6,
                'percentage': 50.0
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


class TestEmployeeSkillsAverageRatingViewSet(APITestCase):

    view_name = "api:employee_skills-list"
    skills = None
    skills_number = 5

    @classmethod
    def setUpTestData(cls):

        cls.team_1 = baker.make(
            "employees.Team",
            name="team_1",
        )
        cls.team_2 = baker.make(
            "employees.Team",
            name="team_2",
        )

        cls.employee_1 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1",
            team=cls.team_1,
        )
        cls.employee_2 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2",
            team=cls.team_2,
        )

        cls.skills = baker.make(
            "ratings.Skill",
            name=(f"Skill_#{i}" for i in range(cls.skills_number)),
            _quantity=cls.skills_number
        )

        cls.rating_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[2],
            rating_value=5,
        )
        cls.rating_2a = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[3],
            rating_date=date.today(),
            rating_value=4,
        )
        cls.rating_2b = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[3],
            rating_date=date.today() - timedelta(days=1),
            rating_value=3,
        )
        cls.rating_2c = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[3],
            rating_date=date.today() - timedelta(days=2),
            rating_value=4,
        )
        cls.rating_3a = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[4],
            rating_date=date.today(),
            rating_value=4,
        )
        cls.rating_3b = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skills[4],
            rating_date=date.today() - timedelta(days=1),
            rating_value=5,
        )
        cls.rating_4 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[4],
            rating_value=3,
        )
        cls.url = reverse(viewname=cls.view_name, args=(cls.employee_1.id,))

    def test_employee_skills_calculating(self):
        """
        Проверяет, что расчет средних оценок по скиллам
        соответствует ожидаемому.
        """
        expected_response_data = [
            {'skill_name': 'Skill_#3', 'average_rating': 3.7},
            {'skill_name': 'Skill_#4', 'average_rating': 4.5},
            {'skill_name': 'Skill_#2', 'average_rating': 5.0}
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
        Проверяет, что поменяется порядок скиллов в
        ответе, если 'employee 1' опустить среднюю оценку
        для 'Skill_#2' ниже чем для 'Skill_#3' и 'Skill_#4'
        """
        baker.make(
            "ratings.Rating",
            employee=self.employee_1,
            skill=self.skills[2],
            rating_date=date.today() - timedelta(days=2),
            rating_value=2,
        )

        expected_response_data = [
            {'skill_name': 'Skill_#2', 'average_rating': 3.5},
            {'skill_name': 'Skill_#3', 'average_rating': 3.7},
            {'skill_name': 'Skill_#4', 'average_rating': 4.5}
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
