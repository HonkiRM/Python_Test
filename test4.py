import os
path=os.getcwd()       #定义工作路径
hash_lst=[]
a=0
b=0
for home, dirs, files in os.walk(path):
    for element in files:
        file_name=os.path.basename(element)
        file_hash=hash(path+element)
        if file_hash not in hash_lst:
            hash_lst.append(file_hash)
            a+=1
        else:
            file_name0='\\'+file_name           #给file_name前面加个\，以便调用
            print(home+file_name0)
            os.remove(home+file_name0)          #删除语句
            print(f'已删除{home+file_name0}')
            b+=1
print(f'共保存{a}个文件,共删除{b}个重复文件')
answer=input('回车键退出')