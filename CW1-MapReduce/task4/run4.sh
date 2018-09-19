#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output4.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/data/output2.out/part-* -output /user/$USER/data/output4.out -mapper mapper4.py -file mapper4.py -reducer reducer4.py -file reducer4.py