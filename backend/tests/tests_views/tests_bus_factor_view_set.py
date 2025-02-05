from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestBusFactorViewSet(APITestCase):

    url = reverse("api:bus_factor-list")
    skills = None
    skills_number = 5

    @classmethod
    def setUpTestData(cls):

        cls.employee_1 = baker.make(
            "employees.Employee",
            last_name="employee_1",
        )
        cls.employee_2 = baker.make(
            "employees.Employee",
            last_name="employee_2",
        )
        cls.employee_3 = baker.make(
            "employees.Employee",
            last_name="employee_3",
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
            employee=cls.employee_2,
            skill=cls.skills[2],
            suitability="да",
        )
        cls.rating_4 = baker.make(
            "ratings.Rating",
            employee=cls.employee_2,
            skill=cls.skills[3],
            suitability="да",
        )
        cls.rating_5 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skills[2],
            suitability="да",
        )
        cls.rating_6 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skills[3],
            suitability="да",
        )
        cls.rating_7 = baker.make(
            "ratings.Rating",
            employee=cls.employee_3,
            skill=cls.skills[4],
            suitability="нет",
        )

    def test_bus_factor(self):

        expected_response_data = {"skill": "Skill_#3", "bus_factor": 2}

        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.data
        )
        self.assertEqual(
            response.data,
            expected_response_data,
            "Ответ не совпадает с ожидаемым."
        )
