from drf_spectacular.utils import (
    extend_schema,
)


chart_3_description_schema = {
    "tags": ["chart 3"]
}

CHART_3_A_SCHEMA = {
    "list": extend_schema(
        **chart_3_description_schema,
        summary="Вкладка A. 'Уровень владения навыками'."
                "(Доступно: ).",
        description="",
    ),
}

CHART_3_B_SCHEMA = {
    "list": extend_schema(
        **chart_3_description_schema,
        summary="Вкладка B. 'Балы сотрудников по навыкам и датам."
                "(Доступно: ).",
        description="",
    ),
}
