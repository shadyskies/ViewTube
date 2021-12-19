# run django server from docker container


FROM python:3.9

COPY cron.d /etc/cron.d/
RUN chmod 0644 /etc/cron.d/*

# copy source and install dependencies
RUN mkdir -p /app
COPY . /app

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN touch /var/log/cron.log

RUN chmod +x /app/start-server.sh

# start server and run cronjob
CMD ["/app/start-server.sh"]