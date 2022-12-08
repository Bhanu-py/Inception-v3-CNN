import os

# Get all the paths
data_dir_list = os.listdir('data/')
print(data_dir_list)
path, dirs, files = next(os.walk("data/"))
file_count = len(files)
# print(file_count)


# create two folders (train and validation)
train_dir = os.path.join('data/', 'train')
if not os.path.isdir(train_dir):
    os.mkdir(train_dir)

validation_dir = os.path.join('data/', 'validation')
if not os.path.isdir(validation_dir):
    os.mkdir(validation_dir)

test_dir = os.path.join('data/', 'test')
if not os.path.isdir(test_dir):
    os.mkdir(test_dir)


# Under train folder create Nine folders
# ('3_4th_driver_side_front', '3_4th_driver_side_rear', '3_4th_passenger_side_front',
#       '3_4th_passenger_side_rear', 'driver_side', 'front', 'passenger_side', 'rear', 'unknown')
data_lbls = data_dir_list

for i in data_dir_list:
    if not os.path.isdir(f'{train_dir}/{i}'):
        train_files_dir = os.path.join(train_dir, i)
        os.mkdir(train_files_dir)

for i in data_dir_list:
    if not os.path.isdir(f'{validation_dir}/{i}'):
        validation_files_dir = os.path.join(validation_dir, i)
        os.mkdir(validation_files_dir)

for i in data_dir_list:
    if not os.path.isdir(f'{test_dir}/{i}'):
        test_files_dir = os.path.join(test_dir, i)
        os.mkdir(test_files_dir)


