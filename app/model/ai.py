import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import db.dbt_afn as dbt_afn
import joblib
import numpy as np
import lightgbm as lgb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model/lgb_model_p2.pkl")

def load_lgb_model():
    try:
        with open(MODEL_PATH, "rb") as f:
            model = joblib.load(f)
            return model
        # model = joblib.load('model/lgb_model_p2.pkl')
        # return model
    except Exception as e:
        print("모델 로드 오류:", e)
        return None

def make_feature_array(feature_dict):
    feature_order = [
        "qs_log", "qs_per_store", "qs_total_diff_sqrt", "store_density",
        "comp_pres", "comp_pres_pct", "qs_per_store_pct", "store_density_pct",
        "qs_1114_pct", "qs_1721_pct", "qs_2124_pct", "qs_weekdays_pct",
        "qs_weekend_pct", "qs_2030_pct", "qs_3050_pct", "qs_60_pct",
        "fp_log", "wp_log", "rp_log", "subway_station", "bus_log",
        "traffic_score", "apt_cnt", "apt_log"
    ]
    print("Feature Dict:", feature_dict)
    # 순서에 맞게 리스트 생성
    values = [feature_dict.get(key, 0) for key in feature_order]
    
    return np.array(values).reshape(1, -1)  # LightGBM 입력 형태

def predict_sales(body):
    # 1) Feature 조회
    feature_list = dbt_afn.read_featrue(body)

    if not feature_list:
        print("조회된 데이터가 없습니다.")
        return None

    feature = feature_list[0]   # 첫 번째 row 사용

    # 2) feature → numpy 변환
    feature_array = make_feature_array(feature)

    # 3) 모델 로드
    model = load_lgb_model()
    if model is None:
        return None

    # 4) LightGBM 예측
    prediction = model.predict(feature_array)

    return float(prediction[0])


if __name__ == '__main__':
    body = {
        "gu": "강남구",
        "dong": "대치1동",
        "category": "PC방"
    }
    result = predict_sales(body)
    print("Predicted Sales:", result)