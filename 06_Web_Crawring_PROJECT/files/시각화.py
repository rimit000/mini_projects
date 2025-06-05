import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 정의
years = [2022, 2023, 2024, 2025]
values = [328, 114, 139, 389]

# 그래프 크기 설정
plt.figure(figsize=(8, 5))

# 막대 그래프 그리기
plt.bar(years, values, color='skyblue', edgecolor='black')

# 제목 및 라벨 설정
plt.title("KDT 연도별 과정 개수 추이", fontsize=14, fontweight='bold')
plt.xlabel("연도", fontsize=12)
plt.ylabel("과정 개수", fontsize=12)

# 값 표시
for i, v in enumerate(values):
    plt.text(years[i], v + 10, str(v), ha='center', fontsize=11, fontweight='bold')

# x축, y축 눈금 설정
plt.xticks(years, fontsize=11)
plt.yticks(fontsize=11)

# 그리드 추가 (y축 기준, 점선 스타일)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 그래프 출력
plt.show()
