import csv
from geopy.geocoders import Nominatim
from collections import Counter
import os
import numpy as np
import gmplot
import imageio

geolocator = Nominatim(timeout = 50)

# # ---------------------------------------------------------------------------------------------------------------------
# # reading and saving the data
# # maintaining a list of dictionary where the ith dictionary in the list contains the location wise count in the ith week
# count_list = [Counter([]) for i in range(25)]

# data_files = [os.path.join('uber-trip-data', filename) for filename in os.listdir('uber-trip-data') if os.path.isfile(os.path.join('uber-trip-data', filename)) and filename.endswith('.csv') and filename.startswith('uber')]
# for filename in data_files:
# 	with open(filename) as csvfile:
# 		data_reader = csv.reader(csvfile, delimiter = ',')
# 		next(data_reader)

# 		for line in data_reader:
# 			# getting the month and the date
# 			month = int(line[0].split('/')[0])
# 			month = month -3

# 			date = int(line[0].split('/')[1])
			
# 			# getting the week number
# 			if (month == 1):
# 				week = 0
# 			else:
# 				week = 4*(month-1)

# 			if (1<= date <= 7):
# 				week = week + 1
# 			elif (8<= date <= 14):
# 				week = week + 2
# 			elif (15<= date <= 21):
# 				week = week + 3
# 			else:
# 				week = week + 4

# 			lat_lon = format(float(line[1]), '.3f') + ',' + format(float(line[2]), '.3f')
			
# 			count_list[week] += Counter([lat_lon])

# np.save("data_saved.npy", count_list)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# loading the saved data and generating the images
# count_list = np.load("data_saved.npy").tolist()

# week_count_dict = count_list[24]
# lats = []
# lons = []

# for key, value in week_count_dict.items():
# 	# unfolding the dictionary entry as a list, based on value
# 	lat_as_float = float(key.split(',')[0])
# 	lon_as_float = float(key.split(',')[1])
# 	lats_temp_list = [lat_as_float for i in range(value)]
# 	lons_temp_list = [lon_as_float for i in range(value)]

# 	# updating the weekl-based lat lon lists
# 	lats = lats + lats_temp_list
# 	lons = lons + lons_temp_list
	
# # generating the heatmap image
# gmap = gmplot.GoogleMapPlotter(40.72, -73.886379, 11)
# gmap.heatmap(lats, lons)
# gmap.draw("nyc_uber_pickups-24.html")
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# combining the heatmap (hm) images generated above to form a gif
images = []
filenames = [os.path.join('images', filename) for filename in os.listdir('images') if os.path.isfile(os.path.join('images', filename)) and filename.endswith('.png') and filename.startswith('hm')]
for filename in filenames:
	images.append(imageio.imread(filename))
imageio.mimsave('nyc_uber_pickups.gif', images, duration = 0.4)
