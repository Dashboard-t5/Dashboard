from drf_spectacular.utils import (
    extend_schema,
)


chart_1_description_schema = {
    "tags": ["chart 1"]
}

CHART_1_A1_SCHEMA = {
    "list": extend_schema(
        **chart_1_description_schema,
        summary="Вкладка A1. 'Соответствие должности'.",
        description="(Доступно: ).",
    ),
}

CHART_1_A2_SCHEMA = {
    "list": extend_schema(
        **chart_1_description_schema,
        summary="Вкладка A2. 'Соответствие должности'"
                " для выбранного сотрудника.",
        description="(Доступно: ).",
    ),
}

CHART_1_B1_SCHEMA = {
    "list": extend_schema(
        **chart_1_description_schema,
        summary="Вкладка B1. 'Количество сотрудников, "
                "владеющих навыками'.",
        description="(Доступно: ).",
    ),
}

CHART_1_B2_SCHEMA = {
    "list": extend_schema(
        **chart_1_description_schema,
        summary="Вкладка B2. 'Количество сотрудников, "
                "владеющих навыками'. для выбранного навыка.",
        description="(Доступно: ).",
    ),
}