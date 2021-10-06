#!/bin/bash

for i in {1..2000}; do	python3 maaklogs.py > log_`date -I -d "2016-03-26 +$i days"`.log; echo $i; done

