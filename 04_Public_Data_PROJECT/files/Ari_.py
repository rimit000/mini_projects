import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


## 3-3. 대기오염물질 워터풀 차트(그래프)
Air_Pollutants = pd.read_csv('Air_Pollutants.csv')

# 대기오염물질 항목 리스트
pollutants = [
    "PM2.5", 
    "PM10", 
    "Nitrogen Dioxide (NO₂)", 
    "Ozone (O₃)", 
    "Sulfur Dioxide (SO₂)", 
    "Carbon Monoxide (CO)"
]

# 각 오염물질의 연도별 변화율(전년도 대비 % 변화) 계산
df_pct = Air_Pollutants[pollutants].pct_change() * 100

# 첫 해는 전년 대비 계산이 안 되므로 제거 후 인덱스 재설정
df_pct = df_pct.iloc[1:].reset_index(drop=True)

# 연도 리스트 및 전환 구간(예: "2017-2018", "2018-2019", …) 생성
years = Air_Pollutants['YEAR'].tolist()
transitions = [f"{years[i]}-{years[i+1]}" for i in range(len(years)-1)]

# 6개 오염물질에 대해 3행 2열의 서브플롯 생성
fig, axs = plt.subplots(3, 2, figsize=(15, 10))
axs = axs.flatten()  # 2차원 배열을 1차원 리스트로 변환

# 각 오염물질에 대해 Next Period 스타일 막대그래프 그리기
for i, pollutant in enumerate(pollutants):
    ax = axs[i]
    # 해당 오염물질의 전년도 대비 변화율 리스트 (길이: len(years)-1)
    pct_changes = df_pct[pollutant].tolist()
    x = list(range(len(transitions)))  # x축 위치
    
    # 변화율에 따라 색상 지정: 양수면 초록, 음수면 빨강, 0이면 파랑
    colors = ['tomato' if change > 0 else 'royalblue' if change < 0 else 'blue' for change in pct_changes]
    
    # 막대그래프 그리기
    ax.bar(x, pct_changes, color=colors, edgecolor='black')
    
    # 각 막대 위(또는 아래)에 변화율 텍스트 표시
    for j, change in enumerate(pct_changes):
        va = 'bottom' if change >= 0 else 'top'
        ax.text(x[j], change, f"{change:.2f}%", ha='center', va=va, fontsize=10)
    
    # 0 기준선 표시
    ax.axhline(0, color='black', linewidth=0.8)
    
    # 제목, 축 레이블, 눈금 설정
    ax.set_title(f"{pollutant} 증감율 (NextPeriod Graph)", fontsize=12)
    ax.set_ylabel("변화율 (%)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(transitions)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()