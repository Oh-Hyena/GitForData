"""
1. img_dir_path에서 하위 디렉터리까지 탐색하면서, 전체 이미지의 filename과 img_dir_path를 img_dictionary에 넣기
2. img_list를 탐색하면서, img_list의 img_dir_path와 filename을 copy_list에 넣기 (copy_list[0]=img_dir_path, copy_list[1]=filename)
3. copy_list를 탐색하면서, img_dir_path에서 save_path(copy_dir_path + copy_list의 filename)으로 복사하기
"""


import os
import shutil
import cv2


targetDir = r"C:\Users\user\Desktop\test\copy\origin_img"
annotationFilePath = r"C:\Users\user\Desktop\test\copy\imglist_annotation\annotation.txt"
imgListFilePath = r"C:\Users\user\Desktop\test\copy\imglist_annotation\img_list.txt"
resultDir = r"C:\Users\user\Desktop\test\copy\copy_img"


# targetDir 하위디렉토리까지 탐색하면서 있는 이미지들 dict 에 넣기
# 원본 img의 하위 디렉터리까지 탐색하면서, 전체 이미지의 filname과 원본 img의 경로를 dictionary에 넣기
OriginImgDict = {}
for root, dirs, files in os.walk(targetDir):
    for file in files:
        # key=filename / value=targetDir(total_img_dir)
        OriginImgDict[file] = root


# 복사하고싶은 이미지 리스트들의 txt
# img_list의 텍스트 파일을 list에 append하기
imgNameList = []
with open(imgListFilePath, 'r', encoding='utf8') as f:
    for eachLine in f:
        eachLine = eachLine.strip('\n')
        imgNameList.append(eachLine)


# 찾아서 imgNameList에 있는 이미지들만 복사하기
# list를 돌리면서, 원본 img의 경로+filename과 복사할 filename을 copyList에 append하기
copyList = []
for eachImg in imgNameList:
    # dictionay.get(key)/dictionay[key] : key 값으로 value 얻기(filename 값으로 root 얻기)
    validRoot = OriginImgDict.get(eachImg)
    if validRoot is not None:
        # copyList.append([복사 대상 경로(root+filename), 복사할 이름(filename)])
        copyList.append([os.path.join(OriginImgDict[eachImg], eachImg), eachImg])


COPY_PATH = 0
COPY_NAME = 1


# 복사하기
# copyList를 돌리면서, 원본 img 경로에서 저장할 경로+filename로 복사하기
for eachCopyImg in copyList:
    # savePath = 저장경로 + copyList[1]인 filename
    savePath = os.path.join(resultDir, eachCopyImg[COPY_NAME])
    # copyList[0]인 원본 img 경로에서 savePath로 복사하기
    try:
        shutil.copy(eachCopyImg[COPY_PATH], savePath)
    except Exception as e:
        print(e)


# annotation.txt 파일 복사하기
shutil.copy(annotationFilePath, resultDir)

# img_list.txt 파일에 경로 추가하기
imgFileNameList = []
with open(imgListFilePath, 'r', encoding='utf8') as f:
    for eachLine in f:
        eachLine = eachLine.strip('\n')
        imgFileNameList.append(os.path.join(resultDir, eachLine))

# resultPath = os.path.join(resultDir, "ConditionFilter_ImgList.txt")
resultPath = os.path.join(resultDir, os.path.basename(imgListFilePath))
print(resultPath)
with open(resultPath, 'w', encoding='utf8') as f:
    for eachLine in imgFileNameList:
        f.write(f"{eachLine}\n")

