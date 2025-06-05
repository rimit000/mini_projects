# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
import joblib

# 1) 데이터 로드
df = pd.read_csv('heart.csv')

# 2) 특성과 타겟 분리
X = df.drop(columns=['target'])
y = df['target']

# 3) 학습/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4) 파이프라인 구성 (스케일링 + SVC)
pipeline = make_pipeline(
    StandardScaler(),
    SVC(kernel='rbf', C=2, probability=True, random_state=42)
)

# 5) 모델 학습
pipeline.fit(X_train, y_train)

# 6) 성능 평가
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

print('Accuracy:', accuracy_score(y_test, y_pred))
print('ROC AUC:', roc_auc_score(y_test, y_proba))
print('\nClassification Report:')
print(classification_report(y_test, y_pred))

# 7) 모델 저장
joblib.dump(pipeline, 'heart_model_pipeline.pkl')
print('\nModel pipeline saved to heart_model_pipeline.pkl')