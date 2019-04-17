# Detecting attacks leveraging vulnerability fixed in MS17-010 from Event Log

This is a detection tool for detecting attack  leveraging vulnerability fixed in MS17-010 from Event Log.<br>
The tool is implemented by Java, and tested in Java 1.8.

## How to use
1. Export Event Log (Security) as CSV file using the standard function of Event viewer<br/>
    Right click Security Logs-> "Save All Event As.." -> Select CSV file type
2. Execute parse tool as follows<br/>
Usage: java logparse/DetectEternalblueDoublepulsar2008 [inputdirname] [outputdirname]<br/>
  inputdirname: full path of the directory in which Event Logs are put<br/>
  outputdirname: full path of the directory in which detection result is put<br/>
The tool is provided as Eclipse format, so you can also execute the tool  on Eclipse.
  
Example of useage:<br/>
$ cd doublepalserdetection/tools/LogParserForDoublePalser/bin<br/>
$ java logparse/DetectEternalblueDoublepulsar2008 /tmp/input /tmp/output<br/>

####	Input of the tools: Event logs of the target computer. 
* 4673: A privileged service was called
* 4688: A new process was created
* 5140: A network share object was accessed

###	Output (result) of the tool
* Distinguish logs recorded by attack activities from logs recorded by normal operations, and identity infected computers. <br>
 * If "attack"  column is "1": The Event may be recorded by attacks
 * If "attack"  column is "0": The Event may be recorded by normal operations

###	Requirements
* OS of the target computer: Windows 2008R2  
