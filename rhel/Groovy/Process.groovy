// Read OSRid From Valid TestCase, Get the OSRid and ActionID to retrieve the information

import com.eviware.soapui.impl.wsdl.teststeps.*
import com.eviware.soapui.support.types.StringToStringMap 
import groovy.json.*

def project = context.testCase.testSuite.project
def TestSuite = project.getTestSuiteByName("POST-Send action");
def TestCase = TestSuite.getTestCaseByName("OPS_POST_Sends_action_OSR_App_mode_Correct_request") 
def TestSteps = TestCase.getTestStepByName("Get-OSR Status - Simulated") 
def teststepname = TestSteps.getName().toString()
log.info teststepname

def request = TestCase.getTestStepByName(teststepname)
def response = request.getProperty("Response").value

def json = new JsonSlurper().parseText(response)
log.info json.id
log.info json.instance

log.info json.actions.id[0]

def ActionSimulate = testRunner.testCase.getTestStepByName("Get list action")
ActionSimulate.setPropertyValue("osrId", json.id.toString())
ActionSimulate.setPropertyValue("instance", json.instance.toString())
ActionSimulate.setPropertyValue("actionid", json.actions.id[0].toString())