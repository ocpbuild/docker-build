#!/usr/bin/env python

import subprocess
import time
import sys
import os
import re

while True:
    print("Hello from IBM zCX for OpenShift")
    time.sleep(2)

    cmd = 'whoami'
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    sys.stderr.write(result.stderr)
    sys.stdout.write(result.stdout)
    time.sleep(6)
    if result.returncode != 0:
        exit(1)

    cmd = 'id'
    print(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    sys.stderr.write(result.stderr)
    sys.stdout.write(result.stdout)
    time.sleep(6)
    if result.returncode != 0:
        exit(1)

    cmd = 'Python app is running!'
    print(cmd)
    time.sleep(6)
