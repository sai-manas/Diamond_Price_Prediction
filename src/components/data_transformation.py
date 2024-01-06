import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer # handling missing values
from sklearn.preprocessing import StandardScaler # handling feature scaling
from sklearn.preprocessing import OrdinalEncoder # ordinal encoding
## importing pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() 

    def get_data_transformation_obj(self):
        logging.info("Data transformation method started")

        try:
            ## Numerical and Categorical columns
            numerical_columns = ["carat", "depth", "table", "x", "y", "z"]
            categorical_columns = ["cut","color","clarity"]

            ## Defining the custom ranking for each ordinal variable with respect to the ranking given in domain site("https://www.americangemsociety.org/ags-diamond-grading-system/")
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info("Data Transformation Pipeline Initiated")
            ## Numerical pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            ## Categorical pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('Ordinal encoder', OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num pipeline',num_pipeline,numerical_columns),
                ('cat pipeline',cat_pipeline,categorical_columns)
            ])

            logging.info("Data Transformation is completed")
            return preprocessor
        
        except Exception as e:
            logging.info("Error occurred in Data Transformation process")
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading train and test data to dataframe is completed")
            logging.info(f'Train DataFrame : \n{train_df.head().to_string()}')
            logging.info(f'Test DataFrame : \n{test_df.head().to_string()}')

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformation_obj()

            target_column = "price"
            drop_column = [target_column,"id"]

            ## Independent and dependent features
            ## Train data
            input_train_df = train_df.drop(columns=drop_column, axis=1)
            target_train_df = train_df[target_column]

            ## Test data
            input_test_df = test_df.drop(columns=drop_column, axis=1)
            target_test_df = test_df[target_column]

            ## Applying Data Transformation
            input_train_array = preprocessing_obj.fit_transform(input_train_df)
            input_test_array = preprocessing_obj.transform(input_test_df)
            
            logging.info("Applied preprocessing on training and testing datasets")

            train_arr = np.c_[input_train_array, np.array(target_train_df)]
            test_arr = np.c_[input_test_array, np.array(target_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_file_path,
                obj= preprocessing_obj
            )

            logging.info('Preprocessor pickle file is created and saved')

            return(
                train_arr,test_arr,self.data_transformation_config.preprocessor_file_path
            )

        except Exception as e:
            logging.info("Exception occurred in the initiate_data_transformation method")
            raise CustomException(e,sys)