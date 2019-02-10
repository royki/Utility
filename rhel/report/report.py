import os
import os.path
import codecs


import xml.etree.ElementTree
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup

from shutil import copyfile

data = open(r'')
root = ET.parse(data).getroot()
# print "Root tag", root.tag
# print "Root attrib", root.attrib

# for child in root:
#    print "Child tag", child.tag 
#    print "Child Attrib", child.attrib
   

# for child in root.iter('testcase'):
#    print child.tag
#    print child.attrib
print "======================================"

for node in root:
   root.findall('failures')

# for node in root.getiterator():  
#    # print "Name", node.get('name')
#    # print "Tag", node.tag
#    # print "Attrib", node.attrib
#    # print "Text", node.text
#    if node.tag == 'failure':
#       print node.get('name')
#       print node.get('message')
#       print node.get('type')
#       print node.text

print "======================================="

length = len(root.findall('testsuite'))
projectName = root.find('testsuite').get('package')
# print projectName
totalTime = 0
totalTestCases = 0
totalTestFailure = 0

for testsuites in root.findall('testsuite'):
    # print "TestSuite name =>" + (testsuites.get('name'))
    # print "TestSuite error =>" + (testsuites.get('errors'))
    # print "TestSuite failure =>" + (testsuites.get('failures'))
    # print "Testcase number =>" + (testsuites.get('tests'))
    # print "TestSuite execution time =>" + (testsuites.get('time'))
    totalTestCases += int(testsuites.get('tests'))
    totalTime += float(testsuites.get('time'))
    totalTestFailure += int(testsuites.get('failures'))
print "TotalExecutionTime ", "%.2f" % totalTime
print "TotalNumberTests " , totalTestCases
print "TotalNumberFailure " , totalTestFailure
successRate = "%.2f" % ((float(totalTestCases) - float(totalTestFailure))/float(totalTestCases)*100)
print "SuccessRate", successRate



# for testcases in root.iter('testcase'):
#     print "All Testcase", (testcases.get('name'))
    # print "testcase Tag ", (testcases.tag)
    # print "testcase attrib", testcases.attrib

for testsuites in root.findall('testsuite'):
   if int(testsuites.get('failures')) !=0:
      print "Failed TestSuite name", testsuites.get('name')
      # print testsuites.tag
      # print testsuites.attrib 
      for testcases in root.getiterator():
         if testcases.tag == 'failure':
            print testcases.get('name')
      #       print testcases.get('message')
      #       print testcases.text


with open(r'H:\Scripts\report\soapresult.html', 'w') as f:
   pass

with open(r'H:\Scripts\report\soapresult.html', 'a') as f:
   f.write('<html><head><meta content="text/html; charset=utf-8" http-equiv="content-type"/>')
   f.write('<title>'+projectName+'</title>')
   #f.write('<style>')
   #f.write(fileCss.read())
   #f.write('</style>')
   f.write('<style>body{margin:0;padding:0;font-family:sans-serif;font-size:12pt}h1{font-size:150%}a{color:#000}#content{padding:5px 30px}#footer{padding:30px;font-size:small;color:#a9a9a9}#footer a{color:#a9a9a9}#navigation{font-size:small;color:#a9a9a9}#navigation a{color:#a9a9a9}.summary-group{display:inline-block;border:solid 2px #D0D0D0;border-radius:10px;margin-right:10px}.summary-group.PASSED{color:green;border-color:green;background-color:#BBD9BB}.summary-group.FAILED{color:#B60808;border-color:#B60808;background-color:#ECDADA}.summary-group.SKIPPED{color:#000;border-color:#a9a9a9;background-color:lightgray}.summary-counter{display:inline-block;text-align:center;padding:20px}.summary-counter .counter{font-weight:700;font-size:130%}#features-section table{border-bottom:solid #D0D0D0 1px;border-collapse:collapse;border-spacing:2px}#features-section th{border-bottom:solid #D0D0D0 1px;white-space:nowrap;text-align:right;padding-left:3em}#features-section th:first-child{padding-left:0;text-align:left}#features-section td{white-space:nowrap;padding-top:5px;padding-bottom:5px;display:table-cell;vertical-align:inherit;text-align:right}#features-section td:first-child{padding-left:0;text-align:left}.result_PASSED{color:green}.result_FAILED{color:#B60808}.spec-output{font-family:monospace;font-size:large;border:1px solid #a9a9a9}div.steps,div.details{font-family:monospace;font-size:10pt;margin-left:10px}div.details{font-size:9pt;border-left:1px #D0D0D0 solid;padding-left:2px}div.steps span.PASSED{font-size:9pt;color:green}div.steps span.FAILED{font-size:9pt;color:#B60808}div.steps span.NOT_PERFORMED{font-size:9pt;color:gray}</style>')
   f.write('</head><body><div id="content"><h1>'+projectName+'</h1><div id="summary-section"><div id="summary"><div class="summary-group"><div class="summary-counter"><div class="counter" id="featureCount">'+str(totalTestCases)+'</div><div class="label">Total Test Cases</div></div>')
   f.write('<div class="summary-counter"><div class="counter" id="failedFeatureCount">'+str(totalTestFailure)+'</div><div class="label">Total Test Failures</div></div>')
   f.write('<div class="summary-counter"><div class="counter" id="specDuration">'+str("%.2f" % (totalTime))+'</div><div class="label">Total Time</div></div></div>')
   f.write('<div class="summary-group FAILED"><div class="summary-counter"><div class="counter" id="successPercentage">'+str(successRate)+'%</div><div class="label">successful</div></div></div>')
   f.write('<div id="features-section"><h3>Specifications</h3>')
   f.write('<div id="features-list"><table><thead><tr><th>Specification</th><th>Features</th><th>Failures</th><th>Duration</th><th>Result</th></tr></thead><tbody>')
   # for testsuites in root.findall('testsuite'):
   #    if (testsuites.get('failures')) == '0':
   for testcases in root.iter('testcase'):
      f.write('<tr><td><a href="" class="result_PASSED">'+testcases.get('name')+'</a></td><td>'+str(1)+'</td><td>'+testsuites.get('failures')+'</td><td>'+testcases.get('time')+'</td><td class="result_PASSED">'+'Passed'+'</td></tr>')
   else:
      for testcases in root.getiterator():
         if testcases.tag == 'failure':               
            f.write('<tr><td><a href="" class="result_FAILED">'+testcases.text+'</a></td><td>'+str(1)+'</td><td>'+testsuites.get('failures')+'</td><td>'+testsuites.get('time')+'</td><td class="result_FAILED">'+'Failed'+'</td></tr>')



      

   
