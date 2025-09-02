FROM python 
WORKDIR /home/app
COPY . /home/app
RUN pip install -r requirements.txt 
CMD python3 -u /home/app/worker.py