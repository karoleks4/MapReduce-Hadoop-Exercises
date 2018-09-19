#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output6.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/data/output4.out/part-* -output /user/$USER/data/output6.out -mapper mapper6.py -file mapper6.py -reducer reducer6.py -file reducer6.py