import os
import glob
import time
import shutil
path = 'F:\pythonProject4\新建文件夹'
os.chdir(path)
search_lst=glob.glob('**/钓鱼攻略*',recursive=True)
copy_pyth = 'F:\pythonProject4\修改后'
print(search_lst)
for item in search_lst:
    print(item)
    item_build_time_tuple=time.localtime(os.stat(item).st_ctime)
    item_build_time=time.strftime('%Y-%m-%d',item_build_time_tuple)
    shutil.copy2(path+'\\'+item,copy_pyth+'\\'+item_build_time+item)