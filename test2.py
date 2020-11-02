import os
import glob
import time
os.chdir('F:\pythonProject4\新建文件夹')
txt_lst=glob.glob('**/*.txt',recursive=True)
print(txt_lst)
for item in txt_lst:
    item_size=os.stat(item).st_size
    item_build_time_tuple=time.localtime(os.stat(item).st_ctime)
    item_build_time=time.strftime('%Y-%m-%d',item_build_time_tuple)
    if item_size>2 and item_build_time<'2020-12-30':
        print(f'路径：F:\pythonProject4\新建文件夹\{item},大小:{item_size}bit,创建时间:{item_build_time}')