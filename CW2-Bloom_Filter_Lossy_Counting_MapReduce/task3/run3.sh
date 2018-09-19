#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output3.out

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/data/inter3 \
-mapper mapper3.py \
-file mapper3.py \
-reducer reducer3.py \
-file reducer3.py

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /user/$USER/data/inter3/part-* \
-output /user/$USER/data/output3.out \
-mapper mapper3_2.py \
-file mapper3_2.py \
-reducer reducer3_2.py \
-file reducer3_2.py

hdfs dfs -rm -r /user/$USER/data/inter3