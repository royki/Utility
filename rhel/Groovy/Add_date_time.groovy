def updateAttachmentName(String testStepName) {
	Calendar cal = Calendar.getInstance();
	cal.setTime(new Date());
	cal.add(Calendar.HOUR_OF_DAY, 1);
	def date = cal.getTime().format("yyMMdd");
	log.info("Date:"+date);
	def time = cal.getTime().format("HHmmss");
	log.info("Time:"+time);
	def attachment1 = testRunner.testCase.getTestStepByName(testStepName).httpRequest.getAttachmentAt(0);
	attachment1.name = "APP-SIOSR-DEV-"+date+"-"+time+"-123456789.zip";
}

updateAttachmentName("Create_OSR_with_zip_file");