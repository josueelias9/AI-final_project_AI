## -- folder structure
data terminology:
- __training__: The data or algorithm that were used to train a model.
- __inference__: The data or algorithm that were used to predict a result.
```
|-- filtering
    |-- AWS                                 (scripts to create the needed infraestructure in AWS)
    |-- data                                (all data needed for the project)
        |-- prod_data                       (data for production)    
            |-- 2_filter_3_mobilenet_train  (filter 3: data needed for training)
                |-- input                   (input data for training the MobileNetV2 model)
            |-- 4_filters                   (all filters concatenated)
                |-- input                   (input data that will pass trough all the filters)
                |-- output_100              (output data. Considers only 100 images per directory)
                |-- output_200              (output data. Considers only 200 images per directory)
                |-- output_200_test         (data that will be used to train the final model)
            |-- 5_final_model_train         (final model: data needed for training)
                |-- input                   (input data for training the DenseNet121 model)
        |-- test_data                       (data for testing)
    |-- project                             (all scripts needed for the project)
        |-- 1_filter_2                      (filter 2: inference)
        |-- 2_filter_3_mobilenet_train      (filter 3: training)
        |-- 3_filter_3_mobilenet_inference  (filter 3: inference)
        |-- 4_filters                       (all filters concatenated)
        |-- 5_final_model_train             (final model: training)
    |-- utils                               (scripts needed to do general computation)
```

## -- filter


## -- final model

carpetas de la forma
```
<branch>_<model>_<year>
```
# - test
Do not modify this folder. It is just for documentation porpuse. You will have to replate in another directory if you want your project up and running.
## -- dir: 2_filter_3_mobilenet_train
steps:
- get into the file _split_dataset.py_ and modifive the following variables:
```python
DIR_ORIG = 'como_dan'
DIR_DEST = 'result'
percentage = 20
```
- Execute and a new folder will be created.
- Execute the comand _bash tam.sh_ if you want to know how many files are in each directory created.



http://127.0.0.1:8888/tree?token=8e82b218b57002c2e8b9f2ade43e17472d8268c0f04c3473
http://127.0.0.1:8888/tree/josue

```
abarth_500
parece ser imagen tomadan dentro del carro
207_8_d348b25d-7fc1-b235-e053-e250040a3dfb_7b768ce4-8426-4642-8e0f-f6feaca06cb0.jpg
```


python3 -m unittest test_1.py