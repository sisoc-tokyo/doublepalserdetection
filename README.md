# Detecting attacks leveraging vulnerabilities fixed in MS17-010 from Event Log

This is a detection tool for detecting attack  leveraging vulnerability fixed in MS17-010 from Event Log.<br>
The tool is implemented by Pyrhon 3.

## How to use
1. Export Event Log (Security) as CSV file using the standard function of Event viewer<br/>
    Right click Security Logs-> "Save All Event As.." -> Select CSV file type
2. Execute a tool as follows<br/>
$ cd tools/PythonTool/
$ python test.py [inputdirname]
  inputdirname: full path of the directory in which Event Logs are put<br/>
  
####	Input of the tools: Event logs of the target computer. 
* 4624: 
* 4688: A new process was created
* 4776: 
* 5140: A network share object was accessed

###	Output (result) of the tool
* Distinguish logs recorded by attack activities from logs recorded by normal operations, and identity infected computers. <br>
result.csv will be created in the current directory.<br>
 * If "result"  column is "attack": The Event may be recorded by attacks
 * If "result"  column is "normal": The Event may be recorded by normal operations

###	Requirements
* Supported  OS of the target computer: Windows 2016, 10, 2012 R2, 8.1, 2008R2 ,7 
