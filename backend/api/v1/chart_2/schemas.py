from drf_spectacular.utils import (
    extend_schema,
)


chart_2_description_schema = {
    "tags": ["chart 2"]
}

CHART_2_A_SCHEMA = {
    "list": extend_schema(
        **chart_2_description_schema,
        summary="Вкладка A. 'Должности сотрудников'."
                "(Доступно: ).",
        description="",
    ),
}

CHART_2_B1_SCHEMA = {
    "list": extend_schema(
        **chart_2_description_schema,
        summary="Вкладка B1. 'Количество сотрудников по "
                "грейдам'. "
                "(Доступно: ).",
        description="",
    ),
}

CHART_2_B2_SCHEMA = {
    "list": extend_schema(
        **chart_2_description_schema,
        summary="Вкладка B2. 'Количество сотрудников по "
                "выбранному грейду'. "
                "(Доступно: ).",
        description="",
    ),
}
