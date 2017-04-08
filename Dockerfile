FROM alpine:latest

RUN apk -U add python py-pip

COPY requirements.txt /run/requirements.txt

RUN /usr/bin/pip install -r /run/requirements.txt

COPY app.py /run/app.py
COPY z.gif     /run/z.gif

EXPOSE 8080

WORKDIR /run/

CMD /usr/bin/python /run/app.py
ENTRYPOINT /usr/bin/python /run/app.py
