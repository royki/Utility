#!D:\Software\cygwin64\bin\bash
totalNoOfTestFailed=`cat TESTS-TestSuites.xml | grep "<testsuite" | tr -s " "| cut -d " " -f3,4 | cut -c9,22 | sed 's/\"//g' | paste -sd+ | bc`
echo $totalNoOfTestFailed
