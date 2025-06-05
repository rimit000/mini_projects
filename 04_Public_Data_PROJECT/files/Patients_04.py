import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# CSV 파일 읽기
region_data = pd.read_csv('J45_asthma_location.csv')

# '심사년도' 컬럼의 "년" 제거 후 정수형으로 변환
region_data['심사년도'] = region_data['심사년도'].str.replace('년', '').astype(int)

# 연도 순서대로 정렬 후, '심사년도'를 인덱스로 설정
region_data = region_data.sort_values('심사년도').set_index('심사년도')

# 각 지역별로 전년도 대비 증감율(%) 계산
# pct_change()는 전년도 대비 증감율을 소수로 계산하므로 100을 곱해 %로 변환
region_change = region_data.pct_change() * 100

# 첫 해(2017년)는 증감율이 계산되지 않으므로 NaN이 나오는데, 필요에 따라 제거할 수 있음
region_change = region_change.dropna()

# 증감율 시각화
plt.figure(figsize=(12, 8))

for col in region_change.columns:
    plt.plot(region_change.index, region_change[col], marker='o', label=col)

plt.title('연도별 지역별 천식 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()