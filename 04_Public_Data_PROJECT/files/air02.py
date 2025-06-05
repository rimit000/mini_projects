import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib  # 한글 폰트 처리를 위해

# CSV 파일 읽기 (파일명 및 경로는 실제 파일에 맞게 수정)
df = pd.read_csv('Air_Pollutants & Disease.csv')

# --- 컬럼 설정 ---
# 대기오염물질 항목
air_columns = [
    "PM2.5", 
    "PM10", 
    "Nitrogen Dioxide (NO₂)", 
    "Ozone (O₃)", 
    "Sulfur Dioxide (SO₂)", 
    "Carbon Monoxide (CO)"
]
# 질환 항목
disease_columns = ["J40_bronchitis", "J44_COPD", "J45_asthma"]

# --- 전년도 대비 변화율(%) 계산 ---
# (각 항목의 변화율 = (현재값 - 전년도값) / 전년도값 * 100)
df_pct_air = df[air_columns].pct_change() * 100
df_pct_air = df_pct_air.iloc[1:].reset_index(drop=True)  # 첫 해는 NaN이므로 제거

df_pct_disease = df[disease_columns].pct_change() * 100
df_pct_disease = df_pct_disease.iloc[1:].reset_index(drop=True)

# --- x축: 연도 전환 구간 생성 ---
years = df['YEAR'].tolist()  # 예: [2017, 2018, 2019, 2020, 2021, 2022, 2023]
transitions = [f"{years[i]}-{years[i+1]}" for i in range(len(years)-1)]
x = np.arange(len(transitions))  # x축 위치 (0, 1, 2, ..., len(transitions)-1)

# --- Plot 설정 ---
plt.figure(figsize=(14, 8))

# 1. 대기오염물질: 그룹화된 Next Period 스타일 막대그래프
num_air = len(air_columns)
group_width = 0.8          # 그룹 전체 너비
bar_width = group_width / num_air  # 각 막대의 너비
# 각 막대를 x 위치 기준으로 좌우로 분산시키기 위한 offset 계산
offsets = np.linspace(-group_width/2 + bar_width/2, group_width/2 - bar_width/2, num_air)

# 대기오염물질용 색상 (원하는대로 조정)
air_colors = ['lawngreen','forestgreen','mediumspringgreen','mediumturquoise','deepskyblue','slateblue']

for i, col in enumerate(air_columns):
    values = df_pct_air[col].tolist()  # 해당 항목의 변화율 값 (길이 = len(transitions))
    positions = x + offsets[i]         # 그룹 내 각 막대의 x 위치
    bars = plt.bar(positions, values, width=bar_width, color=air_colors[i],
                   edgecolor='black', label=f"{col} 변화율 (air)")
    # 각 막대 위에 값 텍스트 표시
    for pos, val in zip(positions, values):
        plt.text(pos, val, f"{val:.1f}%", ha='center', va='bottom' if val >= 0 else 'top', fontsize=8)

# 2. 질환: 선 그래프로 표시 (각 항목 별로 다른 마커와 색상)
disease_markers = ['o', 's', 'D']
disease_colors = ['peru','tomato','darkorange']

for i, col in enumerate(disease_columns):
    values = df_pct_disease[col].tolist()
    plt.plot(x, values, marker=disease_markers[i], color=disease_colors[i],
             linestyle='-', linewidth=2, markersize=8, label=f"{col} 변화율 (disease)")
    # 각 데이터 포인트 위에 값 텍스트 표시
    for xi, val in zip(x, values):
        plt.text(xi, val, f"{val:.1f}%", ha='center', va='bottom' if val >= 0 else 'top', fontsize=12, fontweight='bold')

# 0 기준선 그리기
plt.axhline(0, color='black', linewidth=0.8)

# x축 눈금 및 라벨 설정
plt.xticks(x, transitions, fontsize=10)
plt.xlabel("연도", fontsize=12)
plt.ylabel("변화율 (%)", fontsize=12)
plt.title("대기오염물질 & 질병 증감율 (NextPeriod & Line Graph)", fontsize=14)
plt.legend(fontsize=9, loc='best')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()