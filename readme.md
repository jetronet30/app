
py -m venv  venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

venv\Scripts\activate

python.exe -m pip install --upgrade pip

pip install django

pip install Pillow  

pip install ipython

pip install django-debug-toolbar

django-admin startproject project_name — ახალი პროექტის შექმნა
django-admin startapp app_name — ახალი app-ის შექმნა

py manage.py makemigrations

py manage.py migrate
py manage.py runserver

py manage.py createsuperuser

pip install django-debug-toolbar

py manage.py shell

py manage.py dumpdata goods.Categories > fixtures/goods/cats.json

$env:PYTHONIOENCODING="utf-8"

$env:PYTHONUTF8="1"

py manage.py dumpdata goods.Products --indent 2 --output fixtures/goods/prod.json

py manage.py loaddata fixtures/goods/cats.json

