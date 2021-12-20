FROM python:3.8.9

ADD main.py .

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

COPY run.sh /tmp/run.sh

RUN chmod a+x /tmp/run.sh

COPY producer.py /tmp/producer.py

RUN chmod a+x /tmp/producer.py

COPY consumer.py /tmp/consumer.py

RUN chmod a+x /tmp/consumer.py

COPY main.py /tmp/main.py

RUN chmod a+x /tmp/main.py

COPY app.py /tmp/app.py

RUN chmod a+x /tmp/app.py

COPY /templates/base.html /tmp/templates/base.html

RUN chmod a+x /tmp/templates/base.html

COPY /templates/home.html /tmp/templates/home.html

RUN chmod a+x /tmp/templates/home.html

COPY /templates/login.html /tmp/templates/login.html

RUN chmod a+x /tmp/templates/login.html

COPY /templates/signup.html /tmp/templates/signup.html

RUN chmod a+x /tmp/templates/signup.html

COPY /templates/transport.html /tmp/templates/transport.html

RUN chmod a+x /tmp/templates/transport.html

COPY database.db /tmp/database.db

RUN chmod a+x /tmp/database.db

COPY /templates/data.txt /tmp/templates/data.txt

RUN chmod a+x /tmp/templates/data.txt

EXPOSE 5000

CMD ["/tmp/run.sh"]