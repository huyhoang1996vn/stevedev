
# Django3 Project

### Create Virtual 
python3.7
```sh
# https://dev.to/serhatteker/how-to-upgrade-to-python-3-7-on-ubuntu-18-04-18-10-5hab
# https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/
virtualenv -p python3.8 django3_env
source django3_env/bin/activate
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

docker run -d --name postgres  -p 5432:5432  -e "POSTGRES_USER=postgres"  -e "POSTGRES_PASSWORD=postgres"  postgres:10.17



docker-compose -f docker-compose.yml up -d

sudo docker-compose -f docker-compose.yml up -d --build --force-recreate web

docker exec -it django3_web_1 bash

docker exec django3_web_1 bash -c "python manage.py collectstatic --noinput"



<VirtualHost *:80>
    ServerName stevedev.cf
    ServerAlias resume.stevedev.cf
    ProxyRequests On
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8001/
    ProxyPassReverse / http://127.0.0.1:8001/
</VirtualHost>

sudo certbot --apache -d stevedev.cf -d www.stevedev.cf
https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04

ProxyPreserveHost On

sudo sysctl -p

docker run -d -p 9000:9000 -p 9001:9001 \ --name minio-server \ -d \ -v /minio-server/data:/data \ -e "MINIO_ROOT_USER=huyhoang1996ha" \ -e "MINIO_ROOT_PASSWORD=huyhoang@123" \ quay.io/minio/minio server /data --console-address ":9001"

