import os
import os.path
import codecs


from BeautifulSoup import BeautifulSoup

fileCss=open(r'\\nceshtalm0620\data\APIDeploy\stylesheet.css')

with open(r'\\nceshtalm0620\data\APIDeploy\report.html', 'a') as f:
    f.write('<style>')
    f.write(fileCss.read())
    f.write('</style>')

#           Junit with Frame
# fileAmpAppOverViewSummery = open(r'\\nceshtalm0620\data\shrek\AMPApp\overview-summary.html')
# #fileAmpAppPackageSummery = open(r'\\nceshtalm0620\data\shrek\AMPApp\AMP_ApplicationMode\package-summary.html')
# fileAmpGhostOverViewSummery = open(r'\\nceshtalm0620\data\shrek\AMPGhost\overview-summary.html')
# #fileAmpGhostPackageSummery = open(r'\\nceshtalm0620\data\shrek\AMPGhost\AMP_GhostMode\package-summary.html')
# fileOpsAppOverViewSummery =  open(r'\\nceshtalm0620\data\shrek\OPSApp\overview-summary.html')
# fileOpsAppPackageSummery =  open(r'\\nceshtalm0620\data\shrek\OPSApp\OPS_ApplicationMode\package-summary.html')
# fileOpsGhostOverViewSummery = open(r'\\nceshtalm0620\data\shrek\OPSGhost\overview-summary.html')
# fileOpsGhostPackageSummery = open(r'\\nceshtalm0620\data\shrek\OPSGhost\OPS_GhostMode\package-summary.html')

# with open(r'\\nceshtalm0620\data\shrek\report.html', 'a') as f:
#     f.write(fileAmpAppOverViewSummery.read())
#     f.write(fileAmpAppPackageSummery.read())
#     f.write(fileAmpGhostOverViewSummery.read())
#     f.write(fileAmpGhostPackageSummery.read())
#     f.write(fileOpsAppOverViewSummery.read())
#     f.write(fileOpsAppPackageSummery.read())
#     f.write(fileOpsGhostOverViewSummery.read())
#     f.write(fileOpsGhostPackageSummery.read())

# with open(r'\\nceshtalm0620\data\shrek\report.html', 'a') as f:
#     f.write(fileAmpAppOverViewSummery.read())
#     f.write(fileAmpAppPackageSummery.read())
#     f.write(fileAmpGhostOverViewSummery.read())
#     f.write(fileAmpGhostPackageSummery.read())
#     f.write(fileOpsAppOverViewSummery.read())
#     f.write(fileOpsAppPackageSummery.read())
#     f.write(fileOpsGhostOverViewSummery.read())
#     f.write(fileOpsGhostPackageSummery.read())



#           Junit with noFrame
fileAmpAppReport = open(r'\\nceshtalm0620\data\APIDeploy\AMPApp\junit-noframes.html')
fileAmpGhostReport = open(r'\\nceshtalm0620\data\APIDeploy\AMPGhost\junit-noframes.html')
fileOpsAppReport =  open(r'\\nceshtalm0620\data\APIDeploy\OPSApp\junit-noframes.html')
fileOpsGhostReport = open(r'\\nceshtalm0620\data\APIDeploy\OPSGhost\junit-noframes.html')
fileAfdAppReport = open(r'\\nceshtalm0620\data\APIDeploy\AFDApp\junit-noframes.html')

with open(r'\\nceshtalm0620\data\APIDeploy\report.html', 'a') as f:
    f.write(fileAmpAppReport.read())
    f.write(fileAmpGhostReport.read())
    f.write(fileOpsAppReport.read())
    f.write(fileOpsGhostReport.read())
    f.write(fileAfdAppReport.read())


with open(r'\\nceshtalm0620\data\APIDeploy\report.html', 'a') as f:
    f.write('<style>')
    f.write(fileCss.read())
    f.write('</style>')


f=codecs.open(r'\\nceshtalm0620\data\APIDeploy\report.html')
text = f.read()
text = text.replace("Unit Test Results: Summary", "")
text = text.replace("Unit Test Results.", "")
soup = BeautifulSoup(text)
for a in soup.findAll('a'):
    del a['href']
text = str(soup)
text = text.replace("Designed for use with <a>JUnit</a> and <a>Ant</a>.", "")


with open(r'\\nceshtalm0620\data\APIDeploy\report.html', 'w') as f:
    f.write(text)
