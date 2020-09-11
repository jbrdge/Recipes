#!/bin/sh
#Convert names of files to ordered numbers

i=0
for f in *;
do file $f;
mv $f ${i}.png;
i=i+1;
done