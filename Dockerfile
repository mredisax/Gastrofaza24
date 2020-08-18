# pull official base image
FROM python:3.8.3-alpine

# create directory for the app user
RUN mkdir -p /home/gastrofaza24 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S gastrofaza24 && adduser -S gastrofaza24 -G gastrofaza24

# create the appropriate directories
ENV HOME=/home/gastrofaza24 
ENV APP_HOME=/home/gastrofaza24/web 
RUN mkdir $APP_HOME 
RUN mkdir $APP_HOME/staticfiles 
RUN mkdir $APP_HOME/mediafiles 
WORKDIR $APP_HOME
# install dependencies
RUN apk update && apk add libpq postgresql-dev \
	&& apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev 
COPY ./requirements.txt . 

RUN pip install -r requirements.txt 
RUN apk add libjpeg

# copy entrypoint-prod.sh
COPY ./entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R gastrofaza24:gastrofaza24 $APP_HOME

# change to the app user
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "gastrofaza.wsgi:application"]

# run entrypoint.prod.sh
ENTRYPOINT ["/home/gastrofaza24/web/entrypoint.prod.sh"]
 
