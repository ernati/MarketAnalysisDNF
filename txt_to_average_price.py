import os
import json


def File_To_average_unit_price(file_path) :
    # 파일 경로 (실제 파일 경로로 수정하세요)
    # file_path = "D:\\Data\\MarketAnalysis\\DNF\\PC_Token\\Data\\20250219_233325_data.txt"

    # 텍스트 파일 읽기 및 JSON 파싱
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # data는 [ JSON1, JSON2, ... ] 형태의 리스트입니다.

    # "unitPrice" 값 합산
    total_unit_price = 0
    for item in data:
        # 각 JSON 객체에서 "unitPrice" 값을 추출 (값이 없으면 0을 반환)
        unit_price = item.get("unitPrice", 0)
        total_unit_price += unit_price
        # print("해당 데이터의 unitPrice : ", unit_price)

    # 총 100개의 JSON 데이터가 있다고 가정하면, 평균 계산
    average_unit_price = total_unit_price / len(data)

    print("평균 unitPrice:", average_unit_price)
   
def get_file_paths(directory):
    absolute_file_paths = []
    # directory 내의 항목들을 순회합니다.
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        # 파일인 경우 절대경로로 변환하여 리스트에 추가합니다.
        if os.path.isfile(full_path):
            absolute_file_paths.append(os.path.abspath(full_path))
    return absolute_file_paths

if __name__ == "__main__":
    # 사용자로부터 디렉토리 경로 입력받기
    directory = "D:\\Data\\MarketAnalysis\\DNF\\PC_Token\\Data"
    
    if os.path.isdir(directory):
        file_list = get_file_paths(directory)
    else:
        print("유효한 디렉토리 경로가 아닙니다.")
        
    for file in file_list :
        File_To_average_unit_price(file)


