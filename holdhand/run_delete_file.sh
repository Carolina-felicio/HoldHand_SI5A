# !/bin/bash
for i in `find ./images -mtime +2`
do
sudo rm -f $i
sudo rm -r $i
done