FROM python:3
  
ADD ./ /
COPY ./ /
WORKDIR ./
RUN pip3 install -r requirements.txt

EXPOSE 9999
CMD python3 app.py
