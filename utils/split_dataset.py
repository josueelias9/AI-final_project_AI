
# import required module
import os
import shutil



def delete_structure(DIR_DEST):   
    if os.path.exists(DIR_DEST):
        shutil.rmtree(DIR_DEST)


'''
|-- como_dan
    |-- class_1
    |-- class_2
    |-- ...
'''
def create_structure(DIR_ORIG,DIR_DEST):
    # get absolute path
    abs_path = os.getcwd()

    # defining paths
    como_dan_path = DIR_ORIG
    como_debe_ser_path = DIR_DEST
    validation_path = os.path.join(como_debe_ser_path, 'validation')
    train_path = os.path.join(como_debe_ser_path, 'train')

    # create main structure
    #
    # |-- como_debe_ser
    #     |-- validation
    #     |-- train
    if not os.path.exists(como_debe_ser_path):
        os.mkdir(como_debe_ser_path)
    if not os.path.exists(validation_path):
        os.mkdir(validation_path)
    if not os.path.exists(train_path):
        os.mkdir(train_path)


    # start coping folders 
    for i in os.listdir(como_debe_ser_path):
        for j in os.listdir(como_dan_path):
            aux_path = os.path.join(como_debe_ser_path, i,j)
            if not os.path.exists(aux_path):
                os.mkdir(aux_path)



def split_dataset(DIR_ORIG,DIR_DEST,percentage):
    # rutas padres
    como_dan_path = DIR_ORIG  
    como_debe_ser_path = DIR_DEST 

    # tamaño del validation
    porcentaje = percentage

    # se itera por cada clase
    for each_class_name in os.listdir(como_dan_path):

        # todo lo que viene hasta el final es para una sola clase (<clase>)
        each_class_path = como_dan_path + '/' + each_class_name

        # total de archivos que hay en la carpeta <clase>
        each_class_num_archivos = len([entry for entry in os.listdir(
            each_class_path) if os.path.isfile(os.path.join(each_class_path, entry))])

        # definimos el numero de elementos que debe tener la carpeta "como_debe_ser/validation/<clase>"
        each_class_num_validation = round(each_class_num_archivos * porcentaje / 100)

        # repartimos los archivos
        for count, given_file_name in enumerate(os.listdir(each_class_path)):
            given_file_path = each_class_path + '/' + given_file_name

            # se envia a la carpeta <clase>/validation/ el porcentaje de archivos que corresponda
            if(count +1 <= each_class_num_validation):
                destination = os.path.join(como_debe_ser_path ,'validation', each_class_name)
                # os.popen('cp ' + given_file_path + ' ' + destination)
                shutil.copy (given_file_path, destination)

            # los demas archivos se envian a la carpeta <clase>/train/
            else:
                destination = os.path.join(como_debe_ser_path,'train' , each_class_name)
                # os.popen('cp ' + given_file_path + ' ' + destination)
                shutil.copy(given_file_path, destination)


if __name__ == '__main__':

    DIR_ORIG = '/tf/josue/data/prod_data/4_filters/output_200_test'
    DIR_DEST = '/tf/josue/data/prod_data/5_train_final_model/input'
    percentage = 20


    try:
        delete_structure(DIR_DEST)
        create_structure(DIR_ORIG,DIR_DEST)
        split_dataset(DIR_ORIG,DIR_DEST,percentage)
    except Exception as e:
        print("something wrong happened")
        print(e)
