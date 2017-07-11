#! /bin/bash

set -e

curr_dir=$(pwd)
app_name=$1
f_name=$2
l_name=$3
email=$4
username=$5
password=$6

function display_help() {
    echo "./setup.sh APPNAME FIRSTNAME LASTNAME EMAIL DBUSERNAME DBPASSWORD"
}

if [[ $1 == '--help' ]]
then
    display_help
    exit 0
fi
if [[ $1 ==  "" ]]
then
     app_name="appname"
fi
if [[ $2 ==  "" ]]
then
     f_name="firstname"
fi
if [[ $3 ==  "" ]]
then
     l_name="lastname"
fi
if [[ $4 ==  "" ]]
then
     email="example@sample.com"
fi
if [[ $5 ==  "" ]]
then
     username="potter"
fi
if [[ $6 ==  "" ]]
then
    password="voldemort"
fi

echo "Replacing boilerplate names with your app name..."
# setup.py
sed -i "" "s/boilerplate/${app_name}/g" "$curr_dir/setup.py"
sed -i "" "s/Flask-Boilerplate/${app_name}/g" "$curr_dir/setup.py"
# Docker files
sed -i "" "s/flaskboilerplate/${app_name}/g" "$curr_dir/docker-compose.yml"
sed -i "" "s/FirstName/${f_name}/g" "$curr_dir/Dockerfile"
sed -i "" "s/LastName/${l_name}/g" "$curr_dir/Dockerfile"
sed -i "" "s/email@example.com/${email}/g" "$curr_dir/Dockerfile"
# Rename .env-example to env
if [ -f $curr_dir/.env-example ]
then mv .env-example .env
fi
# Replace values in .env
sed -i "" "s/flaskboilerplate/${app_name}/g" "$curr_dir/.env"
sed -i "" "s/potter/${username}/g" "$curr_dir/.env"
sed -i "" "s/voldemort/${password}/g" "$curr_dir/.env"

echo "Making instance/ directory for storing secure values..."
# Make instance directory
mkdir -p instance/
touch instance/__init__.py
touch instance/settings.py
config="SQLALCHEMY_DATABASE_URI = 'postgresql://$username:$password@postgres:5432/$app_name'\n\n\
# Mail\n\
MAIL_SERVER = 'smtp.googlemail.com'\
MAIL_PORT = 587\n\
MAIL_USE_TLS = True\n\
MAIL_USERNAME = '$email'\n\
MAIL_PASSWORD = 'supersecret'\n\
CC_MAIL_SUBJECT_PREFIX = '[$app_name]'\n\
CC_MAIL_SENDER = '$app_name <$email>'\n"
echo -e $config > instance/settings.py

echo "Installing packaging and removing git remote repository..."
# Packaging and Git stuff
pip install --editable .
git remote rm origin
echo "Done!"
