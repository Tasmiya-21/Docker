FROM ubuntu
MAINTAINER Tasmiya 
RUN apt-get update
RUN apt-get install -y python3-pip 
RUN pip install pytest
ADD Calculator.py /home/Calculator.py
ADD max_min.py /home/max_min.py
#CMD ["/home/Calculator.py"]
CMD ["/home/max_min.py"]
ENTRYPOINT ["python3"]
