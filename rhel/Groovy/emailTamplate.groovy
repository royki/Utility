currentDir = new File(".").getAbsolutePath()
println("currentDir =>" + currentDir)

def inputCssDir = "${currentDir}/target/damage-control-reports"
def inputCssFile = "${inputCssDir}/style/damage-control.css" as String
def outputDir = "${inputCssDir}"

def engine = new groovy.text.SimpleTemplateEngine()
def writeCaseData = {
	
}