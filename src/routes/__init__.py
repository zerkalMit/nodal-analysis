from fastapi import APIRouter
from src.models.models import NodalCalcRequest, NodalCalcResponse

main_router = APIRouter(prefix="/nodal", tags=["NodalAnalysis"])


@main_router.post("/calc", response_model=NodalCalcResponse)
def my_profile(data: NodalCalcRequest):
    """
    Эндпоинт для выполнения Узлового Анализа
    """
    parsed = data.dict()
    from src.calculations.nodal import calc_nodal

    result = calc_nodal(parsed.get('ipr'), parsed.get('vlp'))
    # Функция для выполнения узлового анализа
    return NodalCalcResponse.parse_obj(result)
