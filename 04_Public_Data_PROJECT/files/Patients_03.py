import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# --------------------------------------
# 1. 연령별 데이터 시각화
# --------------------------------------
# CSV 파일 읽기 (파일 이름은 상황에 맞게 수정)
age_data = pd.read_csv('J45_asthma_age.csv')

# '심사년도' 컬럼의 "년" 제거 후 정수형으로 변환
age_data['심사년도'] = age_data['심사년도'].str.replace('년', '').astype(int)

# 시각화를 위한 figure 생성
plt.figure(figsize=(10, 6))

# 각 연령대별로 선 그래프 그리기 (첫번째 컬럼은 '심사년도'이므로 제외)
for col in age_data.columns[1:]:
    plt.plot(age_data['심사년도'], age_data[col], marker='o', label=col)

plt.title('연도별 연령대별 천식 추이')
plt.xlabel('연도')
plt.ylabel('질병 건수')
plt.legend(title='연령대')
plt.grid(True)
plt.show()

# --------------------------------------
# 2. 지역별 데이터 시각화
# --------------------------------------
# CSV 파일 읽기
region_data = pd.read_csv('J45_asthma_location.csv')

# '심사년도' 컬럼 정제: "년" 제거 후 정수형 변환
region_data['심사년도'] = region_data['심사년도'].str.replace('년', '').astype(int)

# 시각화를 위한 figure 생성
plt.figure(figsize=(12, 8))

# 각 지역별 선 그래프 그리기 (첫번째 컬럼은 '심사년도'이므로 제외)
for col in region_data.columns[1:]:
    plt.plot(region_data['심사년도'], region_data[col], marker='o', label=col)

plt.title('연도별 지역별 천식 추이')
plt.xlabel('연도')
plt.ylabel('질병 건수')
# 범례가 많으므로, 범례 위치를 오른쪽 바깥쪽으로 배치
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()  # 레이아웃 조정
plt.show()
