#           План тестирования PositionRatingViewSet
#    1) Проверка корректного калькуляции средней оценки по должностям
#    2) Проверка сортировки

from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from employees.constants import JUNIOR, MIDDLE, SENIOR


class TestPositionRatingViewSet(APITestCase):

    view_name = "api:position_rating-list"

    @classmethod
    def setUpTestData(cls):

        cls.position_team_lead = baker.make(
            "employees.Position",
            name="Teamlead",
        )
        cls.position_developer = baker.make(
            "employees.Position",
            name="Developer",
        )
        cls.position_tester = baker.make(
            "employees.Position",
            name="Tester",
        )
        cls.employee_1_a = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1_a",
            position=cls.position_team_lead,
        )
        cls.employee_1_b = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="1_b",
            position=cls.position_team_lead,
        )
        cls.employee_2_a = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2_a",
            position=cls.position_developer,
        )
        cls.employee_2_b = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="2_b",
            position=cls.position_developer,
        )
        cls.employee_3_a = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="3_a",
            position=cls.position_tester,
        )
        cls.employee_3_b = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="3_b",
            position=cls.position_tester,
        )
        cls.employee_3_c = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="3_c",
            position=cls.position_tester,
        )

        cls.rating_1_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_1_a,
            rating_value=4,
        )
        cls.rating_1_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_1_b,
            rating_value=5,
        )
        cls.rating_2_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_2_a,
            rating_value=3,
        )
        cls.rating_2_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_2_b,
            rating_value=2,
        )
        cls.rating_3_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_3_a,
            rating_value=5,
        )
        cls.rating_3_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_3_b,
            rating_value=4,
        )
        cls.rating_3_c = baker.make(
            "ratings.Rating",
            employee=cls.employee_3_c,
            rating_value=4,
        )
        cls.url = reverse(cls.view_name)


    def test_rating_average_by_position_calculating(self):
        """
        Проверяет, что средняя оценка по
         должностям считается корректно.
        """
        expected_response_data = [
            {
                'position': 'Developer',
                'position_id': '2',
                'average_rating': '2.50'
            },
            {
                'position': 'Tester',
                'position_id': '3',
                'average_rating': '4.33'
            },
            {
                'position': 'Teamlead',
                'position_id': '1',
                'average_rating': '4.50'
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

    def test_rating_average_by_position_ordering(self):
        """
         Проверяет, что поменяется порядок средних
         оценок по должностям если снизить среднюю
          оценку Тимлидам ниже чем у Тестеров.
         """

        rating_3_b_extra = baker.make(
            "ratings.Rating",
            employee=self.employee_1_b,
            rating_value=2,
        )
        expected_response_data = [
            {
                'position': 'Developer',
                'position_id': '2',
                'average_rating': '2.50'
            },
            {
                'position': 'Teamlead',
                'position_id': '1',
                'average_rating': '3.67'
            },
            {
                'position': 'Tester',
                'position_id': '3',
                'average_rating': '4.33'
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


#           План тестирования PositionRatingViewSet
#    1) Проверка корректного калькуляции средней оценки по должностям
#    2) Проверка сортировки


class TestGradeRatingViewSet(APITestCase):

    view_name = "api:grade_rating-list"

    @classmethod
    def setUpTestData(cls):

        cls.position_developer = baker.make(
            "employees.Position",
            name="Developer",
        )
        cls.employee_dev_jun = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_jun",
            grade=JUNIOR,
            position=cls.position_developer,
        )
        cls.employee_dev_mid = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_mid",
            grade=MIDDLE,
            position=cls.position_developer,
        )
        cls.employee_dev_sen = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_sen",
            grade=SENIOR,
            position=cls.position_developer,
        )

        cls.rating_dev_jun_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun,
            rating_value=4,
        )
        cls.rating_dev_mid_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_mid,
            rating_value=5,
        )
        cls.rating_dev_sen_1 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_sen,
            rating_value=3,
        )
        cls.rating_dev_jun_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun,
            rating_value=5,
        )
        cls.rating_dev_mid_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_mid,
            rating_value=5,
        )
        cls.rating_dev_sen_2 = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_sen,
            rating_value=4,
        )

        cls.url = reverse(cls.view_name, args=(cls.position_developer.id,))


    def test_rating_average_by_grade_calculating(self):
        """
        Проверяет, что средняя оценка по
         грейду считается корректно.
        """
        expected_response_data = [
            {'grade': 'Senior', 'average_rating': '3.50'},
            {'grade': 'Junior', 'average_rating': '4.50'},
            {'grade': 'Middle', 'average_rating': '5.00'}
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

    def test_rating_average_by_grade_ordering(self):
        """
         Проверяет, что поменяется порядок средних
         оценок по грейдам если снизить среднюю
          оценку Junior ниже чем у Senior.
         """

        rating_dev_jun_3 = baker.make(
            "ratings.Rating",
            employee=self.employee_dev_jun,
            rating_value=1,
        )
        expected_response_data = [
            {'grade': 'Junior', 'average_rating': '3.33'},
            {'grade': 'Senior', 'average_rating': '3.50'},
            {'grade': 'Middle', 'average_rating': '5.00'}
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



#           План тестирования EmployeeRatingViewSet
#    1) Проверка корректного калькуляции средней оценки по должностям
#    2) Проверка сортировки


class TestEmployeeRatingViewSet(APITestCase):

    view_name = "api:employee_rating-list"

    @classmethod
    def setUpTestData(cls):

        cls.position_developer = baker.make(
            "employees.Position",
            name="Developer",
        )
        cls.employee_dev_jun_1 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_jun_1",
            grade=JUNIOR,
            position=cls.position_developer,
        )
        cls.employee_dev_jun_2 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_jun_2",
            grade=JUNIOR,
            position=cls.position_developer,
        )
        cls.employee_dev_jun_3 = baker.make(
            "employees.Employee",
            last_name="employee",
            first_name="dev_jun_3",
            grade=JUNIOR,
            position=cls.position_developer,
        )

        cls.rating_dev_jun_1_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_1,
            rating_value=4,
        )
        cls.rating_dev_jun_1_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_1,
            rating_value=5,
        )
        cls.rating_dev_jun_2_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_2,
            rating_value=3,
        )
        cls.rating_dev_jun_2_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_2,
            rating_value=4,
        )
        cls.rating_dev_jun_3_a = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_3,
            rating_value=3,
        )
        cls.rating_dev_jun_3_b = baker.make(
            "ratings.Rating",
            employee=cls.employee_dev_jun_3,
            rating_value=3,
        )

        cls.url = reverse(cls.view_name, args=(cls.position_developer.id, JUNIOR))


    def test_rating_average_by_employee_calculating(self):
        """
        Проверяет, что средняя оценка по
         сотруднику считается корректно.
        """
        expected_response_data = [
            {'employee': 'employee dev_jun_3', 'average_rating': '3.00'},
            {'employee': 'employee dev_jun_2', 'average_rating': '3.50'},
            {'employee': 'employee dev_jun_1', 'average_rating': '4.50'}
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

    def test_rating_average_by_employee_ordering(self):
        """
         Проверяет, что поменяется порядок средних оценок
          по сотруднику если снизить среднюю оценку
          employee dev_jun_2 ниже чем у employee dev_jun_3.
         """

        rating_dev_jun_2_с = baker.make(
            "ratings.Rating",
            employee=self.employee_dev_jun_2,
            rating_value=1,
        )
        expected_response_data = [
            {'employee': 'employee dev_jun_2', 'average_rating': '2.67'},
            {'employee': 'employee dev_jun_3', 'average_rating': '3.00'},
            {'employee': 'employee dev_jun_1', 'average_rating': '4.50'}
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
