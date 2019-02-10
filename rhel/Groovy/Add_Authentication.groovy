import com.eviware.soapui.impl.wsdl.teststeps.*;
import com.eviware.soapui.support.types.StringToStringMap;

def authentAdminIntegrator = new StringToStringMap();
authentAdminIntegrator.put("idToken", "XXX");
authentAdminIntegrator.put("accessToken", "XXX");

def authentMagOperator = new StringToStringMap();
authentMagOperator.put("idToken", "XXX");
authentMagOperator.put("accessToken", "XXX");

def authentConfReader = new StringToStringMap();
authentConfReader.put("idToken", "XXX");
authentConfReader.put("accessToken", "XXX");

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

updateTestSuiteAuthent("POST-Create OSR", authentAdminIntegrator);
updateTestSuiteAuthent("POST-Send action", authentMagOperator);
updateTestSuiteAuthent("GET content OSR", authentConfReader);
updateTestSuiteAuthent("GET Retrieve list of action", authentConfReader);
updateTestSuiteAuthent("GET content of action", authentConfReader);
updateTestSuiteAuthent("GET SAP", authentConfReader);
updateTestSuiteAuthent("GET Retrieve content of a report", authentConfReader);
updateTestSuiteAuthent("GET ReportsByAction", authentConfReader);
updateTestSuiteAuthent("GET OSRsWithFilter", authentConfReader);
updateTestSuiteAuthent("Error Management", authentAdminIntegrator);

return;