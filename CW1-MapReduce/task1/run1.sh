#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output1.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /data/assignments/ex1/webLarge.txt -output /user/$USER/data/output1.out -mapper mapper1.py -file mapper1.py -reducer NONE