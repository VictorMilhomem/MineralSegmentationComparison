import os

def get_parent_folder_path(file_path):
    parent_folder_path = os.path.dirname(file_path)
    return  os.path.dirname(parent_folder_path)

CURRENT_PATH = os.path.realpath(__file__)
BASE_FOLDER = get_parent_folder_path(CURRENT_PATH)


PROCESSED_FOLDER = f'{BASE_FOLDER}/MineralSegmentation/processed_images'
RESULTS_FOLDER = f'{BASE_FOLDER}/MineralSegmentation/results'
LOGS_FOLDER = f'{BASE_FOLDER}/MineralSegmentation/logs'

PATH_TO_FE19_DATASET_RLM = f'{BASE_FOLDER}/Fe19/Reflected_Light_Microscopy'
PATH_TO_FE120_DATASET_RLM = f'{BASE_FOLDER}/Fe120/Reflected_Light_Microscopy'
PATH_TO_FEM_DATASET_RLM = f'{BASE_FOLDER}/FeM/Reflected_Light_Microscopy'
PATH_TO_CU_DATASET_RLM = f'{BASE_FOLDER}/Cu/Reflected_Light_Microscopy'

PATH_TO_FE19_DATASET_MASK = f'{BASE_FOLDER}/Fe19/Reference'
PATH_TO_FE120_DATASET_MASK = f'{BASE_FOLDER}/Fe120/Reference'
PATH_TO_FEM_DATASET_MASK = f'{BASE_FOLDER}/FeM/Reference'
PATH_TO_CU_DATASET_MASK = f'{BASE_FOLDER}/Cu/Reference'

PATH_TO_FOLDER = {
    'Fe19':{
        'RLM': PATH_TO_FE19_DATASET_RLM,
        'MASK': PATH_TO_FE19_DATASET_MASK},
    'Fe120':{
		'RLM': PATH_TO_FE120_DATASET_RLM,
		'MASK': PATH_TO_FE120_DATASET_MASK},
    'FeM':{
        'RLM': PATH_TO_FEM_DATASET_RLM,
        'MASK': PATH_TO_FEM_DATASET_MASK},
    'Cu':{
        'RLM': PATH_TO_CU_DATASET_RLM,
        'MASK': PATH_TO_CU_DATASET_MASK}}

"""
NUM_IMAGES = {
        'Fe19': 19,
        'Fe120': 120,
        'FeM': 81,
        'Cu': 121}

"""


NUM_IMAGES = {
        'Fe19': 19,
        'Fe120': 19,
        'FeM': 39,
        'Cu': 39}

TEST_INDEX = {
        'Fe19': [0, 14, 5, 17],
        'Fe120': [0, 14, 5, 17],
        'FeM': [35, 3, 12, 21],
        'Cu': [20, 32, 1, 7]}