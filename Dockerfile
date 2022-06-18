FROM icr.io/ibmz/python:3.9.7-bullseye
RUN addgroup -gid 1000 nfsgrp
RUN adduser  --home /home/nfsuser --uid 1000 -gid 1000 --disabled-password --gecos 'Deepti Naphade,3,,,Test'  nfsuser

USER 1000:1000
COPY . .
CMD [ "python", "./python-app.py" ]
