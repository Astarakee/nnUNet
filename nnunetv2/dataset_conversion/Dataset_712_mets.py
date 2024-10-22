import multiprocessing
import shutil
from multiprocessing import Pool

import SimpleITK as sitk
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


if __name__ == '__main__':
    out_base = '/home/mehdi/Data/Mets24/Dataset721_Mets24'
    label_path = os.path.join(out_base, 'labelsTr')
    n_files = len(os.listdir(label_path))
    task_id = 721
    task_name = "Mets24"

    foldername = "Dataset%03.0d_%s" % (task_id, task_name)

    generate_dataset_json(out_base,
                          channel_names={0: 'T1n', 1: 'T1c', 2: 'T2w', 3: 'T2f'},
                          labels={
                              'background': 0,
                              'NETC': 1,
                              'SNFH': 2,
                              'ET': 3,
                          },
                          num_training_cases=n_files,
                          file_ending='.nii.gz',
                          dataset_release='1.0')