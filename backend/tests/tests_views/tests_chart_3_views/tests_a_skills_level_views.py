#           План тестирования SkillsLevelViewSet
#    1) Проверка корректной калькуляции уровней владения навыков
#    2) Проверка сортировки

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestSkillsLevelViewSet(APITestCase):

    view_name = "api:skill_level-list"

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
            rating_value=3,
        )
        cls.rating_3 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skill_2,
            rating_value=3,
        )
        cls.url = reverse(cls.view_name)

    def test_skill_level_calculating(self):
        """
        Проверяет, что уровень владения навыками
         соответствует ожидаемому.
        """
        expected_response_data = [
            {
                'domain': 'Hard skills',
                'skill_name': 'Skill_#2',
                'skill_level': '3.00'
            },
            {
                'domain': 'Hard skills',
                'skill_name': 'Skill_#1',
                'skill_level': '3.50'
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
        Проверяет, что поменяется порядок навыков по
        уровню владения навыков если добавить новую
        оценку для скилла 'Skill_#2'.
        """

        rating_4 = baker.make(
            "ratings.Rating",
            employee=self.employee_2,
            skill=self.skill_2,
            rating_value=5,
        )
        expected_response_data = [
            {
                'domain': 'Hard skills',
                'skill_name': 'Skill_#1',
                'skill_level': '3.50'
            },
            {
                'domain': 'Hard skills',
                'skill_name': 'Skill_#2',
                'skill_level': '4.00'
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