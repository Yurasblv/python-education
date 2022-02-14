#!/bin/bash
echo 'Time'
files='ls ./*'
for file in $files
do
	echo $file
done

echo $(date)

