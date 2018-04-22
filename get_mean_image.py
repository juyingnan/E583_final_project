from skimage import io
from skimage.color import rgba2rgb
import os
import numpy as np

os.chdir('C:/Users/bunny/Desktop/images-227/')
years = [i for i in range(2003, 2018)]


def get_mean_image(img_list):
    return np.mean(img_list, axis=0)


image_for_years_all = []
for year in years:
    image_for_years_all.append([])
for website in os.listdir(os.getcwd()):
    web_dir = os.path.join(os.getcwd(), website)
    if not os.path.isdir(web_dir):
        continue
    image_for_years = []
    for year in years:
        image_for_years.append([])
    for img in os.listdir(web_dir):
        img_path = os.path.join(os.getcwd(), website, img)
        img_path = img_path.replace('\\', '//')  # for Windows adjustment
        if os.path.exists(img_path) == -1:
            print("[ERROR] Error while reading")
        image = io.imread(img_path)
        image = np.asarray(image, 'float32') / 255
        if image.shape[2] == 4:
            #     image = image[:, :, :3]
            image = rgba2rgb(image)
        if img.startswith('20'):
            img_year = int(img[:4])
            if img_year in years:
                index = years.index(img_year)
                image_for_years[index].append(image)
                image_for_years_all[index].append(image)

    for year in years:
        index = years.index(year)
        if len(image_for_years[index]) > 0:
            mean_img = get_mean_image(image_for_years[index])
            save_path = os.path.join(os.getcwd(), website, 'mean_' + year.__str__() + '.png')
            # print(save_path)
            io.imsave(save_path, mean_img)
    print('\r' + website, end='')
for year in years:
    index = years.index(year)
    if len(image_for_years_all[index]) > 0:
        mean_img = get_mean_image(image_for_years_all[index])
        save_path = os.path.join(os.getcwd(), 'mean_' + year.__str__() + '.png')
        # print(save_path)
        io.imsave(save_path, mean_img)

# delete the img
print('\rdeleting', end='')
for website in os.listdir(os.getcwd()):
    web_dir = os.path.join(os.getcwd(), website)
    if not os.path.isdir(web_dir):
        continue
    for img in os.listdir(web_dir):
        img_path = os.path.join(os.getcwd(), website, img)
        if img.startswith('20'):
            os.remove(img_path)
