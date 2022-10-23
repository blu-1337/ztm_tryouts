import sys
import os
from PIL  import Image


# grab first and second argument

args = sys.argv

print(args)

input_location = args[1]
output_location = args[2]




# check is new / exists, if not create

# for input_location
if(os.path.exists(input_location)):
    print("input_location exists")
else:
    raise Exception("please create input_location dir first")
# for output_location
if(os.path.exists(output_location)):
    print("output_location exists")
else:
    print("it does not exist, creating dir 'converted_fiels'...")
    os.mkdir(output_location)


# loop through Pokedex

print('Here are the files inside the folder:')
for filename in os.listdir(input_location):
    f = os.path.join(input_location, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        print(filename)
        im = Image.open(f)
        new_name = filename[:-4]+".png"
        print('newname:', new_name)

        im.save(output_location+new_name)




# convert images to png


# save to the new folder
