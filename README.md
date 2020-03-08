# Gastrofaza

My first django app with information about local restaurants in my family city



### Tech

Dillinger uses a number of open source projects to work properly:

* Django - Django
* crispy_forms
* captcha(optional)
* social_django(optional)

### Installation

How to run this project on local machine

```sh
$ sudo -H pip3 install virtualenv
$ git clone https://github.com/mredisax/Gastrofaza24.git
$ cd Gastrofaza24
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

If you want set up this project on the server I recommend you guide from [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)



### Todos

 - Write Tests
 - Scraping function to get restaurant news from facebook fanpage (from wall)

License
----

MIT


**Free Software, Hell Yeah!**
