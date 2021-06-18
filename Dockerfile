#
# Test env setup container Dockerfile
#
FROM sys-z-test-docker-local.artifactory.swg-devops.com:ubuntu
MAINTAINER Deepti Naphade "dnaphade@us.ibm.com"
RUN apt-get update && apt-get -y install python3
ADD python-app.py /pv-test/
WORKDIR /pv-test
CMD ["python3", "python-app.py"]

