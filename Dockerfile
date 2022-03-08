FROM ubuntu
MAINTAINER Tasmiya 
RUN apt-get update
RUN apt-get install -y python
ADD check.py /home/check.py
CMD ["/home/check.py"]
ENTRYPOINT ["python"]
