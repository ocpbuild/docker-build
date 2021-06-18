import subprocess
import time
import sys

while true:
  print('Hello World")
  time.sleep(2)
  cmd = 'echo hello > newfile'
  print(cmd)
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  sys.stderr.write('result.stderr\n')
  sys.stdout.write('result.stdout\n')  
  time.sleep(60)
