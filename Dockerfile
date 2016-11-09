FROM alpine:latest

RUN apk -U add python py-pip

COPY requirements.txt /root/requirements.txt

RUN /usr/bin/pip install -r /root/requirements.txt

COPY script.py /app/script.py
COPY z.gif     /app/z.gif

EXPOSE 8080

WORKDIR /app/

CMD /usr/bin/python /app/script.py
ENTRYPOINT /usr/bin/python /app/script.py
