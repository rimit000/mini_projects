import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

# 총 6개 파일 : 3개의 질병에 대한 연령별, 지역별 자료
# J40 : 기관지염 bronchitis (급성인지 만성인지 명시되지 않은 기관지염)
# J44 : 만성폐질환 COPD Chronic obstructive pulmonary disease (기타 만성 폐색성 폐질환)
# J45 : 천식 asthma

J40_age=pd.read_excel('J40_기관지염_2017-2022_연령별.xlsx')
J44_age=pd.read_excel('J44_만성폐질환_2017-2022_연령별.xlsx')
J45_age=pd.read_excel('J45_천식_2017-2022_연령별.xlsx')
J40_loc=pd.read_excel('J40_기관지염_2017-2022_지역별.xlsx')
J44_loc=pd.read_excel('J44_만성폐질환_2017-2022_지역별.xlsx')
J45_loc=pd.read_excel('J45_천식_2017-2022_지역별.xlsx')

J40_age.to_csv('J40_bronchitis_age.csv', index=False, encoding='utf-8-sig')
J44_age.to_csv('J44_COPD_age.csv', index=False, encoding='utf-8-sig')
J45_age.to_csv('J45_asthma_age.csv', index=False, encoding='utf-8-sig')
J40_loc.to_csv('J40_bronchitis_location.csv', index=False, encoding='utf-8-sig')
J44_loc.to_csv('J44_COPD_location.csv', index=False, encoding='utf-8-sig')
J45_loc.to_csv('J45_asthma_location.csv', index=False, encoding='utf-8-sig')