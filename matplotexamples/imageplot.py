from matplotlib import  pyplot as plt
from PIL import Image
import numpy as np

sample = Image.open("../resources/Roses.jpg")
#Convert the image to NDArray
imgarr = np.array(sample)

#Optionally, you can fix image display size
plt.figure(figsize=(3,2))
#Add axes
ax1 = plt.subplot()
#Add image
ax1.imshow(imgarr)
#Display plot
plt.show()