scriptDir = new File(getClass().protectionDomain.codeSource.location.path).parent
println scriptDir

def inputXmlDir = "${scriptDir}/../../../target/site" as String

def inputXml = "${inputXmlDir}/TESTS-TestSuites.xml"

def outputDir = "${scriptDir}/surefire-reports"

// def filePrefix = "${dataFolder}/../../target/surefire-reports" as String


// //creating filename dynamically.
// def reportFileName = "${filePrefix}/TEST-PAD_API_${fileNamePart}.txt" as String