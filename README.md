# App Skeleton
This project is a skeleton to quickly create Flask applications. It implments a number of functionalities, including user registration and profiles, error handling, as has a menu to get you started.

The code was adapted from the outstandingly good Flask Mega-Tutorial by Michael Grinberg, available [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Features implemented:
- Base for error handling
- User registration
- Menu
- User Profile

TODO:
- Password recovery

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
