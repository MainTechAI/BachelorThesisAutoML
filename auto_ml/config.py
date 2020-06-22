# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:33:43 2020

@author: dosto
"""

# %%
from pathlib import Path

import json
import os.path
config_name = 'config.json'

default_config = {   # Only English or Unicode allowed for strings
                    'task':'classification',
                    
                    'experiment_name':'experiment_1',
                    
                    'model_requirements':
                        {  
                            'min_accuracy':65,                 
                            'max_memory':1048576, # bytes
                            'max_single_predict_time':40,  # ms                      
                            'max_train_time (sec)':100,
                        },
                            
                    'search_space':
                        {
                            'AdaBoost':True, 
                            'XGBoost':True, 
                            'Bagging(SVС)':True,        
                            'MLP':True, 
                            'HistGB':False, 
                            'Ridge':False,       
                            'LinearSVC':False, 
                            'PassiveAggressive':False, 
                            'LogisticRegression':False,        
                            'LDA':False, 
                            'QDA':False, 
                            'Perceptron':False, 
                            'SVM':True, 
                            'RandomForest':True, 
                            'xRandTrees':True,     
                            'ELM':True, 
                            'DecisionTree':False, 
                            'SGD':False, 
                            'KNeighbors':False, 
                            'NearestCentroid':False, 
                            'GaussianProcess':False,
                            'LabelSpreading':False, 
                            'BernoulliNB':False, 
                            'GaussianNB':False, 
                            'DBN':False, 
                            'FactorizationMachine':False, 
                            'PolynomialNetwork':False,                                              
                        },
                     
                    'search_options':
                        {
                            'duration':240, # sec
                            'iterations':100, # number of optimizer iterations
                            'metric':'accuracy',
                            'validation':{
                                'type':'CV', # 'CV' or 'holdout'
                                'value':10,  # 10 CV or 70 holdout
                                         },
                            'saved_top_models_amount':1, # number or 'all'
                        },
                     
                    'paths':
                        {
                            'DS_abs_path':None,
                            'CD_abs_path':None,
                        },
                        
                    'global_variables': # move to glob_var.pickle
                        {                        
                            'DS_name':None,
                            'DS_type':None, # csv,  TODO excel
                            
                            'CD_name':None,
                            'CD_type':None, # csv
                            
                            'target_column':None, #[1,4]  так бывает, ммм?
                            'categ_columns':None,
                            'text_columns':None,
                            'num_columns':None,
                            # other by default Auxiliary
                            # and will be ignored
                                                     
                            # 'Number of targets':1, # nr_targets
                            # 'Target cardinality':2,                           
                        }                                     
                 }

# %%

def load_config(): # load_path
    """
    Create config.json file if does not exist
    If exist then return dict
    
    Simply use every time when you need config    
    """
    
    if os.path.isfile(config_name): # if config file EXIST
        with open(config_name, encoding='utf-8') as f:
            config = json.load(f)
        return config
        
    else:                           # if config file doesn't exist        
        # Create default config.json
        save_config(default_config)
        
        # Try to load
        if os.path.isfile(config_name): # if now config file exist
            with open(config_name, encoding='utf-8') as f:
                created_config = json.load(f)
            return created_config
        
        else:
            # Raise error
            print('Error. Unable to write file...')
            raise Exception('Error. Unable to write file...')

# %%

def save_config(config_dict): # save_path=None  file_name=None
    """
    Function saves dict as json file to disk
    """
    with open(config_name, 'w') as fp:  
        json.dump(config_dict, fp, indent=4)  
    
# %%
          
def handle_dataset_path(norm_abs_path):
    
    pathlib_abs_path=Path(norm_abs_path)
    conf = load_config()
    conf['paths']['DS_abs_path'] = str(pathlib_abs_path)
    
    conf['global_variables']['DS_name'] = pathlib_abs_path.name
    conf['global_variables']['DS_type'] = pathlib_abs_path.suffix.lower()
    
    save_config(conf)

# %%         
      
def handle_column_description_path(norm_abs_path):
    
    pathlib_abs_path=Path(norm_abs_path)
    conf = load_config()
    conf['paths']['CD_abs_path'] = str(pathlib_abs_path)
    
    conf['global_variables']['CD_name'] = pathlib_abs_path.name
    conf['global_variables']['CD_type'] = pathlib_abs_path.suffix.lower() 
    
    save_config(conf)
    
# %%
    
def paths_selected():
    
    conf = load_config()
    DS, CD = True, True
    if(conf['paths']['DS_abs_path'] == None):
        DS=False
    if(conf['paths']['CD_abs_path'] == None):
        CD=False
        
    return DS, CD

# %%
    

    
# %%

if __name__ == "__main__":
    from pprint import pprint
    pprint(load_config())



