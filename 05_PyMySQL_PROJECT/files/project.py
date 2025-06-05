import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 고용노동부_예산.xlsx   employment_budget
# 채용행사및박람회.xlsx  recruitment_events

data_budget=pd.read_excel('고용노동부_예산.xlsx')
data_events=pd.read_excel('채용행사및박람회.xlsx')

data_budget.to_csv('employment_budget.csv', encoding='utf-8-sig')
data_events.to_csv('recruitment_events.csv', encoding='utf-8-sig')