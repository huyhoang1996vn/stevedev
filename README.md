
# Django3 Project

### Create Virtual 
python3.7
```sh
# https://dev.to/serhatteker/how-to-upgrade-to-python-3-7-on-ubuntu-18-04-18-10-5hab
# https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/
virtualenv -p python3 venv
source venv/bin/activate
```

python3.6
```sh
virtualenv -p python3.6 django3_env
source django3_env/bin/activate
```


### Install requirements
```sh
sudo apt install python3-pip
pip3 install -r requirements.txt 
```

### 
```sh
python manage.py createsuperuser --settings=config.local
# dev/!@#$%^&*
python manage.py runserver 0:8000 --settings=config.local
python manage.py migrate --settings=config.local

uvicorn helio.asgi:application --host 0.0.0.0 --port 8001
python manage.py collectstatic --settings=config.local
python manage.py createsuperuser --settings=config.local
```
sudo systemctl restart django3
systemctl status django3.service
cat /etc/systemd/system/django3.service

sudo cat /dev/null > /var/log/syslog
0 0 * * *  find  /var/log/syslog.1  -delete
0 0 * * *  find  /var/log/*.gz -delete


### Systemd
```sh

[Unit]
Description=django3 uvicorn daemon
After=network.target

[Service]
User=root
WorkingDirectory=/home/django3
Environment="DJANGO_SETTINGS_MODULE=config.production"
ExecStart=/home/django3_env/bin/uvicorn helio.asgi:application --host 0.0.0.0 --port 8001 --log-config log.ini

[Install]
WantedBy=multi-user.target
```
### Docker
```sh
docker run -d --name postgres  -p 5432:5432  -e "POSTGRES_USER=postgres"  -e "POSTGRES_PASSWORD=postgres"  postgres:10.17

docker-compose -f docker-compose.yml up -d

sudo docker-compose -f docker-compose.yml up -d --build --force-recreate web

docker exec -it django3_web_1 bash

docker exec django3_web_1 bash -c "python manage.py collectstatic --noinput"

```

### Docker hub
```sh
sudo docker build -t django3:0.0.2 .
sudo docker run -d -p 8011:8011 --name=django3 django3:0.0.2
sudo docker build -t django3:0.0.2 .

sudo docker build -t huyhoang1996ha/django3:0.0.2 .
sudo docker push huyhoang1996ha/django3:0.0.2
sudo docker run -d -p 8011:8011 --name=django3 huyhoang1996ha/django3:0.0.5
```



### Nginx config
```sh

<VirtualHost *:80>
    ServerName stevedev.cf
    ServerAlias resume.stevedev.cf
    ProxyRequests On
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8001/
    ProxyPassReverse / http://127.0.0.1:8001/
</VirtualHost>
```

### Certbot config

https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04


```sh

sudo certbot --apache -d stevedev.cf -d www.stevedev.cf

ProxyPreserveHost On

docker run -d -p 9000:9000 -p 9001:9001 \ --name minio-server \ -d \ -v /minio-server/data:/data \ -e "MINIO_ROOT_USER=huyhoang1996ha" \ -e "MINIO_ROOT_PASSWORD=huyhoang@123" \ quay.io/minio/minio server /data --console-address ":9001"
```



https://www.w3schools.com/howto/howto_css_cards.asp



## Django in serverless (Zappa)
### library
```sh
pip install zappa
pip install django-s3-storage
```

### Commands zappa
```sh
zappa init
zappa deploy (stage)
zappa update dev
zappa tail
zappa manage dev "collectstatic --noinput"

```

### Tutorial zappa
https://www.section.io/engineering-education/deploying-a-serverless-django-restapi-with-zappa-on-aws/
https://auth0.com/blog/deploying-django-restful-apis-as-serverless-applications-with-zappa/#Deploying-with-Zappa

### Custom domain zappa
https://romandc.com/zappa-django-guide/walk_domain/
