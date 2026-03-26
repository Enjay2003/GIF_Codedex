
import imageio.v3 as iio

filenames = ["C:/Users/Manish Jain/OneDrive/Desktop/python/GIF Project/team-pic1.png", "C:/Users/Manish Jain/OneDrive/Desktop/python/GIF Project/team-pic2.png"]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)



