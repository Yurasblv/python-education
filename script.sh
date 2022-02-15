#!/bin/bash
files='ls ./*'
for file in $files
do
	echo $file
done

echo $(date)
