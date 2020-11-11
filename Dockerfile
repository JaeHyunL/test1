FROM python:3
<<<<<<< HEAD
  
ADD ./ /
COPY ./ /
WORKDIR ./
RUN pip3 install -r requirements.txt
=======

ADD ./ /
COPY ./ / 
WORKDIR ./ 
RUN pip3 install -r requirementes.txt
>>>>>>> 056a044edd44ea2912ad115ae85f1f4fcfbdb273

EXPOSE 9999
CMD python3 app.py
