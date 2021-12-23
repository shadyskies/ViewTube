# run django server from docker container


FROM python:3.9

RUN apt-get update && apt-get -y install cron vim

COPY cron-job /etc/cron.d/cron-job
RUN chmod 0644 /etc/cron.d/cron-job


# copy source and install dependencies
RUN mkdir -p /app
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
RUN touch /var/log/cron.log

# run the cron job
RUN crontab /etc/cron.d/cron-job

RUN chmod +x /app/start_server.sh
RUN chmod +x /app/run_cron.sh

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
 
# Run the command on container startup
RUN (crontab -l ; echo "* * * * * ./run_cron >> /var/log/cron.log") | crontab

CMD cron && tail -f /var/log/cron.log