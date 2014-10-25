#! /bin/sh

chmod +x WordCountApp.py

for i in 1, 2, 4, 8, 16
do
	python WordCountApp.py --t $i
        mkdir wordcount_result_thread_$i
	mv output_key output_value /wordcount_result_thread_$i/
done

