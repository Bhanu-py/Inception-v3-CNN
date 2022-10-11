import os
import random
from shutil import copyfile
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.image import imread
import pathlib

print(os.getcwd())
os.listdir('data/3_4th_driver_side_front')

#
# def split_data(SOURCE, TRAINING, VALIDATION, TEST, TRAIN_SIZE, VALID_SIZE):
#     files = []
#     for filename in os.listdir(SOURCE):
#         file = SOURCE + filename
#         if os.path.getsize(file) > 0:
#             files.append(filename)
#         else:
#             print(filename + " is zero length, so ignoring.")
#
#     training_length = int(len(files) * TRAIN_SIZE) # 400
#     valid_length = int(len(files) * VALID_SIZE) # 50
#     test_length = int(len(files) - (training_length + valid_length)) # 50
#     shuffled_set = random.sample(files, len(files))
#     training_set = shuffled_set[0:training_length]
#     valid_set = shuffled_set[training_length:(training_length+valid_length)]
#     test_set = shuffled_set[(training_length+valid_length):]
#
#     for filename in training_set:
#         this_file = SOURCE + filename
#         destination = TRAINING + filename
#         copyfile(this_file, destination)
#
#     for filename in valid_set:
#         this_file = SOURCE + filename
#         destination = VALIDATION + filename
#         copyfile(this_file, destination)
#
#     for filename in test_set:
#         this_file = SOURCE + filename
#         destination = TEST + filename
#         copyfile(this_file, destination)
#
#
# driver_side_front_SOURCE_DIR = 'data/3_4th_driver_side_front/'
# TRAINING_driver_side_front_DIR = 'data/train/3_4th_driver_side_front/'
# VALID_driver_side_front_DIR = 'data/validation/3_4th_driver_side_front/'
# TEST_driver_side_front_DIR = 'data/test/3_4th_driver_side_front/'
#
# driver_side_rear_SOURCE_DIR = 'data/3_4th_driver_side_rear/'
# TRAINING_driver_side_rear_DIR = 'data/train/3_4th_driver_side_rear/'
# VALID_driver_side_rear_DIR = 'data/validation/3_4th_driver_side_rear/'
# TEST_driver_side_rear_DIR = 'data/test/3_4th_driver_side_rear/'
#
# passenger_side_front_SOURCE_DIR = 'data/3_4th_passenger_side_front/'
# TRAINING_passenger_side_front_DIR = 'data/train/3_4th_passenger_side_front/'
# VALID_passenger_side_front_DIR = 'data/validation/3_4th_passenger_side_front/'
# TEST_passenger_side_front_DIR = 'data/test/3_4th_passenger_side_front/'
#
# passenger_side_rear_SOURCE_DIR = 'data/3_4th_passenger_side_rear/'
# TRAINING_passenger_side_rear_DIR = 'data/train/3_4th_passenger_side_rear/'
# VALID_passenger_side_rear_DIR = 'data/validation/3_4th_passenger_side_rear/'
# TEST_passenger_side_rear_DIR = 'data/test/3_4th_passenger_side_rear/'
#
# driver_side_SOURCE_DIR = 'data/driver_side/'
# TRAINING_driver_side_DIR = 'data/train/driver_side/'
# VALID_driver_side_DIR = 'data/validation/driver_side/'
# TEST_driver_side_DIR = 'data/test/driver_side/'
#
# front_SOURCE_DIR = 'data/front/'
# TRAINING_front_DIR = 'data/train/front/'
# VALID_front_DIR = 'data/validation/front/'
# TEST_front_DIR = 'data/test/front/'
#
# passenger_side_SOURCE_DIR = 'data/passenger_side/'
# TRAINING_passenger_side_DIR = 'data/train/passenger_side/'
# VALID_passenger_side_DIR = 'data/validation/passenger_side/'
# TEST_passenger_side_DIR = 'data/test/passenger_side/'
#
# rear_SOURCE_DIR = 'data/rear/'
# TRAINING_rear_DIR = 'data/train/rear/'
# VALID_rear_DIR = 'data/validation/rear/'
# TEST_rear_DIR = 'data/test/rear/'
#
# unknown_SOURCE_DIR = 'data/unknown/'
# TRAINING_unknown_DIR = 'data/train/unknown/'
# VALID_unknown_DIR = 'data/validation/unknown/'
# TEST_unknown_DIR = 'data/test/unknown/'
#
# train_size = .80
# valid_size = .10
#
# split_data(driver_side_front_SOURCE_DIR, TRAINING_driver_side_front_DIR, VALID_driver_side_front_DIR, TEST_driver_side_front_DIR,
#            train_size, valid_size)
#
# split_data(driver_side_rear_SOURCE_DIR, TRAINING_driver_side_rear_DIR, VALID_driver_side_rear_DIR, TEST_driver_side_rear_DIR,
#            train_size, valid_size)
#
# split_data(passenger_side_front_SOURCE_DIR, TRAINING_passenger_side_front_DIR, VALID_passenger_side_front_DIR, TEST_passenger_side_front_DIR,
#            train_size, valid_size)
#
# split_data(passenger_side_rear_SOURCE_DIR, TRAINING_passenger_side_rear_DIR, VALID_passenger_side_rear_DIR, TEST_passenger_side_rear_DIR,
#            train_size, valid_size)
#
# split_data(driver_side_SOURCE_DIR, TRAINING_driver_side_DIR, VALID_driver_side_DIR, TEST_driver_side_DIR,
#            train_size, valid_size)
#
# split_data(front_SOURCE_DIR, TRAINING_front_DIR, VALID_front_DIR, TEST_front_DIR,
#            train_size, valid_size)
#
# split_data(passenger_side_SOURCE_DIR, TRAINING_passenger_side_DIR, VALID_passenger_side_DIR, TEST_passenger_side_DIR,
#            train_size, valid_size)
#
# split_data(rear_SOURCE_DIR, TRAINING_rear_DIR, VALID_rear_DIR, TEST_rear_DIR,
#            train_size, valid_size)
#
# split_data(unknown_SOURCE_DIR, TRAINING_unknown_DIR, VALID_unknown_DIR, TEST_unknown_DIR,
#            train_size, valid_size)

image_folder = ['3_4th_driver_side_front', '3_4th_driver_side_rear',
                '3_4th_passenger_side_front', '3_4th_passenger_side_rear',
                'driver_side', 'front', 'passenger_side', 'rear', 'unknown']
nimgs = {}
for i in image_folder:
    nimages = len(os.listdir('data/train/'+i+'/'))
    nimgs[i]=nimages
plt.figure(figsize=(9, 6))
plt.bar(range(len(nimgs)), list(nimgs.values()), align='center')
plt.xticks(range(len(nimgs)), list(nimgs.keys()))
plt.title('Distribution of different classes in Training Dataset')
plt.ylim(0, 600)
plt.show()
