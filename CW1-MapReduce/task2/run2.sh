#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output2.out
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/data/output1.out/part-* -output /user/$USER/data/output2.out -mapper mapper2.py -file mapper2.py -reducer reducer2.py -file reducer2.py