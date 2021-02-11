import os
import matplotlib.image as mpimg
from skimage import exposure
from cv2 import flip
import sys

def create_folder(name):
  if not os.path.exists(name):
    os.makedirs(name)

def make_higer_exposure_sig(img, cutoff):
  return exposure.adjust_sigmoid(img, cutoff=cutoff)

def make_higer_exposure_gamma(img, gamma, gain=1):
  return exposure.adjust_gamma(img, gamma=gamma)


base_path = 'images_v2'

# Path to original images that we need to augmentate
original_cropped_images = f'./{base_path}/cropped_images_128'

# Path where all augmented images will be stored
augmented_path = f'./{base_path}/augmented_images_128'
create_folder(augmented_path)

categories = os.listdir(original_cropped_images)

for category in categories:
  category_path = f'{original_cropped_images}/{category}'
  print(category_path)
  print(category)
  images = os.listdir(category_path)
  # print(images)

  for image in images:
    image_path = f'{category_path}/{image}'

    # 0.5 default
    low_exp_cutoff = 0.55 # before 0.5 (was not dark enough)
    high_exp_cutoff = 0.38 # before 0.4 (sometimes to light)

    # 1 default, greater than 1 darker
    low_exp_gamma = 1
    high_exp_gamma = 0.8

    # Read image from path
    img = mpimg.imread(image_path)

    lower_exp = exposure.adjust_sigmoid(img, cutoff=low_exp_cutoff)
    # higher_exp = exposure.adjust_sigmoid(img, cutoff=high_exp_cutoff)
    # higher_exp = make_higer_exposure_sig(img, cutoff=high_exp_cutoff)
    higher_exp = make_higer_exposure_gamma(img, gamma=high_exp_gamma)


    flip_y = flip(img, 1)

    flipped_lower_exp = exposure.adjust_sigmoid(flip_y, cutoff=low_exp_cutoff)
    # flipped_higher_exp = exposure.adjust_sigmoid(flip_y, cutoff=high_exp_cutoff)
    # flipped_higher_exp = make_higer_exposure_sig(flip_y, cutoff=high_exp_cutoff)
    flipped_higher_exp = make_higer_exposure_gamma(flip_y, gamma=high_exp_gamma)

    # print(type(img))
    # print(type(lower_exp))
    # print(type(higher_exp))
    # print(type(flip_y))
    # print(type(flipped_lower_exp))
    # print(type(flipped_higher_exp))
    
    # sys.exit("END")

    # Create folder for each version
    create_folder(f'{augmented_path}/{category}')

    # Path for each image
    normal_exp_path = f'{augmented_path}/{category}/normal-exposure-{image}'
    lower_exp_path = f'{augmented_path}/{category}/lower-exposure-{image}'
    higher_exp_path = f'{augmented_path}/{category}/higher-exposure-{image}'

    # flip_y_path = f'{augmented_path}/{category}/flip-y-{image}'

    # Mirror image over y as
    if (category == 'left_ear'):
      print('this is a left ear flipped so put in right ear')
      create_folder(f'{augmented_path}/right_ear')
      flip_y_path = f'{augmented_path}/right_ear/flip-y-{image}'
      flipped_lower_exp_path = f'{augmented_path}/right_ear/flip-y-lower-exposure-{image}'
      flipped_higer_exp_path = f'{augmented_path}/right_ear/flip-y-higer-exposure-{image}'

    elif (category == 'right_ear'):
      print('this is a right ear flipped so put in left ear')
      create_folder(f'{augmented_path}/left_ear')
      flip_y_path = f'{augmented_path}/left_ear/flip-y-{image}'
      flipped_lower_exp_path = f'{augmented_path}/left_ear/flip-y-lower-exposure-{image}'
      flipped_higer_exp_path = f'{augmented_path}/left_ear/flip-y-higer-exposure-{image}'

    elif (category == 'left_hand'):
      print('this is a left hand flipped so put in right hand')
      create_folder(f'{augmented_path}/right_hand')
      flip_y_path = f'{augmented_path}/right_hand/flip-y-{image}'
      flipped_lower_exp_path = f'{augmented_path}/right_hand/flip-y-lower-exposure-{image}'
      flipped_higer_exp_path = f'{augmented_path}/right_hand/flip-y-higer-exposure-{image}'

    elif (category == 'right_hand'):
      print('this is a right hand flipped so put in left hand')
      create_folder(f'{augmented_path}/left_hand')
      flip_y_path = f'{augmented_path}/left_hand/flip-y-{image}'
      flipped_lower_exp_path = f'{augmented_path}/left_hand/flip-y-lower-exposure-{image}'
      flipped_higer_exp_path = f'{augmented_path}/left_hand/flip-y-higer-exposure-{image}'

    else:
      print('this has not to be moved to another folder')
      flip_y_path = f'{augmented_path}/{category}/flip-y-{image}'
      flipped_lower_exp_path = f'{augmented_path}/{category}/flip-y-lower-exposure-{image}'
      flipped_higer_exp_path = f'{augmented_path}/{category}/flip-y-higer-exposure-{image}'

    mpimg.imsave(normal_exp_path, img)
    mpimg.imsave(lower_exp_path, lower_exp)
    mpimg.imsave(higher_exp_path, higher_exp)
    mpimg.imsave(flip_y_path, flip_y)
    mpimg.imsave(flipped_lower_exp_path, flipped_lower_exp)
    mpimg.imsave(flipped_higer_exp_path, flipped_higher_exp)
    # break;


sys.exit("END")

# Old version
# # Directory with all cropped images
# # Old one
# # cropped_path = './images/Cropped-square'
# # Version tibo
# cropped_path = './images/cropped_images'

# # Directory where all augmented images will be stored
# aug_path = './images/Augmented-square'

# category = os.listdir(cropped_path) # 'Geen-Gsm-gebruik' & 'Gsm-gebruik'

# for cat in category:
#   cat_path = f'{cropped_path}/{cat}'
#   images = os.listdir(cat_path)
  
#   for image in images:
#     # Load image
#     img_path = f'{cat_path}/{image}'
#     img = mpimg.imread(img_path)


#     # Create lower & higher exposure image
#     # lower_exp = exposure.exposure.adjust_gamma(img, gamma=2)
#     lower_exp = exposure.adjust_sigmoid(img, cutoff=0.5)
#     higher_exp = exposure.adjust_sigmoid(img, cutoff=0.4)
#     flip_y = flip(img, 1)

#     # Path for each image
#     normal_exp_path = f'{aug_path}/{cat}/aug-normal-exposure-{image}'
#     lower_exp_path = f'{aug_path}/{cat}/aug-lower-exposure-{image}'
#     higher_exp_path = f'{aug_path}/{cat}/aug-higher-exposure-{image}'
#     flip_y_path = f'{aug_path}/{cat}/aug-flip-y-{image}'

#     # print(normal_exp_path)
#     # print(lower_exp_path)
#     # print(higher_exp_path)
#     # print(flip_y_path)
    
#     mpimg.imsave(normal_exp_path, img)
#     mpimg.imsave(lower_exp_path, lower_exp)
#     mpimg.imsave(higher_exp_path, higher_exp)
#     mpimg.imsave(flip_y_path, flip_y)
#     # break