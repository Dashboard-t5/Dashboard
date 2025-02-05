#           План тестирования EmployeesCountWithSkillsViewSet
#    1) Проверка корректного отображения списка сотрудников, владеющих
#       навыками
#    2) Проверка сортировки
#    3) Проверка фильтров (см. модуль tests_filter_set.py)

#           План тестирования EmployeesWithSkillViewSet
#    1) Проверка корректного отображения списка сотрудников, владеющих
#       выбранным навыком
#    2) Проверка фильтров (см. модуль tests_filter_set.py)

from datetime import date, timedelta
from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestEmployeesCountWithSkillsViewSet(APITestCase):

    view_name = "api:employees_count_with_skills-list"

    @classmethod
    def setUpTestData(cls):

        cls.domain_1 = baker.make(
            "ratings.Domain",
            name="Hard skills",
        )
        cls.domain_2 = baker.make(
            "ratings.Domain",
            name="Soft skills",
        )

        cls.skill_1 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_1,
            ),
            name="Skill_#1",
        )
        cls.skill_2 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_1,
            ),
            name="Skill_#2",
        )
        cls.skill_3 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_2,
            ),
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

        cls.rating_1_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_1_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_2,
            suitability="нет",
        )
        cls.rating_1_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_3,
            suitability="нет",
        )
        cls.rating_2_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_2_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_2,
            suitability="да",
        )
        cls.rating_2_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_3,
            suitability="нет",
        )
        cls.rating_3_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_3_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_2,
            suitability="да",
        )
        cls.rating_3_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_3,
            suitability="да",
        )
        cls.url = reverse(cls.view_name)

    def test_employees_count_with_skills_calculating(self):
        """
        Проверяет, что количество сотрудников, владеющих
        навыками соответствует ожидаемому.
        """
        expected_response_data = [
            {
                'domain': 'Soft skills',
                'skill_id': '3',
                'skill_name': 'Skill_#3',
                'count_employees': 1
            },
            {
                'domain': 'Hard skills',
                'skill_id': '2',
                'skill_name': 'Skill_#2',
                'count_employees': 2
            },
            {
                'domain': 'Hard skills',
                'skill_id': '1',
                'skill_name': 'Skill_#1',
                'count_employees': 3
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
        Проверяет, что поменяется порядок скиллов в
        ответе, если изменить количество сотрудников,
        владеющих навыком 'Skill_#3'
        """
        rating_1_3_extra = baker.make(
            "ratings.Rating",
            employee=self.employee_1,
            rating_date=date.today() - timedelta(days=1),
            skill=self.skill_3,
            suitability="да",
        )
        rating_2_3_extra = baker.make(
            "ratings.Rating",
            employee=self.employee_2,
            rating_date=date.today() - timedelta(days=1),
            skill=self.skill_3,
            suitability="да",
        )
        expected_response_data = [
            {
                'domain': 'Hard skills',
                'skill_id': '2',
                'skill_name': 'Skill_#2',
                'count_employees': 2
            },
            {
                'domain': 'Hard skills',
                'skill_id': '1',
                'skill_name': 'Skill_#1',
                'count_employees': 3
            },
            {
                'domain': 'Soft skills',
                'skill_id': '3',
                'skill_name': 'Skill_#3',
                'count_employees': 3
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


class TestEmployeesWithSkillViewSet(APITestCase):

    view_name = "api:skill_employee-list"

    @classmethod
    def setUpTestData(cls):

        cls.domain_1 = baker.make(
            "ratings.Domain",
            name="Hard skills",
        )
        cls.domain_2 = baker.make(
            "ratings.Domain",
            name="Soft skills",
        )

        cls.skill_1 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_1,
            ),
            name="Skill_#1",
        )
        cls.skill_2 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_1,
            ),
            name="Skill_#2",
        )
        cls.skill_3 = baker.make(
            "ratings.Skill",
            competence = baker.make(
                "ratings.Competence",
                domain=cls.domain_2,
            ),
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

        cls.rating_1_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_1_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_2,
            suitability="нет",
        )
        cls.rating_1_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_1,
            skill=cls.skill_3,
            suitability="нет",
        )
        cls.rating_2_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_2_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_2,
            suitability="да",
        )
        cls.rating_2_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skill_3,
            suitability="нет",
        )
        cls.rating_3_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_1,
            suitability="да",
        )
        cls.rating_3_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_2,
            suitability="да",
        )
        cls.rating_3_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_3,
            suitability="да",
        )
        cls.url = reverse(cls.view_name, args=(cls.skill_1.id,))

    def test_skill_employee_list(self):
        """
        Проверяет, что список сотрудников, владеющих
        выбранным навыком соответствует ожидаемому.
        """
        expected_response_data = [
            {
                'domain': 'Hard skills',
                'employee': 'employee 1',
                'count_employees': 1
            },
            {
                'domain': 'Hard skills',
                'employee': 'employee 2',
                'count_employees': 1
            },
            {
                'domain': 'Hard skills',
                'employee': 'employee 3',
                'count_employees': 1
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
