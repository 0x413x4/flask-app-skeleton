# App Skeleton

Skeleton for Flask application.

Features implemented:
- Base for error handling
- User registration
- Menu
- User Profile

TODO:
- Password recovery
- Move users to email based auth

## How to start

1. Clone the repository locally and delete the `.git` directory

```bash
$ git clone https://github.com/0x413x4/flask-app-skeleton.git
$ cd flask-app-skeleton && rm -rf .git
```

2. Replace `app-skeleton` by the name of your app

```bash
$ grep -rliI app-skeleton * .* | xargs sed -i 's/app-skeleton/my-new-app/g'
```

Don't forget to change the name of the app file `app-skeleton.py`

3. Start the test server

```bash
$ vagrant up
```

4. Connect to the test server, and initialise the database

```bash
$ vagrant ssh

vagrant $ cd /my-new-app
vagrant $ flask db init
vagrant $ flask db migrate
vagrant $ flask db upgrade
```

5. Start the application

```bash
vagrant $ flask run --host 0.0.0.0
```

Once the application started, you should be able to login at: 
[](http:/127.0.0.1:5000)
