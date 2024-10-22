import multiprocessing
import shutil
from multiprocessing import Pool

import SimpleITK as sitk
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


if __name__ == '__main__':
    out_base = '/home/mehdi/Data/BraTS24/Dataset720_BraTS24CTV_test'
    label_path = os.path.join(out_base, 'labelsTr')
    n_files = len(os.listdir(label_path))
    task_id = 720
    task_name = "BraTS24CTV_test"

    foldername = "Dataset%03.0d_%s" % (task_id, task_name)

    generate_dataset_json(out_base,
                          channel_names={0: 'T1', 1: 'T1ce', 2: 'T2', 3: 'Flair'},
                          labels={
                              'background': 0,
                              'ctv': 1,
                          },
                          num_training_cases=n_files,
                          file_ending='.nii.gz',
                          dataset_release='1.0')