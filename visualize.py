from os import listdir, path, makedirs
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

input_path = './Test_Validation/normal/'
output_path = './transformed_testset/normal/'

if not path.exists(output_path):
    makedirs(output_path)

imgCount = 0

for filename in listdir(input_path):
    imgCount += 1
    img = np.asarray(Image.open(input_path + filename))
    normalized = (img/np.amax(img))
    plt.imsave(output_path + "covid_" +str(imgCount) + ".jpg", normalized, cmap="gray")

    print("Saving Image {}/{} ==> {:.2f}% Concluded".format(imgCount, len(listdir(input_path)),(imgCount/len(listdir(input_path))*100)))

#for diretorio in listdir(input_path):
#    firstDir = input_path + diretorio + "/"
#    for dirname in listdir(firstDir):
#        patientDir = firstDir + dirname + "/"
#        for srDir in listdir(patientDir):
#            dirCount = 0
#            lastDir = patientDir + srDir + "/"
#            for filename in listdir(lastDir):
#                dirCount += 1
#                imgCount += 1
#                img = np.asarray(Image.open(lastDir + filename))
#                normalized = (img/np.amax(img))
#                plt.imsave(output_path + "covid_" + str(imgCount) + ".jpg", normalized, cmap="gray")
#                print("Colecting and Saving {}/{} Images from {}".format(dirCount,
#                                                                         len(listdir(lastDir)),
#                                                                         lastDir + filename))
