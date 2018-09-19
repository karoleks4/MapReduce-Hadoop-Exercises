#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output2.out

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapred.reduce.tasks=1 \
-D mapreduce.partition.keycomparator.options=-k1nr \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/data/output2.out \
-mapper mapper2.py \
-file mapper2.py \
-reducer reducer2.py \
-file reducer2.py