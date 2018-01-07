Liberation Philly
=================
[![Maintainability](https://api.codeclimate.com/v1/badges/222dd743841a45af937f/maintainability)](https://codeclimate.com/github/liberationphilly/django_site/maintainability)


A WIP website for Liberation Philly in Django. Contains events, email subscription field, and might cover more in the future.


To run locally:

```
pip3 install -r requirements.txt
```

```
python3 manage.py migrate
```

```
python3 manage.py runserver
```

Note: some static images in the /photos folder have been gitignored. 


To login to the admin site:

```
$ python manage.py createsuperuser
```


```
Username: admin
```


```
Email address: admin@example.com
```


```
Password: **********
Password (again): *********
Superuser created successfully.
```

http://127.0.0.1:8000/admin/
