import os
import shutil

targetDir = r'C:\Users\user\Desktop\test\move5\origin_img'
imgListFilePath = r'C:\Users\user\Desktop\test\move5\img_list.txt'
resultMoveDir = r'C:\Users\user\Desktop\test\move5\move_img'
resultAddPath_FilePath = r'C:\Users\user\Desktop\test\move5\move_img\add_path_img_list.txt'


OriginalDict = {}
for root, dirs, files in os.walk(targetDir):
    for file in files:
        OriginalDict[file] = root


dictList = []
for k in list(OriginalDict.keys()):
    dictList.append(k)


nameList = []
with open(imgListFilePath, 'r', encoding='utf8') as f:
    for each in f:
        each = each.strip('\n')
        nameList.append(each)
        each2 = each.split('.')[0]
        each2 = each2 + '.txt'
        nameList.append(each2)


addPathList = []
moveList = []
for each in nameList:
    validRoot = OriginalDict.get(each)
    if validRoot is not None:
        moveList.append([os.path.join(validRoot, each), each])

        if each.split('.')[1] != 'txt':
            addPathList.append(os.path.join(validRoot, each))


for each in moveList:
    # each[0] = move 할 img&txt 경로 / each[1] = move 할 img&txt 파일 이름
    savePath = os.path.join(resultMoveDir, each[1])
    try:
        shutil.move(each[0], savePath)
    except Exception as e:
        print("move error : ", e)


with open(resultAddPath_FilePath, 'w', encoding='utf8') as f:
    for each in addPathList:
        f.write(f"{each}\n")


            


