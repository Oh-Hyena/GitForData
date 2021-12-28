src = r'H:\39class_attribute_dataset\1st_version\train\dataset\valid\val_merge_annotation.txt'

dist_file = r'H:\39class_attribute_dataset\1st_version\train\dataset\valid\val_merge_annotation_18.txt'
dist = []
for line in open(src):
    label = line.strip()
    #print(label)
    temp = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(label[17], label[18], label[19], label[20], label[21], label[22], label[23], label[24], label[25], label[30], label[31], label[32], label[33], label[34], label[35], label[36], label[37], label[38])
    dist.append(temp)
textfile = open(dist_file,'w')
for list in dist:
    # print(list)
    textfile.write(list+'\n')
textfile.close()