# es

Setup for database

cd C:\Users\Ana\.aws # your path to the credentials
notepad credentials #update with aws credentials in website 
cd C:\Users\Ana\Desktop\ES\project_2\ebdjango # your path to the project
%HOMEPATH%\eb-virt\Scripts\activate

python manage.py startapp project #star app with name project

For installing access to the database

python manage.py createsuperuser #create your admin user for django console

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#if it does not work do
python manage.py makemigrations project


For the react part

#On project directory
npx create-react-app frontend
cd frontend
npm start

npm run build

 
