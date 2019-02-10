import os
import os.path
import codecs
import re
import fileinput

#set css style for email template
def setCssStyle(file):
	oldCss='<link rel="stylesheet" type="text/css" href="style/damage-control.css"/>'
	newCss="""<style>body{margin:0;padding:0;font-family:sans-serif;font-size:12pt}h1{font-size:150%}#footer,#navigation{font-size:small;color:#a9a9a9}a{color:#000}#content{padding:5px 30px}
    #footer{padding:30px}#footer a,#navigation a{color:#a9a9a9}.summary-group{display:inline-block;border:2px solid #D0D0D0;border-radius:10px;margin-right:10px}
    .summary-group.PASSED{color:green;border-color:green;background-color:#BBD9BB}.summary-group.FAILED{color:#B60808;border-color:#B60808;background-color:#ECDADA}
    .summary-group.SKIPPED{color:#000;border-color:#a9a9a9;background-color:#d3d3d3}.summary-counter{display:inline-block;text-align:center;padding:20px}
    .summary-counter .counter{font-weight:700;font-size:130%}#features-section table{border-bottom:solid #D0D0D0 1px;border-collapse:collapse;border-spacing:2px}
    #features-section th{border-bottom:solid #D0D0D0 1px;white-space:nowrap;text-align:right;padding-left:3em}#features-section td:first-child,#features-section
    th:first-child{padding-left:0;text-align:left}#features-section td{white-space:nowrap;padding-top:5px;padding-bottom:5px;display:table-cell;vertical-align:inherit;text-align:right}
    .result_PASSED{color:green}.result_FAILED{color:#B60808}.spec-output{font-family:monospace;font-size:large;border:1px solid #a9a9a9}
    div.details,div.steps{font-family:monospace;font-size:10pt;margin-left:10px}div.details{font-size:9pt;border-left:1px #D0D0D0 solid;padding-left:2px}
    div.steps span.PASSED{font-size:9pt;color:green}div.steps span.FAILED{font-size:9pt;color:#B60808}div.steps span.NOT_PERFORMED{font-size:9pt;color:gray}</style>"""

	oldJs='<script type="text/javascript" src="js/damage-control.js"></script>'
	newJs="""<script>>!function(){"use strict";$(document).ready(function(){$("[expand]").hover(function(a){$(a.target).css("cursor","pointer"),$(a.target).css("text-decoration","underline")},
    function(a){$(a.target).css("cursor","auto"),$(a.target).css("text-decoration","none")}),$("[expand]").on("click",function(a){var b=$(a.target).attr("expand");$("[expandable="+b+"]").toggle()}),
    $("[expandable]").hide()})}();</script>"""
	oldJqry='<script type="text/javascript" src="js/jquery.min.js"></script>'
	newJqry='<script type="text/javascript" src="https://code.jquery.com/jquery-3.1.0.min.js"></script>'

	for line in fileinput.FileInput(file,inplace=1):
	   line = line.replace(oldCss,newCss)
	   line = line.replace(oldJs,newJs)
	   line = line.replace(oldJqry,newJqry)
	   print line



#remove packaging path from the full name
def cutClassName(file, prefix ):
	f=codecs.open(file, 'r')
	text = f.read()
	text = text.replace(prefix, "")
	print text
	with open(file, 'w') as f:
		f.write(text)



#convert seconds to HH:MM:SS
def convertDuration(file):
	f=codecs.open(file, 'r')
	text = f.read()
	duration= re.search('id="specDuration">(.*?)s</div>', text).group(1)
	seconds= int(float(duration))
	hours = seconds // (60*60)
	seconds %= (60*60)
	minutes = seconds // 60
	seconds %= 60
	text = text.replace(duration+"s", str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+"s")
	with open(file, 'w') as f:
		f.write(text)


filePath="D:\\jenkins\\workspace\\UI-Regression_Framework\\target\\damage-control-reports\\index.html"
prefix="com.app.ui"
#Call to methods
setCssStyle(filePath)
cutClassName(filePath, prefix)
convertDuration(filePath)