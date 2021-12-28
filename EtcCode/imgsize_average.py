imgNameList = []
with open("3.txt", 'r', encoding='utf-8') as f:
    for eachLine in f:
        eachLine = eachLine.strip('\n')
        img = eachLine.split(" ")
        width = img[0]
        height = img[1]
        img_size = int(width) * int(height)
        imgNameList.append(img_size)

    print("11 : ", imgNameList)
    img_sum = sum(imgNameList)
    print("13 : ", img_sum)
    img_average = int(img_sum) / 95233
    print('15 : ', img_average)
