# -*- coding: cp949 -*-
import os
import json
import requests
from urllib import parse
from datetime import datetime

# �α� ���� �ۼ� �Լ�
def log_message(message):
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_folder = "D:\\Data\\atmosphere\\Rawinsonde\\logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, "data_log.txt")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"{log_time} : {message}\n")

# API�� ���� �����͸� �������� �Լ�
def get_api_data():
    get_param = {
        'itemName': 'pc��',
        'wordType': 'front',
        'wordShort': '<wordShort>',
        'limit': 100,
        'apikey': 'wxcTpDcvx4gWL4kSB8JRJy6b6tb04rq5'
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.neople.co.kr/df/auction-sold?%s" % (get_param)
    print(url)

    response = requests.get(url)  # GET ��û

    # API ������ JSON �����̶�� �����ϰ� �Ľ��մϴ�.
    data = response.json()

    # ���� ���, ���� ������ {"rows": [ ... ]} ���¶�� �Ʒ��� ���� ó���� �� �ֽ��ϴ�.
    result = data.get("rows", [])
    # ���� ������ �ֻ��� ����Ʈ��� �׳� data�� �״�� �����մϴ�.
    # result = data  # ������ ����Ʈ��� ����

    # result�� �̹� JSON ��ü(��ųʸ�)���� ���� ����Ʈ�Դϴ�.
    return result

# API�κ��� ������ ��ȸ
data = get_api_data()

if data is not None:
    # ���� �ð��� 'YYYYMMDD_HHMMSS' �������� �����Ͽ� ������ �� ���ϸ� ����
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"D:\\ta\\MarketAnalysis\\DNF\\PC_Token\\{current_time}"
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, f"{current_time}_data.txt")
    
    # JSON �����͸� ���Ͽ� ���� (�ѱ��� ������ �ʵ��� ensure_ascii=False)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"�����Ͱ� '{file_path}'�� ����Ǿ����ϴ�.")
    log_message("Data Save Success!")
else:
    print("API ������ ��ȸ ����")
    log_message("Data Save Fail!")

