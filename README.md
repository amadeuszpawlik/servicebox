# servicebox
## requirements

python3 (sudo apt install python3.7; set as default: sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1)

python3-pip (sudo apt install python3-pip)

pipenv (sudo -H pip3 install -U pipenv)

cd <whateva>/servicebox
pipenv install

## run server locally
### run pipenv shell
cd <whateva>/servicebox
pipenv shell
  
### start server
cd servicebox (placing you at <whateva>/servicebox/servicebox)
python manage.py runserver 127.0.0.1:8000

## addresses and users
login> admin@admin.com
pw>    admin

login> user@user.com
pw>    userpassword

login> johnny@bazooka.com
pw>    userpassword

base url: 127.0.0.1:8000/
adminpage: <base url>/admin
