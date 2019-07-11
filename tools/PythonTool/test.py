#import parse_csv_jp
import parse_csv
import os,sys,csv

LOGFILE="err.log"
file=None
RESULT_FILE='result.csv'

file = open(LOGFILE, 'a')
try:
    if (os.path.isfile(RESULT_FILE)):
        os.remove(RESULT_FILE)
    if (len(sys.argv) >= 3):
        mode = sys.argv[2]

    with open(RESULT_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(
            ["datetime", "eventid", "accountname", "clientaddr", "servicename", "processname", "objectname",
             "sharedname", "result","file"])

    #parse_csv_jp.read_csv(sys.argv[1])
    parse_csv.read_csv(sys.argv[1])

except Exception as e:
    file.write(str(e))
finally:
    file.close()