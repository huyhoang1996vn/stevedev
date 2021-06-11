
# Django3 Project

### Create Virtual 
python3.7
```sh
# https://dev.to/serhatteker/how-to-upgrade-to-python-3-7-on-ubuntu-18-04-18-10-5hab
virtualenv -p python3.7 django3_env
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
```


