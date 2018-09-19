#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output8.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapred.reduce.tasks=1 -input /user/$USER/data/output7.out/part-* -output /user/$USER/data/output8.out -mapper mapper8.py -file mapper8.py -reducer reducer8.py -file reducer8.py