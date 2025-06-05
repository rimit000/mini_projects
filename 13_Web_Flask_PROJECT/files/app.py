from flask import Flask, render_template, request
import pandas as pd
import joblib

# Flask 인스턴스
app = Flask(__name__)

# 1) 웹 폼 입력 피처 목록 (13개)
features = [
    'age','sex','cp','trestbps','chol',
    'fbs','restecg','thalach','exang',
    'oldpeak','slope','ca','thal'
]

# 2) 한글 라벨 매핑
display_names = {
    'age': '나이',
    'sex': '성별',
    'cp': '가슴 통증 유형',
    'trestbps': '안정시 혈압',
    'chol': '혈청 콜레스테롤',
    'fbs': '공복 혈당 >120mg/dl 여부',
    'restecg': '안정시 심전도(0~2)',
    'thalach': '최대 심박수',
    'exang': '운동성 협심증 여부',
    'oldpeak': 'ST 분절 저하도',
    'slope': 'ST 분절 기울기',
    'ca': '형광염색 채색 주요 혈관 수(0~3)',
    'thal': '혈류장애 유형'
}

# 3) 학습해 둔 Random Forest 모델 로드
model = joblib.load('heart_model_rf.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    probability = None
    # 초기 입력값을 빈 문자열로 세팅
    input_data = {feat: '' for feat in features}

    if request.method == 'POST':
        # 폼에서 받은 값으로 dict 채우기
        for feat in features:
            val = request.form.get(feat)
            if val not in (None, ''):
                input_data[feat] = float(val)
        # DataFrame 생성 & 예측
        df = pd.DataFrame([input_data], columns=features)
        proba = model.predict_proba(df)[0, 1]
        probability = round(proba * 100, 2)
        # 디버깅: 실제 입력 확인
        print("Input for prediction:", input_data)

    return render_template(
        'index.html',
        features=features,
        display_names=display_names,
        input_data=input_data,
        probability=probability
    )
