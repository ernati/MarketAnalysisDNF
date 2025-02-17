# -*- coding: cp949 -*-
import os
import json
import requests
from urllib import parse
from datetime import datetime

# 로그 파일 작성 함수
def log_message(message):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_folder = "D:\\Data\\atmosphere\\Rawinsonde\\logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, "data_log.txt")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"{log_time} : {message}\n")

# API를 통해 데이터를 가져오는 함수
def get_api_data():
    get_param = {
        'itemName': 'pc방',
        'wordType': 'front',
        'wordShort': '<wordShort>',
        'limit': 100,
        'apikey': 'wxcTpDcvx4gWL4kSB8JRJy6b6tb04rq5'
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.neople.co.kr/df/auction-sold?%s" % (get_param)
    print(url)

    response = requests.get(url)  # GET 요청

    # API 응답이 JSON 형식이라고 가정하고 파싱합니다.
    data = response.json()

    # 예를 들어, 응답 구조가 {"rows": [ ... ]} 형태라면 아래와 같이 처리할 수 있습니다.
    result = data.get("rows", [])
    # 만약 응답이 최상위 리스트라면 그냥 data를 그대로 리턴합니다.
    # result = data  # 응답이 리스트라고 가정

    # result는 이미 JSON 객체(딕셔너리)들을 담은 리스트입니다.
    return result

# API로부터 데이터 조회
data = get_api_data()

if data is not None:
    # 현재 시간을 'YYYYMMDD_HHMMSS' 형식으로 추출하여 폴더명 및 파일명 생성
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"D:\\ta\\MarketAnalysis\\DNF\\PC_Token\\{current_time}"
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, f"{current_time}_data.txt")
    
    # JSON 데이터를 파일에 저장 (한글이 깨지지 않도록 ensure_ascii=False)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"데이터가 '{file_path}'에 저장되었습니다.")
    log_message("Data Save Success!")
else:
    print("API 데이터 조회 실패")
    log_message("Data Save Fail!")

