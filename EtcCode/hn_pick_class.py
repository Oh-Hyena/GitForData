annotationFilePath = r'C:\Users\user\Desktop\test\pick_class\annotation.txt'
saveFilePath = r'C:\Users\user\Desktop\test\pick_class\pick_class_annotation3.txt'


# 세번째 방법 때 사용
idx_list = [1, 5, 10]

annotationList = []
with open(annotationFilePath, 'r', encoding='utf8') as f:
    for each in f:
        each = each.strip('\n')

        # 첫번째 방법
        # each = each[5:10]
        # annotationList.append(each)

        # 두번째 방법
        # first  = each[5:10]
        # second = each[15:20]
        # annotationList.append(first+second)

        # 세번째 방법
        result = ""
        for eachIdx in range(len(each)):
            if eachIdx in idx_list:
                result += each[eachIdx]
        annotationList.append(result)


with open(saveFilePath, 'w', encoding='utf8') as f:
    for each in annotationList:
        f.write(f"{each}\n")
