"""
1. txt_list.txt, img_list.txt 파일을 읽어서 한 줄씩 dictionary의 key값에 넣기
2. .txt, .jpg 확장자를 기준으로 filename만 읽어오기
3. set을 이용하여 txt_list에서 img_list의 중복을 제거
"""

import os

first_list_path = r"C:\Users\user\Desktop\code\hyena\text.txt"
second_list_path = r"C:\Users\user\Desktop\code\hyena\img.txt"


def list_file_open(data):
    with open(data, 'r', encoding='euckr') as f:
        text = f.read()
        split_data = text.split()
        split_data = list(dict.fromkeys(split_data))
    
    return split_data


if __name__ == '__main__':
    first_list = list_file_open(first_list_path)
    second_list = list_file_open(second_list_path)

    first_list = [each.split('.txt')[0] for each in first_list]
    second_list = [each.split('.txt')[0] for each in second_list]

    # set = 중복 제거 함수
    print("\nfirst_list.txt에만 있는 것")
    print(list(set(first_list)-set(second_list)))

    print("\nsecond_list.txt에만 있는 것")
    print(list(set(second_list)-set(first_list)))
    print("\n")