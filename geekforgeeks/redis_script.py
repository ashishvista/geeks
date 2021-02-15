#  pip install redis
import time
import redis

print("starting script")
# r = redis.StrictRedis(host='redis-service', port=6379, db=0)
r = redis.StrictRedis(host='localhost', port=7000, db=0)

IDLE_TIME = 7 * 24 * 60 * 60
for key in r.scan_iter("*"):
    idle = r.object("idletime", key)
    print(key, idle)


# # pip install redis-py-cluster
# from rediscluster import RedisCluster
# import time
#
# startup_nodes = [{"host": "redis-service-4.redis-service.prod.svc.cluster.local", "port": "6379"}]
#
# rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#
# IDLE_TIME = 7 * 24 * 60 * 60
# count=0
# for key in rc.scan_iter("*notification*"):
#     count+=1
#     idle = rc.object("idletime", key)
#     print(key, idle,count)
#     # if idle > IDLE_TIME:
#     #     time.sleep(.05)
#     #     print(key, idle)
#     #     rc.delete(key)
#


