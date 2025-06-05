from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창 없이 실행 (옵션)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 크롬 드라이버 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 웹사이트 접속
url = "https://m.work24.go.kr/hr/a/a/1100/trnnCrsInf2.do?dghtSe=A&traingMthCd=A&tracseTme=5&endDate=20260222&keyword1=&keyword2=&pageSize=10&orderBy=ASC&startDate_datepicker=2020-01-01&currentTab=1&topMenuYn=&pop=&tracseId=AIG20220000366804&pageRow=100&totamtSuptYn=A&keywordTrngNm=&crseTracseSeNum=&keywordType=1&gb=&keyword=&kDgtlYn=&area=00%7C%EC%A0%84%EA%B5%AD+%EC%A0%84%EC%B2%B4%2C00%7C%EC%A0%84%EA%B5%AD+%EC%A0%84%EC%B2%B4&orderKey=2&mberSe=&kdgLinkYn=&srchType=all_type&crseTracseSe=A%7C%EB%94%94%EC%A7%80%ED%84%B8%EC%8B%A0%EA%B8%B0%EC%88%A0%EB%B6%84%EC%95%BC+%EC%A0%84%EC%B2%B4%2CA%7C%EB%94%94%EC%A7%80%ED%84%B8%EC%8B%A0%EA%B8%B0%EC%88%A0%EB%B6%84%EC%95%BC+%EC%A0%84%EC%B2%B4&tranRegister=&mberId=&i2=A&pageId=6&programMenuIdentification=EBG020000000313&crseTracseSeKDT=kdgtal_tgcr_yn%7CK-%EB%94%94%EC%A7%80%ED%84%B8%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D%2Ckdgtal_tgcr_yn%7CK-%EB%94%94%EC%A7%80%ED%84%B8%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%8B%9D&endDate_datepicker=2026-02-22&monthGubun=&pageOrder=2ASC&pageIndex=1&bgrlInstYn=&startDate=20200101&ncs=&gvrnInstt=&selectNCSKeyword=&action=trnnCrsInf2Post.do"
driver.get(url)

# 페이지 로딩 대기
time.sleep(2)

# 크롤링 데이터 저장 리스트
data_list = []

# 최대 페이지 크롤링 (예: 5페이지까지)
max_pages = 10

for page in range(1, max_pages + 1):
    print(f"\n🔹 페이지 {page} 결과:")

    # 1. 훈련과정명 가져오기
    course_elements = driver.find_elements(By.CSS_SELECTOR, "h3.b1_sb")

    # 2. 훈련기관명 가져오기
    course_academy = driver.find_elements(By.CSS_SELECTOR, "h3.t3_sb")

    # 3. 훈련기간 가져오기
    course_duration = driver.find_elements(By.XPATH, "//p[@class='info']/span[contains(text(), '202')]")

    # 4. 훈련비용 가져오기
    course_price = driver.find_elements(By.CSS_SELECTOR, "p.b1_sb.mt08")
    
    # 5. 취업률
    course_percent = driver.find_elements(By.CSS_SELECTOR, "em.txt")

    # 리스트 길이 맞추기 (최소 길이에 맞춤)
    min_length = min(len(course_elements), len(course_academy), len(course_duration), len(course_price), len(course_percent))

    # 모든 데이터를 반복문을 사용하여 가져오기
    for idx in range(min_length):
        course_name = course_elements[idx].text.strip() if idx < len(course_elements) else "정보 없음"
        academy_name = course_academy[idx].text.strip() if idx < len(course_academy) else "정보 없음"
        duration = course_duration[idx].text.strip() if idx < len(course_duration) else "정보 없음"
        price = course_price[idx].text.strip() if idx < len(course_price) else "정보 없음"
        percent = course_percent[idx].text.strip() if idx < len(course_percent) else "정보 없음"

        print(f"  🔹 훈련기관: {academy_name}")
        print(f"  🔹 훈련과정: {course_name}")
        print(f"  🔹 훈련기간: {duration}")
        print(f"  🔹 훈련비용: {price}")
        print(f"  🔹 취업률: {percent}")
        print("-" * 50)

        # 리스트에 저장
        data_list.append([academy_name, course_name, duration, price, percent])

    # 다음 페이지 버튼 클릭 (마지막 페이지일 경우 중지)
    try:
        next_button = driver.find_element(By.XPATH, f"//button[@onclick='fn_search({page+1}); return false;']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(2)  # 페이지 이동 후 로딩 대기
    except:
        print("🚨 다음 페이지 버튼을 찾을 수 없습니다. 크롤링 종료")
        break

# 데이터프레임 생성
df = pd.DataFrame(data_list, columns=["훈련기관", "훈련과정", "훈련기간", "훈련비용", "취업률"])

# 엑셀 파일로 저장
file_path = "훈련과정_크롤링dd.xlsx"
df.to_excel(file_path, index=False)

print(f"✅ 엑셀 저장 완료: {file_path}")

# 크롤링 완료 후 브라우저 닫기
driver.quit()
