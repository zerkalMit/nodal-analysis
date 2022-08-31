from shapely.geometry import LineString

from src.models.models import NodalCalcDecision, NodalCalcResponse


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR
    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """

    lineWell = LineString(zip(vlp["p_wf"], vlp["q_liq"]))
    linePast = LineString(zip(ipr["p_wf"], ipr["q_liq"]))
    # Можно использовать numpy или библиотеку Shapely, LineString intersection

    result = lineWell.intersection(linePast)
    points_parse=NodalCalcDecision(p_wf=result.x, q_liq=result.y).dict()
    return [points_parse]
    pass

