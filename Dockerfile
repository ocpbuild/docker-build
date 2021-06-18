#
# Build using source Docker
#
FROM python:3
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get update && \
    apt-get install -y vim
COPY test_file_read_write_delete.py .
