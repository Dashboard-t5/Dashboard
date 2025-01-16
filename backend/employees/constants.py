POSITION_NAME_MAX_LENGTH = 150
TEAM_NAME_MAX_LENGTH = 150

FIRST_NAME_MIN_LENGTH = 2
FIRST_NAME_MAX_LENGTH = 150

LAST_NAME_MIN_LENGTH = 2
LAST_NAME_MAX_LENGTH = 150

FULL_NAME_MAX_LENGTH = 150
# VALID_NAME_REGEX = r"^[а-яА-ЯёЁa-zA-Z]+(\s?\-?[а-яА-ЯёЁa-zA-Z]+){0,5}$"
VALID_NAME_REGEX = r"^[А-ЯЁа-яёA-Za-z]+(?:[\s\-]?[А-ЯЁа-яёA-Za-z]+)*$"


# CHOICES для модели сотрудника Employee
JUNIOR = "Junior"
MIDDLE = "Middle"
SENIOR = "Senior"
INTERN = "Intern"
LEAD = "Lead"
HEAD = "Head"

GRADE_CHOICES = (
    (JUNIOR, "Джуниор"),
    (MIDDLE, "Мидл"),
    (SENIOR, "Сеньор"),
    (INTERN, "Cтажер"),
    (LEAD, "Ведущий специалист"),
    (HEAD, "Руководитель"),
)

GRADE_MAX_LENGTH = max(len(grade) for grade, _ in GRADE_CHOICES)
