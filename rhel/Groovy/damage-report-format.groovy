currentDir = new File(".").getAbsolutePath()
println("currentDir =>" + currentDir)

//Provide the path of the report xml
def inputXmlDir = "${currentDir}/target"
def inputXmlFile = "${inputXmlDir}/site/TESTS-TestSuites.xml" as String

// Define the location where files needs to be written
def outputDir = "${inputXmlDir}/surefire-reports"

def templateXml = '''<?xml version="1.0" encoding="UTF-8"?> 
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="$packageName-$suite-$caseName" time="$caseTime" tests="$tests" errors="$errors" skipped="$skipped" failures="$failures"> 
    <testcase name="runTest" classname="$packageName-$suite-$caseName" time="$caseTime"> </testcase>
</testsuite>'''

def templateFailXml = '''<?xml version="1.0" encoding="UTF-8"?> 
<testsuite xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://maven.apache.org/surefire/maven-surefire-plugin/xsd/surefire-test-report.xsd" name="$packageName-$suite-$caseName" time="$caseTime" tests="$tests" errors="$errors" skipped="$skipped" failures="$failures"> 
    <testcase name="runTest" classname="$packageName-$suite-$caseName" time="$caseTime">
         <error type="$caseName"><![CDATA[$failedMessage]]></error>
    </testcase>
</testsuite>'''

def binding = [failures:'0', errors: '0', skipped:'0', suiteTime: '0.00', caseTime:'0.00', caseName:'', tests: '1', suite: '', failedMessage: '', packageName:'']

def xml = new XmlSlurper().parseText(new File(inputXmlFile).text)
def testcases = xml.'**'.findAll{it.name() == 'testcase'}
def engine = new groovy.text.SimpleTemplateEngine()

//Save the contents to a file
def saveToFile(file, content) {
    if (!file.parentFile.exists()) {
         file.parentFile.mkdirs()
         println "Directory did not exist, created for damage-control-report"
    }
    file.write(content) 
    assert file.exists(), "${file.name} not created"
}

def writeCaseData = { kase ->
    def tempXml = templateXml
    def bindingKase = binding.clone()
    bindingKase.errors = kase.parent().@errors
    bindingKase.suiteTime = kase.parent().@time
    bindingKase.suite = kase.parent().@name
    bindingKase.packageName = kase.parent().@package
    bindingKase.caseName = kase.@name
    bindingKase.caseTime = kase.@time
    if (kase.failure.size()) {
        bindingKase.errors = '1'
        bindingKase.failedMessage = kase.failure.text()
        tempXml = templateFailXml
    }
    def template = engine.createTemplate(tempXml).make(bindingKase)
    saveToFile(new File("${outputDir}/TEST-${bindingKase.packageName}-${kase.parent().@name}-${kase.@name}.xml"), template.toString())
}

testcases.each { writeCaseData it }