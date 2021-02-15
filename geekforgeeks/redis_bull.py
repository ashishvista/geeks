import json
import math
import time
from datetime import datetime, timedelta

import redis
from rediscluster import RedisCluster

def deleteOnBasisOfdays(rc, pattern, key_to_search_in_object, date_N_days_ago):
    count = 0
    for key in rc.scan_iter(pattern):
        time.sleep(1)
        count += 1
        try:
            data = rc.hgetall(key)
        except Exception as e:
            print("An exception occurred", e, key)
            continue

        if key_to_search_in_object in data:
            processedOn = int(data[key_to_search_in_object])
            dt_object_processed_on = datetime.utcfromtimestamp(processedOn // 1000)
            if dt_object_processed_on < date_N_days_ago:
                print("keys deleted*****", key, processedOn, count)
                # rc.delete(key)
            else:
                print("Not deleting key****************", key)
        else:
            print('outside else*********************', data)

    print("Done***************")


def deleteOnIdleTime(rc):
    IDLE_TIME = 7 * 24 * 60 * 60
    count = 0
    for key in rc.scan_iter("*"):
        count += 1
        idle = rc.object("idletime", key)
        # print(key, idle, count)
        if idle > IDLE_TIME:
            time.sleep(.05)
            print(key, idle)
            # rc.delete(key)


def findMemoryUsage(rc):
    count = 0
    kilo = 0
    h = {}
    for key in rc.scan_iter("*"):
        print("key******************", key)
        time.sleep(.005)
        mu = rc.execute_command("MEMORY USAGE", key)
        mu = int(mu) * 0.000001
        count += 1
        kilo += 1
        if kilo == 1000:
            print(count)
            kilo = 0
        tmp = key[:9]
        if tmp in h:
            h[tmp]["count"] += 1
            h[tmp]["mu"] += mu
            h[tmp]["max_mu"] = max(h[tmp]["max_mu"], mu)
        else:
            h[tmp] = {"count": 1, "mu": mu, "max_mu": mu}

    for k in h:
        h[tmp]["mu"] = math.floor(h[tmp]["mu"])
        h[tmp]["max_mu"] = math.floor(h[tmp]["max_mu"])

    sorted_x = sorted(h.items(), key=lambda kv: kv[1]['mu'], reverse=True)
    with open('/home/ashish/PycharmProjects/geeks/downloads/redis5.json', 'w') as fp:
        json.dump(sorted_x, fp)
    print(sorted_x)


def deleteOnTTL(rc):
    count = 0
    expiry_in_days = 60 * 60 * 24 * 3
    for key in rc.scan_iter("*"):
        time.sleep(.01)
        count += 1
        ttl = rc.ttl(key)
        if ttl == -1:
            print("no ttl*********", key,count)
            a = 1
            rc.expire(key, expiry_in_days)
        elif ttl > expiry_in_days:
            print("ttl more than 3 days###########", key, ttl,count)
            rc.expire(key, expiry_in_days)
            a = 1
        else:
            print("ttl less than 3 days", key, ttl,count)
            a = 1


if __name__ == "__main__":
    startup_nodes = [{"host": "redis-service-0.redis-service.prod.svc.cluster.local", "port": "6379"},
                     {"host": "redis-service-1.redis-service.prod.svc.cluster.local", "port": "6379"},
                     {"host": "redis-service-2.redis-service.prod.svc.cluster.local", "port": "6379"},
                     {"host": "redis-service-3.redis-service.prod.svc.cluster.local", "port": "6379"},
                     {"host": "redis-service-4.redis-service.prod.svc.cluster.local", "port": "6379"},
                     {"host": "redis-service-5.redis-service.prod.svc.cluster.local", "port": "6379"}]

    # startup_nodes = [{"host": "localhost", "port": "7000"}]

    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    # rc = redis.StrictRedis(host='localhost', port=7000, db=0, decode_responses=True)

    N = 5
    date_N_days_ago = datetime.now() - timedelta(days=N)

    # key_to_search_in_object = "created_at"
    # pattern = "{t-image}*"

    pattern = "{notification}*"
    key_to_search_in_object = "timestamp"
    # deleteOnBasisOfdays(rc, pattern, key_to_search_in_object, date_N_days_ago)
    # findMemoryUsage(rc)
    deleteOnTTL(rc)
