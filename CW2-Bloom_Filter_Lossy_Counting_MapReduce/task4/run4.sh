#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output4.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /data/assignments/ex2/part3/webLarge.txt \
-output /user/$USER/data/output4.out \
-mapper mapper4.py \
-file mapper4.py \
-reducer reducer4.py \
-file reducer4.py