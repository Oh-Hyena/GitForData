import os
import shutil
import glob


mergeDir = r"C:\Users\user\Desktop\test\merge\dataset"
annotaionSaveDir = r"C:\Users\user\Desktop\test\merge\annotation"
imglistSaveDir = r'C:\Users\user\Desktop\test\merge\img_list'


annotationList = []
imglistList = []
for root, dirs, files in os.walk(mergeDir):
    for file in files :
        if file.find('img_list'):
            annotationList.append([os.path.join(root, file), file])
        else:
            imglistList.append([os.path.join(root, file), file])


for idx, each in enumerate(annotationList):
    saveAnnotationPath = os.path.join(annotaionSaveDir, f"{idx+1}_{each[1]}")
    try:
        shutil.copy(each[0], os.path.join(annotaionSaveDir, f"{idx+1}_{each[1]}"))
    except Exception as e:
        print("move error : ", e)


for idx, each in enumerate(imglistList):
    saveImglistPath = os.path.join(imglistSaveDir, f"{idx+1}_{each[1]}")
    try:
        shutil.copy(each[0], os.path.join(imglistSaveDir, f"{idx+1}_{each[1]}"))
    except Exception as e:
        print("move error : ", e)


resultAnnotationPath = os.path.join(annotaionSaveDir, 'merge_annotation.txt')
readAnnotationFiles = glob.glob(os.path.join(annotaionSaveDir, '*.txt'))
with open(resultAnnotationPath, 'w', encoding='utf8') as f:
    for each in readAnnotationFiles:
        with open(each) as f2:
            for each2 in f2:
                f.write(f"{each2}\n")


resultImglistPath = os.path.join(imglistSaveDir, 'merge_img_list.txt')
readImglistFiles = glob.glob(os.path.join(imglistSaveDir, '*.txt'))
with open(resultImglistPath, 'w', encoding='utf8') as f:
    for each in readImglistFiles:
        with open(each) as f2:
            for each2 in f2:
                f.write(f"{each2}\n")
