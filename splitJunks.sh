#!/bin/bash
FILE=$1 
LINES=`wc -l $FILE | awk '{print $1}' | grep .`
echo $LINES
for i in 2 4 8 16 32 64 128 256  
do
	mkdir -p /tmp/JUNKS_${i}
	JUNKSIZE=`expr $LINES / $i`
	START=1
	END=${JUNKSIZE}
	echo "><<<<<<<<<<<<<<<<<<<<<< FOR JUNKS of $i <<<<<<<<<<<<<<<<<<<<<<<<<"
 	for j in `seq $i`
	do
		sed -n "${START},${END}p" ${FILE}  > /tmp/JUNKS_${i}/part_${START}_${END}__${j}.json
		echo $START $END
		START=`expr $START + ${JUNKSIZE} + 1`
		END=`expr ${END} + ${JUNKSIZE} + 1`
	done
done
