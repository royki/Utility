import com.eviware.soapui.impl.wsdl.teststeps.*
import com.eviware.soapui.support.types.StringToStringMap 
import groovy.json.*

def project = context.testCase.testSuite.project
def TestSuite = project.getTestSuiteByName("APIs")
def TestCase =  TestSuite.getTestCaseList() 
def TestStep = TestCase.testStepList
def request =  testRunner.testCase.getTestStepByName("List_of_APIs_OrderByID_ASC")
def response = request.getPropertyValue("Response")
def JsonSlurperResponse = new JsonSlurper().parseText(response)
def Steps = TestStep.drop(3)
def n =  TestStep.getAt(1).name[0]

Steps.each {
	//it.getAt(0).setPropertyValue("apiId", id1)   
	//log.info it.getAt(0).name     	
}

// log.info JsonSlurperResponse.data.id

//Steps.each{
//	it.getAt(0).setPropertyValue("apiId", id1)   
//	log.info it.getAt(0).name     	
//}
//
//def _id = JsonSlurperResponse.data.id
//_id.each {
//	log.info it
//}
//
//
//Steps.each{
//	it.getAt(0).setPropertyValue("apiId", _id.each{it as String})
//}


// def getID1 =  TestStep.getAt(1).name[0].getProperty("Response").value

return