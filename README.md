Memcached GUI
=============

A simple GUI for `memcached`

Uses:
* Python 2.7
* Flask 0.12
* Green Unicorn

The `docker-compose.yml` also brings up a memcached service, exposed to the host on `localhost:11211`


# Usage
## Bring up the stack
```
docker-compose up -d // :)
```

## URL
```
http://localhost:8000
```

## Memcached
```
telnet localhost 11211

get <key>

set <key> <flags (0)> <expiry (s)> <length (chars)>
<value>

e.g:
set foo 0 100 3
bar
STORED

get foo
VALUE foo 0 3
bar
END

quit
```


