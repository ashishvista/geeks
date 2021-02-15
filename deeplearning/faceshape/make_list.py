from os import walk
from PIL import Image
import shutil
parent = "/home/ashish/Downloads/FaceShape Dataset/training_set"
target_folder = "/home/ashish/Downloads/FaceShape Dataset/all_images"
img_list_file = "/home/ashish/Downloads/FaceShape Dataset/train_img.lst"
class_arr = ['Round', 'Square', 'Oblong', 'Heart', 'Oval']






index = 0
tab_char = "	"
with open(img_list_file, "a") as myfile:
    full_path_parent, classes, filenames = next(walk(parent))
    for class_name in classes:
        f1, f2, filenames = next(walk(full_path_parent + "/" + class_name))
        class_str = ""
        flag = False
        for i, c in enumerate(class_arr):
            if c == class_name:
                class_str += "1"
                flag = True
            else:
                class_str += "0"
            class_str += tab_char

        if not flag:
            raise Exception("class name not found" + class_name)

        for filename in filenames:
            img = Image.open(f1 + "/" + filename)
            if img.format != 'JPEG':
                continue
            s = ""
            filename_without_space = filename.replace(" ", "").replace("(", "-").replace(")", "")
            shutil.copyfile(f1 + "/" + filename, target_folder + "/" + filename_without_space)
            s += str(index) + tab_char + class_str + filename_without_space + "\n"
            myfile.write(s)
            index += 1
print("Completed.......")