import os
import json
import requests
from urllib import parse
from datetime import datetime

# 로그 파일 작성 함수
def log_message(message):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_folder = "D:\\Data\\MarketAnalysis\\DNF\\PC_Token\\Log"
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, "data_log.txt")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"{log_time} : {message}\n")

# API 결과를 JSON 형태로 반환하는 함수
def get_api_data():
    get_param = {
        'itemName': 'pc방',      # 필요에 따라 올바른 아이템명을 입력하세요.
        'wordType': 'front',
        'wordShort': '<wordShort>',
        'limit': 100,
        'apikey': 'wxcTpDcvx4gWL4kSB8JRJy6b6tb04rq5'
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.neople.co.kr/df/auction-sold?%s" % (get_param)
    print(url)

    response = requests.get(url)  # GET 요청

    # API 응답을 JSON 객체로 변환
    data = response.json()

    # 응답 데이터 중, 결과가 {"rows": [ ... ]} 형식으로 담겨 있는 경우 해당 부분만 추출하여 반환합니다.
    result = data.get("rows", [])
    # 또는 응답 데이터가 바로 배열 형태로 반환되는 경우 data 그대로 사용합니다.
    # result = data  # 응답 데이터가 배열인 경우

    # result를 그대로 JSON 객체(리스트) 형태로 반환합니다.
    return result

# API를 통해 데이터 조회
data = get_api_data()

if data is not None:
    # 현재 시간을 'YYYYMMDD_HHMMSS' 형식으로 추출
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    # folder_name = f"D:\\Data\\MarketAnalysis\\DNF\\PC_Token\\{current_time}"
    folder_name = "D:\\Data\\MarketAnalysis\\DNF\\PC_Token\\Data"
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, f"{current_time}_data.txt")
    
    # JSON 형태로 저장 (한글이 깨지지 않도록 ensure_ascii=False)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"데이터가 '{file_path}'에 저장되었습니다.")
    log_message("Data Save Success!")
else:
    print("API 데이터 조회 실패")
    log_message("Data Save Fail!")
