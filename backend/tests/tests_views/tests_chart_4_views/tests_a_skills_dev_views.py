#           План тестирования SkillsDevelopmentViewSet
#    1) Проверка корректного калькуляции средней оценки по датам
#    2) Проверка сортировки

from datetime import date, timedelta

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestSkillsDevelopmentViewSet(APITestCase):

    view_name = "api:skills_development-list"

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

        cls.competence_1 = baker.make(
            "ratings.Competence",
            name="Competence_#1",
            domain=cls.domain_1,
        )
        cls.competence_2 = baker.make(
            "ratings.Competence",
            name="Competence_#2",
            domain=cls.domain_2,
        )

        cls.skill_1 = baker.make(
            "ratings.Skill",
            competence = cls.competence_1,
            name="Skill_#1",
        )
        cls.skill_2 = baker.make(
            "ratings.Skill",
            competence = cls.competence_2,
            name="Skill_#2",
        )
        cls.skill_3 = baker.make(
            "ratings.Skill",
            competence = cls.competence_2,
            name="Skill_#3",
        )

        cls.today_date = date(2024, 3, 25)
        two_days_ago_date = cls.today_date - timedelta(days=2)
        cls.rating_1 = baker.make(
            "ratings.Rating",
            skill=cls.skill_1,
            rating_date=two_days_ago_date,
            rating_value=4,
        )
        cls.rating_2 = baker.make(
            "ratings.Rating",
            skill=cls.skill_1,
            rating_date=two_days_ago_date,
            rating_value=5,
        )
        cls.rating_3 = baker.make(
            "ratings.Rating",
            skill=cls.skill_2,
            rating_date=two_days_ago_date,
            rating_value=3,
        )
        cls.rating_4 = baker.make(
            "ratings.Rating",
            skill=cls.skill_1,
            rating_date=cls.today_date,
            rating_value=5,
        )
        cls.rating_5 = baker.make(
            "ratings.Rating",
            skill=cls.skill_1,
            rating_date=cls.today_date,
            rating_value=5,
        )
        cls.rating_6 = baker.make(
            "ratings.Rating",
            skill=cls.skill_2,
            rating_date=cls.today_date,
            rating_value=4,
        )
        cls.url = reverse(cls.view_name)

    def test_rating_calculating(self):
        """
        Проверяет, что средние оценки расчитываются
        корректно.
        """
        expected_response_data = [
            {
                'rating_date': '2024-03-23',
                'average_rating': '4.00',
                'average_rating_hard': '4.50',
                'average_rating_soft': '3.00'
            },
            {
                'rating_date': '2024-03-25',
                'average_rating': '4.67',
                'average_rating_hard': '5.00',
                'average_rating_soft': '4.00'
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
        Проверяет, что поменяется порядок оценок
        если добавить оценки за вчерашний день.
        Ожидаем, оценки за вчера будут между оценками
        за позавчера и сегодня.
        """
        yesterday_date = self.today_date - timedelta(days=1)
        rating_7 = baker.make(
            "ratings.Rating",
            skill=self.skill_1,
            rating_date=yesterday_date,
            rating_value=3,
        )
        rating_8 = baker.make(
            "ratings.Rating",
            skill=self.skill_1,
            rating_date=yesterday_date,
            rating_value=4,
        )
        rating_9 = baker.make(
            "ratings.Rating",
            skill=self.skill_2,
            rating_date=yesterday_date,
            rating_value=3,
        )
        expected_response_data = [
            {
                'rating_date': '2024-03-23',
                'average_rating': '4.00',
                'average_rating_hard': '4.50',
                'average_rating_soft': '3.00'
            },
            {
                'rating_date': '2024-03-24',
                'average_rating': '3.33',
                'average_rating_hard': '3.50',
                'average_rating_soft': '3.00'
            },
            {
                'rating_date': '2024-03-25',
                'average_rating': '4.67',
                'average_rating_hard': '5.00',
                'average_rating_soft': '4.00'
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
