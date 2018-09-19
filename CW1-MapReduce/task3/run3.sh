#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output3.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapred.reduce.tasks=1  -input /user/$USER/data/output2.out/part-* -output /user/$USER/data/output3.out -mapper mapper3.py -file mapper3.py -reducer reducer3.py -file reducer3.py