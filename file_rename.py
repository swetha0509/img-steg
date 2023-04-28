import os

directory = r'C:/Users/swetha/fn_year/steganography/dataset/train/secret'
 # set the prefix for the new file names
counter = 1 # initialize the counter for the new file names
try:
    for filename in os.listdir(directory):
        #if filename.endswith('.txt'): # only rename text files, change the extension to suit your needs
            new_filename = str("train"+ str(counter)) + '.txt' # create the new file name with the prefix and counter
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename)) # rename the file
            counter += 1 # increment the counter for the next file
except FileExistsError:
      pass