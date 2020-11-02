import os
path=os.chdir('F:\pythonProject4\新建文件夹')        #定义工作路径
file_list=[]
dir_list=[]
for element in os.scandir(path):
    if element.is_dir():
        dir_list.append(element)
    else:
        file_list.append(element)
#print(file_list, dir_list, len(file_list),len(dir_list) )
print(f'文件共{len(file_list)}个，分别为{file_list}')
print(f'文件夹共{len(dir_list)}个，分别为{dir_list}')
txt_lst=[]
for item in file_list:
    item=os.path.basename(item)                     #获得文件名
#    est_name=item.endswith()
#    print(item,est_name)
    if item.endswith('.txt'):
        txt_lst.append(item)
    else:
        pass
print(txt_lst)