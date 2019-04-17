# Detecting attacks leveraging vulnerability fixed in MS17-010 from Event Log

This is a detection tool for detecting attack  leveraging vulnerability fixed in MS17-010 from Event Log.
The tool is implemented by Java, and tested in Java 1.8 

## How to use
1. Export Event Log (Security) as CSV file using the standard function of Event viewer<br/>
    Right click Security Logs-> "Save All Event As.." -> Select CSV file type
2. Execute parse tool as follows
Usage: java logparse/DetectEternalblueDoublepulsar2008 [inputdirname] [outputdirname]
  inputdirname: full path of the directory in which Event Logs are put
  outputdirname: full path of the directory in which detection result is put
Example of useage:
$ cd doublepalserdetection/tools/LogParserForDoublePalser/bin
$ java logparse/DetectEternalblueDoublepulsar2008 /tmp/input /tmp/output

####	Input of the tools: Event logs of the target computer. 
* 4673: An operation was attempted on a privileged object
* 4688: A new process was created
* 5140: A network share object was accessed

###	Output (result) of the tool
* Distinguish logs recorded by attack activities from logs recorded by normal operations, and identity infected computers. <br>
 ** If "attack"  column is "1": The Event may be recorded by attacks
 ** If "attack"  column is "0": The Event may be recorded by normal operations

###	Requirements
* OS of the target computer: Windows 2008R2  
