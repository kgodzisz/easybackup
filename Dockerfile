FROM ubuntu

RUN apt-get update && \
    apt-get install -y tar gzip bzip2 python3

COPY easybackup.py .

ENTRYPOINT ["python3", "easybackup.py"]
