import json
import csv
import re
import glob

filelist = []
extlist = [".gz",".sh",".tar",".zip",".jar",".war"]

for item in glob.glob("./*.json"):
  filelist.append(item)

code_re = re.compile(r'\.\/(?P<code_type>\S+)\_(?P<ip>\S+).json')

with open('logchecklist.csv', 'w') as csvfile:
  fieldname = ['code_type', 'ip', 'path', 'filename']
  csvwriter = csv.DictWriter(csvfile,fieldnames=fieldname)
  csvwriter.writeheader()
  for filename in filelist:
    print(filename)
    code_type = code_re.match(filename)
    with open(filename, 'r') as resultfile:
      result = json.load(resultfile)
      for item in result:
        path = item['item']
        projectlogpath = item['stdout_lines']
        for logitem in projectlogpath:
          if any(ext in logitem for ext in extlist):
            continue
          else:
            csvwriter.writerow({'code_type': code_type.groupdict('code_type').get('code_type'),'ip': code_type.groupdict('ip').get('ip'), 'path':path,'filename':logitem})