from typing import Dict, Any
import numpy as np

LABEL_MAP = {0: "비추천", 1: "보통", 2: "추천"}


def fmt_trend(val: float | None, digits: int = 1) -> str:
    """
    - abs(val) 거의 0  → '큰 변화 없음'
    - val > 0          → 'x 증가'
    - val < 0          → 'x 감소'
    """
    if val is None:
        return "변화 정보 없음"

    try:
        v = float(val)
    except Exception:
        return "변화 정보 없음"

    if np.isnan(v):
        return "변화 정보 없음"

    if abs(v) < 1e-6:
        return "큰 변화 없음"
    elif v > 0:
        return f"{v:.{digits}f} 증가"
    else:
        return f"{abs(v):.{digits}f} 감소"
    
def make_report(
    gu: str,
    dong: str,
    category: str,
    feature_row: Dict[str, Any],
    label_index: int,
) -> str:
    """
    상권 리포트 텍스트 생성.
    - gu, dong, category : 라우터에서 받은 지역/업종 이름
    - feature_row        : read_afn 결과 dict
    - label_index        : 0/1/2
    """
    # gu, dong 중 하나 없으면 "해당 지역"
    if gu and dong:
        region = f"{gu} {dong}"
    else:
        region = "해당 지역"
        
    category = category
    
    label_name = LABEL_MAP.get(label_index, str(label_index))

    # 리포트에 쓸 핵심 피처
    qs_total_diff = feature_row.get("qs_total_diff_sqrt")
    qs_per_store_pct = feature_row.get("qs_per_store_pct")
    store_density_pct = feature_row.get("store_density_pct")
    comp_pres_pct = feature_row.get("comp_pres_pct")

    qs_total_txt = fmt_trend(qs_total_diff, digits=2)
    qs_per_store_txt = fmt_trend(qs_per_store_pct, digits=2)
    density_txt = fmt_trend(store_density_pct, digits=2)
    comp_txt = fmt_trend(comp_pres_pct, digits=2)

    header = (
        f"<strong>{region}</strong>의 <strong>{category}</strong> 상권은 최근 분기 기준으로 "
        f"전분기 대비 전체 매출이 {qs_total_txt}하고, "
        f"점포당 매출이 {qs_per_store_txt}한 것으로 나타납니다. <br>"
    )

    if label_index == 0:
        # 비추천 (위축형)
        body = (
            f"같은 기간 점포 밀도는 {density_txt}하고, 경쟁 압력은 {comp_txt}하면서 "
            "상권 내 수요와 공급이 전반적으로 약화되는 흐름을 보이고 있습니다. <br>"
            "매출·점포 효율·상권 밀도가 함께 둔화되는 양상이 관측되어, "
            "현재 시점에서는 신규 진입에 대해 <strong>'비추천'</strong>에 가까운 상권으로 판단됩니다."
        )
    elif label_index == 1:
        # 보통 (유지형)
        body = (
            f"점포 밀도와 경쟁 압력은 각각 {density_txt}, {comp_txt} 수준으로 "
            "크게 확대되거나 축소되지 않고 비교적 안정적인 흐름을 보입니다. <br>"
            "주요 지표에서 뚜렷한 성장 신호도, 급격한 위축 신호도 크지 않은 상태로 "
            "현 시점에서는 <strong>'보통'</strong> 수준의 상권으로 해석할 수 있습니다."
        )
    elif label_index == 2:
        # 추천 (성장형)
        body = (
            f"동시에 점포 밀도는 {density_txt}하고, 경쟁 압력은 {comp_txt}하는 가운데 "
            "전체 매출과 점포당 매출이 함께 개선되는 모습입니다. <br>"
            "경쟁이 존재하는 환경에서도 수요를 흡수하며 상권의 체력이 강화되는 구간으로, "
            "상대적으로 <strong>'추천'</strong>에 가까운 성장형 상권으로 진단됩니다."
        )
    else:
        body = (
            "모델 예측 라벨 정보를 정확히 확인할 수 없어 상권 유형을 특정하기는 어렵지만, "
            "아래 지표들을 참고하여 상권의 현재 상태를 해석할 수 있습니다."
        )

    return header + body