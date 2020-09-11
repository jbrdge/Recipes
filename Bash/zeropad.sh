#!/bin/sh
#A script to zero pad files
#used this last on .jpg files
for file in *.png; do

#adds three zeros
newnumber='000'${file}

#crop off left-most chars, leaving n chars
#in this case, last 5 chars
newnumber=${newnumber:(-5)}

mv $file $newnumber
done