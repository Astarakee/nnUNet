import os
import shutil
import argparse
from tools.paths_dirs_stuff import path_contents, path_contents_pattern, create_path

parser = argparse.ArgumentParser(description='Using model best checkpoints for prediciting the validation sets')
parser.add_argument('-i', type=str, help='abs path to data directory', required=True)
parser.add_argument('-o', type=str, help='abs path to save masks', required=True)
parser.add_argument('-tmp_path', type=str, help='abs path to a temp directory for copying the data', required=True)
parser.add_argument('-model_path', type=str, help='abs path to a temp directory for copying the data', required=True)
parser.add_argument('-d', type=int, help='model ID', required=True)
parser.add_argument('-f', type=int, help='fold number', required=True)
args = parser.parse_args()

data_path = args.i
pred_path = args.o
model_path = args.model_path
temp_data = args.tmp_path
model_name = args.d
fold = args.f

def main():
    label_path = os.path.join(data_path, 'labelsTr')
    image_path = os.path.join(data_path, 'imagesTr')
    #label_files = path_contents_pattern(label_path, '.nii.gz')
    image_files = path_contents_pattern(image_path, '.nii.gz')
    fold_name = 'fold_'+str(fold)
    fold_path = os.path.join(model_path, fold_name, 'validation')
    fold_files = path_contents_pattern(fold_path, '.nii.gz')
    temp_data_fold = os.path.join(temp_data, fold_name)
    pred_path_fold = os.path.join(pred_path, fold_name)
    create_path(temp_data_fold)
    create_path(pred_path_fold)

    img_fold_name = []
    for item_pred in fold_files:
        for item_img in image_files:
            item_pred_name = item_pred.split('.nii.gz')[0]
            if item_pred_name in item_img:
                img_fold_name.append(item_img)

    for filename in img_fold_name:
        src= os.path.join(image_path, filename)
        dst = os.path.join(temp_data_fold, filename)
        shutil.copy(src, dst)

    os.system('nnUNetv2_predict -i %s -o %s -d %s -c 3d_fullres -p nnUNetResEncUNetPlans -f %s -chk checkpoint_best.pth' % (temp_data_fold , pred_path_fold, model_name, fold))
    # os.system(
    #     'nnUNetv2_predict -i %s -o %s -d %s -c 3d_fullres -p nnUNetResEncUNetPlans -f %s' % (
    #     temp_data_fold, pred_path_fold, model_name, fold))

    return None

if __name__ == '__main__':
    main()

# data_path = "/mnt/workspace/data/Vitali/Mets_Seg/Verteb/Dataset701_VerMetCrop/"
# model_path = "/mnt/workspace/data/nnUnet/nnUNet_results/VerMets/152Subjects/TinyCrop_ClipCT/Dataset701_VerMetCrop/nnUNetTrainer__nnUNetResEncUNetPlans__3d_fullres"
# pred_path = "/mnt/workspace/data/nnUnet/nnUNet_results/VerMets/152Subjects/TinyCrop_ClipCT/Dataset701_VerMetCrop/pred_val_best_ch"
# temp_data = "/mnt/workspace/data/00_junks/temp_"
# fold = 0
# model_name = 701