#!/usr/bin/env python

import subprocess
import time
import sys
import os
import re

while True:
  print("Hello World")
  time.sleep(2)
  os.chdir("/targetdir")

  cmd = 'echo create a new file with string deepti > myfile'
  print(cmd)
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

  sys.stderr.write(result.stderr)
  sys.stdout.write(result.stdout)
  time.sleep(6)
  if result.returncode != 0:
    exit(1)

  cmd = 'echo append second line to text file >> myfile'
  print(cmd)
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

  sys.stderr.write(result.stderr)
  sys.stdout.write(result.stdout)
  time.sleep(6)
  if result.returncode != 0:
    exit(1)
  
  cmd = 'cat myfile'
  print(cmd)
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  if not re.search("deepti", result.stdout):
    exit(1)
  if not re.search("append", result.stdout):
    exit(1)
  else:
    sys.stderr.write(result.stderr)
    sys.stdout.write(result.stdout)
  time.sleep(6)

  cmd = 'rm myfile'
  print(cmd)
  result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  sys.stderr.write(result.stderr)
  sys.stdout.write(result.stdout)
  time.sleep(6)
  if result.returncode != 0:
    exit(1)
