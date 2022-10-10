# ELASTICSEARCH - clean log messages by days

python script run for clean log message and fitler data by days and later than amount of days

## Prerequired
- docker engine

## Syntax

```
Usage: main.py <url_domain> <index> <days>
```


### Build image

ex. build docker images

```
docker build -f Dockerfile -t es_clean .
```

### How to run

ex. run docker via docker image

```
docker run --rm es_clean http://localhost:9200 graylog_0 4
```

enjoy ^_^