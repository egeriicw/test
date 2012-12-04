import re
import sys


with open('C:\Alexandria__1211241130.dbf','r') as f:
  f.seek(194)
  test = True
  while test:
    line = f.read(94)
    #Use Regular Express to remove whitespace,
    #strip righthand whitespace, then split in to tokens
    if line == "":
      test = False
    else: print "--", re.sub('\s{1,}',' ', line.rstrip()).split(' '), '\n'



#Convert image to numpy array
#I = numpy.asarray(Image.open(<image name>))
##
#Convert back to image
#im = Image.fromarray(numpy.uint8(I))



#####
# parameter list using dictionary
# values = {}
# values['lat'] = <lat_value>
# values['longitude'] = <long_value>




