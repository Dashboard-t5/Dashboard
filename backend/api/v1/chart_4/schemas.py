from drf_spectacular.utils import (
    extend_schema,
)


chart_4_description_schema = {
    "tags": ["chart 4"]
}

CHART_4_A_SCHEMA = {
    "list": extend_schema(
        **chart_4_description_schema,
        summary="Вкладка A. 'Динамика развития навыков'"
                "(Доступно: ).",
        description="",
    ),
}

CHART_4_B1_SCHEMA = {
    "list": extend_schema(
        **chart_4_description_schema,
        summary="Вкладка B1. 'Оценки сотрудников по "
                "должностям.'"
                "(Доступно: ).",
        description="",
    ),
}

CHART_4_B2_SCHEMA = {
    "list": extend_schema(
        **chart_4_description_schema,
        summary="Вкладка B2. 'Оценки сотрудников по "
                "выбранной должности.'"
                "(Доступно: ).",
        description="",
    ),
}

CHART_4_B3_SCHEMA = {
    "list": extend_schema(
        **chart_4_description_schema,
        summary="Вкладка B3. 'Оценки сотрудников по "
                "выбранному грейду.'"
                "(Доступно: ).",
        description="",
    ),
}