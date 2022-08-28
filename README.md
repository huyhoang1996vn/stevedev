
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

### Api document by redocly

Open api-doc.html

### Postmain json

Open app.postman_collection.json

### Postgres export data 

Open data.sql

### Run project

```sh
python manage.py runserver 0:8000
```

### Please ignore Docker, docker compose, zappa 
