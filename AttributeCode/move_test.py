import os
import shutil


targetDir = r'C:\Users\user\Desktop\test\move4\origin_img'
imgListFilePath = r'C:\Users\user\Desktop\test\move4\img_list.txt'
resultMoveDir = r'C:\Users\user\Desktop\test\move4\move_img'
resultAddPath_FilePath = r'C:\Users\user\Desktop\test\move4\move_img\add_path_img_list.txt'


OriginalDict = {}
for root, dirs, files in os.walk(targetDir):
    for file in files:
        OriginalDict[file] = root


dictList = []
for k in list(OriginalDict.keys()):
    dictList.append(k)


fileNameList = []
with open(imgListFilePath, 'r', encoding='utf8') as f:
    for eachLine in f:
        # imgListFilePath 에서 img 파일 append 하기
        eachLine = eachLine.strip('\n')
        fileNameList.append(eachLine)
        # imgListFilePath 에서 txt 파일로 변환 후 append 하기
        eachLine2 = eachLine.split('.')[0]
        eachLine2 = eachLine2 + '.txt'
        fileNameList.append(eachLine2)


addPathList = []
moveList = []
for each in fileNameList: 

    validRoot = OriginalDict.get(each)
    if validRoot is not None:
        # moveImgList -> imt&txt 와 img&txt 가 있는 경로 append
        moveList.append([os.path.join(validRoot, each), each])

        if each.split('.')[1] == 'txt':
            continue

        # addPathList -> 이미지가 있는 경로만 append
        addPathList.append(os.path.join(validRoot, each))


for eachMove in moveList:
    # eachMove[0] -> move 할 img&txt 의 경로 / eachMove[1] -> move 할 img&txt 의 이름 
    savePath = os.path.join(resultMoveDir, eachMove[1])
    try:
        shutil.move(eachMove[0], savePath)
    except Exception as e:
        print(e)


with open(resultAddPath_FilePath, 'w', encoding='utf8') as f:
    for each in addPathList:
        f.write(f"{each}\n")