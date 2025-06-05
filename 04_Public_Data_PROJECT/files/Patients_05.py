import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 3개의 질병에 대한 연령별 자료
# J40 : 기관지염    bronchitis  (급성인지 만성인지 명시되지 않은 기관지염)
# J44 : 만성폐질환  COPD         Chronic obstructive pulmonary disease (기타 만성 폐색성 폐질환)
# J45 : 천식        asthma

## 1-1. 기관지염 연령대별 데이터 시각화
J40_bronchitis_age=pd.read_csv('J40_bronchitis_age.csv')

plt.figure(figsize=(10,6))

# (연령별 색상 지정)
colors = {
    '0_19세': 'cornflowerblue',
    '20_39세': 'mediumseagreen',
    '40_59세': 'goldenrod',
    '60세 이상': 'indianred'
} 


for J40_age_graph in J40_bronchitis_age.columns[1:]:
    plt.plot(J40_bronchitis_age['심사년도'], J40_bronchitis_age[J40_age_graph], marker='o', label=J40_age_graph, color=colors.get(J40_age_graph, 'black'))
    
plt.title('연령대별 기관지염(J40) 추이')
plt.xlabel('연도')
plt.ylabel('환자수')
plt.legend(title='연령대')
plt.grid(True)
plt.show()


## 1-2. 만성폐질환 연령대별 데이터 시각화
J44_COPD_age=pd.read_csv('J44_COPD_age.csv')

plt.figure(figsize=(10,6))

for J44_age_graph in J44_COPD_age.columns[1:]:
    plt.plot(J44_COPD_age['심사년도'], J44_COPD_age[J44_age_graph], marker='o', label=J44_age_graph, color=colors.get(J44_age_graph, 'black'))
    
plt.title('연령대별 만성 폐색성 폐질환(J44) 추이')
plt.xlabel('연도')
plt.ylabel('환자수')
plt.legend(title='연령대')
plt.grid(True)
plt.show()


## 1-3. 천식 연령대별 데이터 시각화
J45_asthma_age=pd.read_csv('J45_asthma_age.csv')

plt.figure(figsize=(10,6))

for J45_age_graph in J45_asthma_age.columns[1:]:
    plt.plot(J45_asthma_age['심사년도'], J45_asthma_age[J45_age_graph], marker='o', label=J45_age_graph, color=colors.get(J45_age_graph, 'black'))
    
plt.title('연령대별 천식(J45) 추이')
plt.xlabel('연도')
plt.ylabel('환자수')
plt.legend(title='연령대')
plt.grid(True)
plt.show()



## 2. 연도별 증감율 데이터 시각화

## 2-1. 기관지염 증감율
J40_bronchitis_age = J40_bronchitis_age.sort_values('심사년도').set_index('심사년도')

J40_change=J40_bronchitis_age.pct_change()*100

J40_change = J40_change.dropna()

plt.figure(figsize=(12, 8))

for J40_change_graph in J40_change.columns:
    plt.plot(J40_change.index, J40_change[J40_change_graph], marker='o', label=J40_change_graph, color=colors.get(J40_change_graph, 'black'))

plt.title('연령별 기관지염(J40) 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


## 2-2. 만성폐질환 증감율
J44_COPD_age = J44_COPD_age.sort_values('심사년도').set_index('심사년도')

J44_change=J44_COPD_age.pct_change()*100

J44_change = J44_change.dropna()

plt.figure(figsize=(12, 8))

for J44_change_graph in J44_change.columns:
    plt.plot(J44_change.index, J44_change[J44_change_graph], marker='o', label=J44_change_graph, color=colors.get(J44_change_graph, 'black'))

plt.title('연령별 만성 폐색성 폐질환(J44) 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


## 2-3. 천식 증감율
J45_asthma_age = J45_asthma_age.sort_values('심사년도').set_index('심사년도')

J45_change=J45_asthma_age.pct_change()*100

J45_change = J45_change.dropna()

plt.figure(figsize=(12, 8))

for J45_change_graph in J45_change.columns:
    plt.plot(J45_change.index, J45_change[J45_change_graph], marker='o', label=J45_change_graph, color=colors.get(J45_change_graph, 'black'))

plt.title('연령별 천식(J45) 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='지역', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


## ---------------------------------------------------
## 3. 대기오염물질과 질병 증감율 비교
## ---------------------------------------------------

Air_Pollutants=pd.read_excel('Air_Pollutants.xlsx')

Air_Pollutants.to_csv('Air_Pollutants.csv', index=False, encoding='utf-8-sig')


disease_colors = {
    'PM2.5': 'lawngreen',
    'PM10': 'forestgreen',
    'Nitrogen Dioxide (NO₂)': 'mediumspringgreen',
    'Ozone (O₃)': 'mediumturquoise',
    'Sulfur Dioxide (SO₂)': 'deepskyblue',
    'Carbon Monoxide (CO)': 'slateblue',
    'J40_bronchitis': 'peru',
    'J44_COPD': 'tomato',
    'J45_asthma': 'darkorange'
} 


## 3-1. 대기오염물질 증감율
Air_Pollutants = Air_Pollutants.sort_values('YEAR').set_index('YEAR')

Air_Change=Air_Pollutants.pct_change()*100

Air_Change = Air_Change.dropna()

plt.figure(figsize=(12, 8))

for Air_Change_graph in Air_Change.columns:
    plt.plot(Air_Change.index, Air_Change[Air_Change_graph], marker='o', label=Air_Change_graph, color=disease_colors.get(Air_Change_graph, 'black'))

plt.title('대기오염물질 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='오염물질', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

## 3-2. 대기오염물질과 질병 증감율

Air_Pollutants_AND_Disease=pd.read_excel('Air_Pollutants & Disease.xlsx')

Air_Pollutants_AND_Disease.to_csv('Air_Pollutants & Disease.csv', index=False, encoding='utf-8-sig')


Air_Pollutants_AND_Disease = Air_Pollutants_AND_Disease.sort_values('YEAR').set_index('YEAR')

Air_Dis_Change=Air_Pollutants_AND_Disease.pct_change()*100

Air_Dis_Change = Air_Dis_Change.dropna()

plt.figure(figsize=(12, 8))


for Air_Dis_Change_graph in Air_Dis_Change.columns:
    plt.plot(Air_Dis_Change.index, Air_Dis_Change[Air_Dis_Change_graph], marker='o', label=Air_Dis_Change_graph, color=disease_colors.get(Air_Dis_Change_graph, 'black'))

plt.title('대기오염물질 & 질병 증감율')
plt.xlabel('연도')
plt.ylabel('증감율 (%)')
plt.legend(title='오염물질', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


