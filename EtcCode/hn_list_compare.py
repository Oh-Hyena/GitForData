import os

firstListPath = r'C:\Users\Unicomnet\Desktop\list_compare\first.txt'
secondListPath = r'C:\Users\Unicomnet\Desktop\list_compare\second.txt'
savePath = r'C:\Users\Unicomnet\Desktop\list_compare\compare.txt'


firstReadList = []
with open(firstListPath, 'r', encoding='utf8') as f:
    for each in f:
        each = each.strip('\n')
        firstReadList.append(each.split('.')[0])


secondReadList = []
with open(secondListPath, 'r', encoding='utf8') as f:
    for each in f:
        each = each.strip('\n')
        secondReadList.append(each.split('.')[0])


first_compare = list(set(firstReadList)-set(secondReadList))
with open(savePath, 'w', encoding='utf8') as f:
    f.write(f'{firstListPath} 에만 있는 것\n')
    for each in first_compare:
        f.write(each + '\n')


second_compare = list(set(secondReadList)-set(firstReadList))
with open(savePath, 'a', encoding='utf8') as f:
    f.write(f'\n{secondListPath} 에만 있는 것\n')
    for each in second_compare:
        f.write(each + '\n')
