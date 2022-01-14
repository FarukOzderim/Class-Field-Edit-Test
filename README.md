# Class-Field-Edit-Test

Example demo in which Event class field is different in different scope.


## Flow
```
➜  Class-Field-Edit-Test git:(master) ✗ python3 -m src.__init__

Events.PORT at __init__.py: 8000
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [50563] using statreload
INFO:     Started server process [50565]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
Events.PORT at listener.py: None
INFO:     127.0.0.1:59738 - "GET / HTTP/1.1" 200 OK
^CINFO:     Shutting down
```
