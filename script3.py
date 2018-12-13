'''
Created on Dec 12, 2018
@author: Lusanic
'''
import os
import csv
import requests
import xml.etree.ElementTree as ET

def runCoverage():
    print("testing now")
    allTests = open('all-files.txt', 'w')
    check = "com.google.javascript.jscomp.CreateSyntheticBlocksTest"
    for line in allTests:
        line = line.split("(")
        method = line[0]
        path = line[1].split(")")[0]
        if path == check and method != "testIssue291":
            os.system("defects4j coverage -t "+path+"::"+method)
            os.system("cat coverage.xml")
            name = method+".xml"
            os.system("mv coverage.xml "+name)
            os.system("mv /tmp/closure_87_buggy/"+name +" /tmp/closure_87_buggy_3/passedXml/")
    else:
        pass
    return None    
   
if __name__=='__main__':
  runCoverage()
