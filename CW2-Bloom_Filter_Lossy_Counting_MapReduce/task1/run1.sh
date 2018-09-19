#!/bin/bash
#hdfs dfs -rm -r /user/$USER/data/output1
#Change the output file!!!!


# hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
#  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
#  -D mapreduce.map.output.key.field.separator=" " \
#  -D stream.map.output.field.separator=" " \
#  -D stream.num.map.output.key.fields=2 \
#  -D num.key.fields.for.partition=1 \
#  -input /data/assignments/ex2/part1/large \
#  -output /user/$USER/data/output1 \
#  -mapper mapper1.py \
#  -file mapper1.py \
#  -combiner combiner1.py \
#  -file combiner1.py \
#  -reducer reducer1.py \
#  -file reducer1.py \
#  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /data/assignments/ex2/part1/large \
 -output /user/$USER/data/output1.out \
 -mapper mapper1.py \
 -file mapper1.py \
 -combiner combiner1.py \
 -file combiner1.py \
 -reducer reducer1.py \
 -file reducer1.py