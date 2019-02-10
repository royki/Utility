// Read OSRid from Valid Testcase
import com.eviware.soapui.impl.wsdl.teststeps.*
import com.eviware.soapui.support.types.StringToStringMap 
import groovy.json.*

def project = context.testCase.testSuite.project
def TestSuite = project.getTestSuiteByName("POST-Send action");//project.getTestSuiteAt(2)
def TestCase = TestSuite.getTestCaseByName("OPS_POST_Sends_action_OSR_App_mode_Correct_request") // testSuite.getTestCaseList()//testSuite.getTestCaseAt(0)
def TestSteps = TestCase.getTestStepByName("Get-OSR Status - Cancel") //TestCase.getTestStepAt(1)  //testCase.getTestCaseList().testStepList //
def teststepname = TestSteps.getName().toString()
//log.info teststepname

// Get the Property 
def request = TestCase.getTestStepByName(teststepname)
def response = request.getProperty("Response").value
// log.info response
def json = new JsonSlurper().parseText(response)
log.info json.id
log.info json.instance

// Set the Property
def SetProperty = testRunner.testCase.getTestStepByName("Get-OSR Status")
SetProperty.setPropertyValue("id", json.id.toString())
SetProperty.setPropertyValue("instance", json.instance.toString())