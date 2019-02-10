#!/usr/bin/env python

import sys
import base64
import sha

# Global variables
nonceB64 = sys.argv[1]
timestamp = sys.argv[2]
pwd = sys.argv[3]

# Digest algorithm
def shaTk1Nonce(nonce, timestmp, pswd):  
    shaPwd = sha.new()
    shaPwd.update(pswd)
    result = sha.new()
    result.update( nonce )
    result.update( timestmp )
    result.update( shaPwd.digest() )
    print (base64.b64encode( result.digest() ))
    return base64.b64encode( result.digest() )
    
def processLssToken():
    shaTk1Nonce(nonceB64, timestamp, pwd)
    return

# Main call
processLssToken()