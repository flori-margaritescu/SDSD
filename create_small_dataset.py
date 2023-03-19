import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

"""
all video frames are saved as .npy file and the resolution is 512 x 960 for fast training
"""


""" Script that halves the size of the images, also takes every 5th frame -> speed up by 10x hopefully """
""" New image resolution would be: 256 x 480 """


for gt_or_input in ('GT', 'input'):
    # # Actual dataset directory
    dataset_dir = 'dataset/indoor_np/{}'.format(gt_or_input)
    new_dataset_dir = 'dataset_small/indoor_np/{}'.format(gt_or_input)

    # Create new directory
    if not os.path.exists(new_dataset_dir):
        os.makedirs(new_dataset_dir)

    for i, (subdir, pair_name, files) in enumerate(os.walk(dataset_dir)):
        if i == 0: continue
        pair_name = subdir.split('/')[3]
        #print(subdir, pair_name, files)

        # Create in new directory if it doesn't exist
        if not os.path.exists(os.path.join(new_dataset_dir, pair_name)):
            os.makedirs(os.path.join(new_dataset_dir, pair_name))

        # Go through the .npy files
        for num, file in enumerate(sorted(files)):
            # Take every 5th frame
            if num % 5 != 0:
                continue
            filename = os.path.join(dataset_dir, pair_name, file)
            img_array = np.load(filename, allow_pickle=True)[::2, ::2]
            # # Display image
            # plt.imshow(img_array, cmap="gray")
            # img_name = file+".png"
            # image.imsave(img_name, img_array)
            
            # Save the image into new dir
            np.save(os.path.join(new_dataset_dir, pair_name, file), img_array)


""" Quick script to extract every 10th frame"""

# files = os.listdir('dataset_small/pair1')

# for num, file in enumerate(files):
#     filename = os.path.join('dataset_small/pair1', file)
#     img_array = np.load(filename, allow_pickle=True)
#     plt.imshow(img_array, cmap="gray")
#     img_name = "exracted_"+file+".png"
#     image.imsave(img_name, img_array)
#     print(filename)