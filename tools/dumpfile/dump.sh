#!/bin/bash
date=`date +"%m%d"`
echo $date
pid=`pgrep -u friends`
echo $pid
/usr/lib/jvm/java-7-oracle/bin/jmap -F -dump:file=/mnt/dump_$date.txt $pid

du -h /mnt/dump_$date.txt
