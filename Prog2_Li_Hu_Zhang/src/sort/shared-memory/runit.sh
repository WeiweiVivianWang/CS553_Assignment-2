#! /bin/sh

chmod +x SortingApp.py

for i in 1, 2, 4, 8
do
	python SortingApp.py --t $i
        mkdir sorting_result_thread_$i
	mv output /sorting_result_thread_$i/
done

