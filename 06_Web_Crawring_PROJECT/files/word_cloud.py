from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import re
from konlpy.tag import Okt
import matplotlib.font_manager as fm

# 엑셀 파일 불러오기
file_path = "훈련과정_크롤링.xlsx"
df = pd.read_excel(file_path)

# '훈련과정' 열에서 텍스트 데이터 추출
text_data = " ".join(df["훈련과정"].astype(str))

# 특수문자 및 불필요한 문자 제거
text_data = re.sub(r"[^가-힣a-zA-Z0-9\s]", "", text_data)

# 형태소 분석기 초기화
okt = Okt()

# 명사 추출
nouns = okt.nouns(text_data)

# 불용어 리스트 적용
stopwords = {"과정", "양성", "활용", "개발", "개발자", "기반", "프로젝트", "서비스", "콘텐츠", "융합", "부트캠프", "심화"}
filtered_nouns = [word for word in nouns if word not in stopwords]

# 단어 빈도수 계산
word_counts = Counter(filtered_nouns)

# 한글 폰트 설정
fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
korean_font = next((font for font in fonts if "NanumGothic" in font), fonts[0])

# 워드클라우드 생성
wordcloud = WordCloud(
    font_path=korean_font,  # 한글 폰트 경로
    background_color="white",
    width=800,
    height=400
).generate_from_frequencies(word_counts)

# 워드클라우드 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
