// From Scripts
def val = testRunner.testCase.testSteps['add'].testRequest.response.getResponseHeaders()["Content-Type"][0]
log.info val
assert val == "text/xml; charset=UTF-8" : "Content type not valid"

// From Scripts Assertions
def val = messageExchange.getResponseHeaders()["Content-Type"][0]
log.info val
assert val == "text/xml; charset=UTF-8" : "Content type not valid"

//all Header values from the response using groovy script.
def val = messageExchange.getResponseHeaders()
val.each
{
    k,v ->
    log.info "name ="+k+", value = "+v
}