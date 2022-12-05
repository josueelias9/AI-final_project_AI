import unittest
from amount_of_images import count_elements,search_match_and_copy
from split_dataset import delete_structure, create_structure, split_dataset

class TestUtilsMethods(unittest.TestCase):

    @unittest.skip("skip this test")
    def test_search_match_and_copy(self):
        import os
        import shutil
    
        actual_dir = os.getcwd()
        mi_dir = os.path.join(actual_dir,'copy_here')
    
        if os.path.exists(mi_dir):
            shutil.rmtree(mi_dir, ignore_errors=True)
        os.mkdir(mi_dir)
 
        name= 'spider'
        ruta= '/data/filtering/data/test_data/4_filters/input/'
        search_match_and_copy(name,ruta,mi_dir)
 

        count = 0
        for count, i in enumerate(os.listdir(ruta)):
            a= name in i
            self.assertTrue(a)

        self.assertEqual(2, count+1)


        shutil.rmtree(mi_dir, ignore_errors=True)



    @unittest.skip("skip this test")
    def test_count_elements(self):
        a = count_elements('/data/filtering/data/test_data/5_train_final_model')
        self.assertEqual(a,0)
        a = count_elements('/data/filtering/data/test_data/2_filter_3_mobilenet_train/input/inside')
        self.assertEqual(a,10)
        a = count_elements('/data/filtering/data/test_data/2_filter_3_mobilenet_train/output/validation/inside')
        self.assertEqual(a,2)

    def test_uno(self):
        import os
    
        DIR_ORIG = '/data/filtering/data/test_data/2_filter_3_mobilenet_train/input'
        DIR_DEST = '/data/filtering/data/test_data/2_filter_3_mobilenet_train/output'
        percentage = 20

        delete_structure(DIR_DEST)
        create_structure(DIR_ORIG,DIR_DEST)
        split_dataset(DIR_ORIG,DIR_DEST,percentage)

        self.assertTrue(os.path.exists(os.path.join(DIR_DEST,'train')))
        self.assertTrue(os.path.exists(os.path.join(DIR_DEST,'validation')))

        for i in os.listdir(os.path.join(DIR_DEST,'train')):
            flag = False
            for j in os.listdir(DIR_ORIG):
                if i == j:
                    flag = True
            self.assertTrue(flag)
                
        for i in os.listdir(os.path.join(DIR_DEST,'validation')):
            flag = False
            for j in os.listdir(DIR_ORIG):
                if i == j:
                    flag = True
            self.assertTrue(flag)
        

if __name__ == '__main__':
    unittest.main()