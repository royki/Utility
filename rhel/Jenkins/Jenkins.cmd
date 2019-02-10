:: Get list of jobs from Jenkins Host
java -jar jenkins-cli.jar -s http://10.64.114.25:8080/ list-jobs

:: Get and store the setting of one job from Jenkins Host
java -jar jenkins-cli.jar -s http://10.64.114.25:8080/ get-job "job_name" >> job_name.xml

:: Create the job in new Jenkins Host 
java -jar jenkins-cli.jar -s http://10.64.115.166:8080/ get-job "job_name" < job_name.xml