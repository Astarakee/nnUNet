import multiprocessing
import shutil
from multiprocessing import Pool

import SimpleITK as sitk
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


if __name__ == '__main__':
    out_base = '/mnt/workspace/data/VerTEB/Dataset722_Spine1kBinary'
    label_path = os.path.join(out_base, 'labelsTr')
    n_files = len(os.listdir(label_path))
    task_id = 722
    task_name = "Spine1kBinary"

    foldername = "Dataset%03.0d_%s" % (task_id, task_name)

    generate_dataset_json(out_base,
                          channel_names={0: 'CT'},
                          labels={
                              'background': 0,
                              'Vertebra': 1,
                          },
                          num_training_cases=n_files,
                          file_ending='.nii.gz',
                          dataset_release='1.0')