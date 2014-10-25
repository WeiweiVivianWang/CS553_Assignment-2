************************************************************************************************
*                                                                                              * 
*                      CS553 Assignment#2 ———— WordCounting and Sorting                        *
*                                                                                              *
************************************************************************************************
============
Description:
============
        This assignment requires a wordcount operation implemented by using Shared-Memory, Hadoop and Swift, as well as a sorting operation implemented by all of above and MPI.


==================================
Files included in this assignment:
==================================
        ./src/wordcount/shared-memory/*.py
        ./src/wordcount/shared-memory/runit.sh
        ./src/wordcount/Hadoop/*.jar
        ./src/wordcount/Swift/wordcount.swift
        ./src/wordcount/Swift/*.py


        ./src/sort/shared-memory/*.py
        ./src/sort/shared-memory/runit.sh
        ./src/sort/Hadoop/*.jar
        ./src/sort/Swift/sort.swift
        ./src/sort/Swift/*.py

        ./config/general/local_init.sh
        ./config/general/node_init.sh
        ./config/Hadoop/*.xml
        ./config/Swift/swift.conf
        ./config/Swift/configs
        ./config/MPI/mpi_setup.sh
	./config/MPI/configs

        ./output/wordcount/shared-memory/wordcount-python.txt
        ./output/wordcount/shared-memory/*.png
        ./output/wordcount/Hadoop/wordcount-hadoop.txt
        ./output/wordcount/Swift/wordcount-swift.txt
	./output/wordcount/Swift/run001.log

        ./output/sort/shared-memory/sort1MB-sharedmemory.txt
        ./output/sort/Hadoop/sort1MB-hadoop.txt
        ./output/sort/Swift/sort1MB-swift.txt

	./README.txt
	./prog2_report.pdf


==========================
Details about each folder:
==========================
        ./src/wordcount/shared-memory/
	This folder contains the python source code file of  how to implement the wordcount in the shared-memory way. There are totally four files in it:
            		./WordCountApp.py
            		./WordCountThread.py
            		./WordCountRE.py
            		./runit.sh
            	The bash shell script is used to automatically execute the WordCoutApp.py file more than one time with different threads.
        
        ./src/wordcount/Hadoop/
        	This folder contains the source code of implementation by using Hadoop. 
			./wordcount.jar
        	The bash shell script is used to compile the source code file into a .jar executable file and run it directly.

        ./src/wordcount/Swift/
        	This folder contains the source code file in python and swift script file, with these files we can implement the wordcount using swift language.
        		./wordcount.swift
        		./Mapper.py
        		./Reducer.py
        	The bash shell script do two major tasks, split the 10GB file into small files and then run the swift script.

        ./src/sort/shared-memory/
        	This folder contains the python source code that implement the sorting of 10GB file using external-sorting algorithm.
        		./SortingApp.py
        		./SortingThread.py
			./runit.sh

        ./src/sort/Hadoop/
        	This folder contains the source code file in Java implementing the sorting algorithm using hadoop.
        		./sort.jar

        ./src/sort/Swift/
        	This folder contains the source code file in python and swift script file, with these files we can implement the external sorting using swift language.
        		./sort.swift
        		./Mapper.py
			./Reducer.py

        ./config/general/
        	This folders contains the general script file to config the instance on Amazon EC2, including install JDK, pip, set up hadoop environment and swift environment.
        		./local_init.sh
        		./node_init.sh
        	local_init.sh will be executed on your local computer and it has two arguments, one is your amazon private key and the other one is the public ip of the instance. node_init.sh is the script file that will be actually executed on the amazon EC2 instance.

        ./config/Hadoop/
        	This folder contains the .xml configuration files needed for setting up environment for 16 nodes to work together on Amazon EC2.
        		./masters
        		./slaves
        		./core-site.xml
        		./mapred-site.xml
        		./hdfs-site.xml

        ./config/Swift/
        	This folder contains the configuration files used to set up 16 nodes on Amazon EC2 automatically .
        		./configs
        		./swift_config

        ./output/wordcount/shared-memory/
        	This folder contains the output file and captures of wordcount implemented in python.
        		./wordcount-python.txt
        		./wordcount_result_thread_1.png
        		./wordcount_result_thread_2.png
        		./wordcount_result_thread_4.png
        		./wordcount_result_thread_8.png
        		./wordcount_result_thread_16.png

        ./output/wordcount/Hadoop/
        	This folder contains the output file and captures of wordcount implemented using hadoop.
        		./wordcount-hadoop.txt

        ./output/wordcount/Swift/
        	This folder contains the output file and captures of wordcount implemented using swift language.
        		./wordcount-swift.txt
        		./run001.log

        ./output/sort/shared-memory/
        	This folder contains the output file of  external sorting algorithm implemented in python. Only the first 1MB file is written into the output file.
        		./sort1MB-sharedmemory.txt

        ./output/sort/Hadoop/
        	This folder contains the output file of this sorting problem implemented by using Hadoop. Only the first 1MB file is written into the output file.
        		./sort1MB-hadoop.txt

        ./output/sort/Swift/
        	This folder contains the output file of this sorting problem implemented by using swift language. Only the first 1MB file is written into the output file.
        		./sort1MB-swift.txt


====================================
compile and execute the source code:
====================================
        Shared-Memory Wordcount
		For the shared-memory wordcount, because it is implemented in python and python is installed in every Linux system environment. So we don't need to do anything else.
		This wordcount accept one argument, which is number of threads. So we can run this code by typing the command:
			python WordCountApp.py --t 8
		In this situation, this code will be run by 8 threads concurrently. Or just simply execute runit.sh to execute the program.

        Hadoop Wordcount
        	For the hadoop wordcount, wordcount.jar file is already compiled, so we just need to run this .jar file with hadoop library. Using command like:
	        	bin/hadoop jar wordcount.jar org.wordcount/ZzcWordCount /zzc/input /zzc/output

        Swift Wordcount
        	For the swift wordcount, two python source code need to be executed through that swift script language. To run the swift script, we need to use swift command like:
        		swift wordcount.swift

        Shared-Memory Sort
        	Like the shared-memory wordcount, this code can be run by simplily typing command like:
        		python SortingApp.py --t 8
        	which will have 8 threads to run this code concurrently. Or just simply execute runit.sh to execute the program.

        Hadoop Sort
        	Like wordcount compiling and executing, using command like:
        		bin/hadoop jar sort.jar org.wordcount/ZzcWordCount /zzc/input /zzc/output
        Swift Sort
        	Like wordcount in swift, execute the swift script by using command: 
        		swift sort.swift


===========================
Authors of this assignment:
===========================
Boyang Li 	A20314367
Xingtan Hu	A20304622
Zichen Zhang	A20307812