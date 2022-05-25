FROM python:3.10
MAINTAINER yurasblv.y@gmail.com
ENV PYTHONUNBUFFERED 1
WORKDIR data
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","main.py"]