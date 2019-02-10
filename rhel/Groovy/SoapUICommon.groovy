def project = context.testCase.testSuite.project

// Get the Property 
def getPropertyfromTestSuite = project.getTestSuiteByName("APIs and API Versions retrieval");//project.getTestSuiteAt(2)
def getPropertyfromTestCase = getPropertyfromTestSuite.getTestCaseByName("GET-APIs") // testSuite.getTestCaseList()//testSuite.getTestCaseAt(0)
def getPropertyfromTestSteps = getPropertyfromTestCase.getTestStepByName("List_of_APIs") // TestCase.getTestStepAt(7)  //testCase.getTestCaseList().testStepList //
def getPropertyfromTeststepName = getPropertyfromTestSteps.getName().toString()
//log.info getPropertyfromTeststepName
def request = getPropertyfromTestCase.getTestStepByName(getPropertyfromTeststepName)
//def responseContent = testRunner.testCase.getTestStepByName("xxx").getPropertyValue("Response")

def updateTestSuiteAuthent(String testSuiteName, StringToStringMap authent) {
  def testSuite = context.testCase.testSuite.project.getTestSuiteByName(testSuiteName);
  testSuite.each() {
    it.getTestCaseList().each() {
      it.testSteps.each() {
        if(it.getValue().config.type.equals("restrequest") || it.getValue().config.type.equals("request")) {
          it.getValue().getHttpRequest().setRequestHeaders(authent);
        }
      }
    }
  }
}