# #           План тестирования RatingFilter
# #    1) Проверка корректного калькуляции средней оценки по должностям
# #    2) Проверка сортировки
#
#
# from model_bakery import baker
#
# from rest_framework import status
# from rest_framework.reverse import reverse
# from rest_framework.test import APITestCase
#
# from employees.constants import JUNIOR, MIDDLE, SENIOR
#
#
# class TestRatingFilter(APITestCase):
#
#     view_name = "api:skill_employee-list"
#     skills_number = 4
#
#     @classmethod
#     def setUpTestData(cls):
#
#         cls.domain_1 = baker.make(
#             "ratings.Domain",
#             name="Hard skills",
#         )
#         cls.domain_2 = baker.make(
#             "ratings.Domain",
#             name="Soft skills",
#         )
#
#         cls.competence_1 = baker.make(
#             "ratings.Competence",
#             name="Competence_#1",
#             domain=cls.domain_1,
#         )
#         cls.competence_2 = baker.make(
#             "ratings.Competence",
#             name="Competence_#2",
#             domain=cls.domain_2,
#         )
#
#         cls.skill_1 = baker.make(
#             "ratings.Skill",
#             competence = cls.competence_1,
#             name="Skill_#1",
#         )
#         cls.skill_2 = baker.make(
#             "ratings.Skill",
#             competence = cls.competence_2,
#             name="Skill_#2",
#         )
#         cls.skill_3 = baker.make(
#             "ratings.Skill",
#             competence = cls.competence_2,
#             name="Skill_#3",
#         )
#
#         cls.position_team_lead = baker.make(
#             "employees.Position",
#             name="Teamlead",
#         )
#         cls.position_developer = baker.make(
#             "employees.Position",
#             name="Developer",
#         )
#         cls.position_tester = baker.make(
#             "employees.Position",
#             name="Tester",
#         )
#
#         cls.team_core = baker.make(
#             "employees.Team",
#             name="Core",
#         )
#         cls.team_media = baker.make(
#             "employees.Team",
#             name="Media",
#         )
#
#
#         cls.employee_1 = baker.make(
#             "employees.Employee",
#             last_name="employee_1",
#             position=cls.position_developer,
#             team=cls.team_core,
#             grade=JUNIOR
#         )
#         cls.employee_2 = baker.make(
#             "employees.Employee",
#             last_name="employee_2",
#         )
#         cls.employee_3 = baker.make(
#             "employees.Employee",
#             last_name="employee_3",
#         )
#
#         cls.skills = baker.make(
#             "ratings.Skill",
#             name=(f"Skill_#{i}" for i in range(cls.skills_number)),
#             _quantity=cls.skills_number
#         )
#
#         cls.rating_1 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_1,
#             skill=cls.skills[2],
#             suitability="да",
#         )
#         cls.rating_2 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_1,
#             skill=cls.skills[0],
#             suitability="нет",
#         )
#         cls.rating_3 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_2,
#             skill=cls.skills[2],
#             suitability="да",
#         )
#         cls.rating_4 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_2,
#             skill=cls.skills[3],
#             suitability="да",
#         )
#         cls.rating_5 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_3,
#             skill=cls.skills[2],
#             suitability="да",
#         )
#         cls.rating_6 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_3,
#             skill=cls.skills[3],
#             suitability="да",
#         )
#         cls.rating_7 = baker.make(
#             "ratings.Rating",
#             employee=cls.employee_3,
#             skill=cls.skills[4],
#             suitability="нет",
#         )
#
#     def test_bus_factor(self):
#
#         expected_response_data = {"skill": "Skill_#3", "bus_factor": 2}
#
#         response = self.client.get(self.url)
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK,
#             response.data
#         )
#         self.assertEqual(
#             response.data,
#             expected_response_data,
#             "Ответ не совпадает с ожидаемым."
#         )
