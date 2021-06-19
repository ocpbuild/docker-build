#
# Test container Dockerfile
#
FROM sys-z-test-docker-local.artifactory.swg-devops.com/python:3
MAINTAINER Deepti Naphade "dnaphade@us.ibm.cm"

COPY . .

CMD [ "python", "./python-app.py" ]
