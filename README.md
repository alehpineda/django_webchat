# django_webchat
 A demo webchat created using django, django channels, react, docker, redis, and node.


This demo is for how to build a chat application with Django Channels.

Needs a redis backend, I suggest using docker.

To run the backend, run:

```bash
docker container run -d -p 6379 redis:2.8
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

To run the frontend:

```bash
npm i
npm start
```

Open

localhost:1234 to see the demo

To develop locally:

```
1. Change the `DEBUG` flag in `src/settings.js`
2. Create two users (easiest way might be to run `python manage.py createsuperuser` twice)
3. Using django admin, create a `Contact` object for each user.
4. Make sure you have an instance of redis running.
```

To build for deployment:

```bash
npm run build
```

Please note this is a **demo project** of the concepts used in building a chat app. It is simply not production ready.