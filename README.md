# BigData
## Dependencies 
* [Python 3.7](https://www.python.org/download/releases/3.7/)

```
$ pip install -r requirement.txt
```
## Start cluster
```
$ cd docker
$ docker-compose up -d
```
## Start crawl then store in hdfs cluster
```
$ cd Python
$ python main.py --amount=100 --namenode=192.168.1.1 --path=bigdata/data.json
```

