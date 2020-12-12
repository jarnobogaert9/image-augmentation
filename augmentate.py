import os
import matplotlib.image as mpimg
from skimage import exposure
from cv2 import flip

# Directory with all cropped images
cropped_path = './images/Cropped-square'

# Directory where all augmented images will be stored
aug_path = './images/Augmented-square'

category = os.listdir(cropped_path) # 'Geen-Gsm-gebruik' & 'Gsm-gebruik'

for cat in category:
  cat_path = f'{cropped_path}/{cat}'
  images = os.listdir(cat_path)
  
  for image in images:
    # Load image
    img_path = f'{cat_path}/{image}'
    img = mpimg.imread(img_path)


    # Create lower & higher exposure image
    # lower_exp = exposure.exposure.adjust_gamma(img, gamma=2)
    lower_exp = exposure.adjust_sigmoid(img, cutoff=0.5)
    higher_exp = exposure.adjust_sigmoid(img, cutoff=0.4)
    flip_y = flip(img, 1)

    # Path for each image
    normal_exp_path = f'{aug_path}/{cat}/aug-normal-exposure-{image}'
    lower_exp_path = f'{aug_path}/{cat}/aug-lower-exposure-{image}'
    higher_exp_path = f'{aug_path}/{cat}/aug-higher-exposure-{image}'
    flip_y_path = f'{aug_path}/{cat}/aug-flip-y-{image}'

    # print(normal_exp_path)
    # print(lower_exp_path)
    # print(higher_exp_path)
    # print(flip_y_path)
    
    mpimg.imsave(normal_exp_path, img)
    mpimg.imsave(lower_exp_path, lower_exp)
    mpimg.imsave(higher_exp_path, higher_exp)
    mpimg.imsave(flip_y_path, flip_y)
    # break