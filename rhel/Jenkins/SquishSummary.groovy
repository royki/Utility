List getJenkinsTestResultFiles() {
    File squishResultsPath = new File( build.getRootDir(), "squishResults" )
    if ( !squishResultsPath.exists() || !squishResultsPath.isDirectory() ) {
        throw new GroovyRuntimeException( "Squish results path does not exist at: " + squishResultsPath.getAbsolutePath() )
    }

    File summaryFile = new File( squishResultsPath, "summary.xml" )
    if ( !summaryFile.exists() || !summaryFile.isFile() ) {
        throw new GroovyRuntimeException( "Squish summary file does not exist at: " + summaryFile.getAbsolutePath() )
    }

    List resultFiles = []
    def summaries = new XmlSlurper().parse( summaryFile )
    summaries.summary.each {
        resultFiles.push( new File( squishResultsPath, it.xmlFileName.text() ) )
    }

    return resultFiles
}

List getExampleTestResultFiles( File exampleResultsDir ) {
    if ( !exampleResultsDir.exists() || !exampleResultsDir.isDirectory() ) {
        throw new GroovyRuntimeException( "Example test results directory does not exist at: " + exampleResultsDir.getCanonicalPath() )
    }

    return exampleResultsDir.listFiles( new FilenameFilter() {

        public boolean accept( File dir, String name ) {
            return name.endsWith( ".xml" )
        }

    } )
}

void updateEmailDefaultContent( String summary ) {
    def content = msg.getContent()
    assert content.getCount() > 0

    // Assuming the first body part contains the "Default content"
    def defaultContentIndex = 0

    String defaultContent = content.getBodyPart( defaultContentIndex ).getContent()
    if ( defaultContent.contains( "SQUISH_SUMMARY" ) ) {
        defaultContent = defaultContent.replace( "SQUISH_SUMMARY", summary )
    } else {
        defaultContent += summary
    }

    content.getBodyPart( defaultContentIndex ).setContent( defaultContent, "text/html" )
    msg.setContent( content, content.getContentType() )
}

String getTableStyle() {
    return '''\
      table.squishSummary {
        border-collapse: collapse;
      }
      table.squishSummary td, th {
        border: 1px solid black;
        padding: 5px;
      }
      table.squishSummary tr.suiteName {
        background-color: #EEEEEE;
      }
      table.squishSummary th {
        padding: 8px;
      }
      table.squishSummary tr.testCasePassed {
        background-color: #80FF80;
      }
      table.squishSummary tr.testCaseFailed {
        background-color: #FF8080;
      }
    '''
}

String generateHtmlSummary( List squishResultFiles ) {
    def writer = new StringWriter()
    def html = new groovy.xml.MarkupBuilder( writer )

    html.table( class: "squishSummary" ) {
        style( type: "text/css" ) {
            mkp.yield( getTableStyle() )
        }
        squishResultFiles.each {
            def squishReport = new XmlSlurper().parse( it )

            // For each test suite
            squishReport.test.each {
                def suiteName = it.@name.text()
                tr( class: "suiteName" ) {
                    th {
                        mkp.yield( suiteName )
                    }
                }

                // For each test case
                it.test.each {
                    def result = it.depthFirst().find() {
                        it[ "@type" ] == "FAIL" ||
                        it[ "@type" ] == "XPASS" ||
                        it[ "@type" ] == "FATAL" ||
                        it[ "@type" ] == "ERROR"
                    }
                    def testCaseName = it.@name.text()
                    def testCaseFailed = result != null && result.size() > 0
                    tr( class: ( testCaseFailed ? "testCaseFailed" : "testCasePassed" ) ) {
                        td {
                            mkp.yield( testCaseName )
                        }
                    }
                }
            }
        }
    }

    return writer.toString()
}

boolean getExecuteWithinJenkins() {
    try {
        // TODO Find a better way to check if the args property exists or not.
        args.size()
    } catch ( MissingPropertyException ) {
        return true
    }
    return false
}

/*
 * To test the generated HTML summary outside of Jenkins a directory which
 * contains Squish XML result files can be passed as first and only argument
 * to this script. The HTML summary file will be written into the same
 * directory.
 */
void main() {
    def executeWithinJenkins = getExecuteWithinJenkins()

    def squishResultFiles = []
    def exampleResultsDir = null

    if ( executeWithinJenkins ){
        squishResultFiles = getJenkinsTestResultFiles()
    } else {
        if ( args.size() != 1 ) {
            throw new GroovyRuntimeException( "Expected path to Squish test results folder as only argument" )
        }
        exampleResultsDir = new File( args[ 0 ] )
        squishResultFiles = getExampleTestResultFiles( exampleResultsDir )
    }

    def summary = generateHtmlSummary( squishResultFiles )

    if ( executeWithinJenkins ) {
        updateEmailDefaultContent( summary )
    } else {
        new File( exampleResultsDir, "summary.html" ).withWriter { out ->
            out.writeLine( summary )
        }
    }
}

main()
