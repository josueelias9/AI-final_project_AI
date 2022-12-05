
import os
import shutil 

'''
params
------
abs_path: path of directory

return
------
returns amount of elements in directory
'''
def count_elements(abs_path):
    if len(os.listdir(abs_path)) == 0:
        return 0
    else:
        count= None
        for count,i in enumerate(os.listdir(abs_path)):
            pass
        return count +1 


'''
Enters to each folter inside of path an prints
how many elements are inside it.
'''
def recursivo(path):

    # iterate over eache element inside "path"
    for i in os.listdir(abs_path):
        join_path = os.path.join(path,i)
        try:
            a = count_elements(join_path)
            print(join_path+"\t"+str(a))
        except Exception as e:
            print(e)


'''
this function search all directories that match the string that you passed as 
argument and copy it to the destination directory

param
-----
name: string that you want to match
ruta: '/data/josue_2/data_orginal_data/images'
dest: '/data/josue_2/josue_x/data/prod_data/4_filters/input'
'''
def search_match_and_copy(name,ruta,dest):

    count = 0
    for count, i in enumerate(os.listdir(ruta)):
        try:

            if name in i:
                a = os.path.join(ruta,i)
                b = os.path.join(dest,i)
                shutil.copytree(a, b) 
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("asdasdasdas")

    abs_path = '/data/filtering/data/test_data/4_filters/output'
    recursivo(abs_path)

