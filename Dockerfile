FROM ubuntu
MAINTAINER Tasmiya 
RUN apt-get update
RUN apt-get install -y python
ADD Calculator.py /home/Calculator.py
CMD ["/home/Calculator.py"]
ENTRYPOINT ["python"]
