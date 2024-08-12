import time

from main import Order, redis
from redis.exceptions import ConnectionError, ResponseError

key = "refund_order"
group = "payment-group"

try:
    redis.xgroup_create(key, group)
except ResponseError as e:
    if "BUSYGROUP Consumer Group name already exists" not in str(e):
        print(f"Error creating group: {e}")
except ConnectionError as e:
    print(f"Redis connection error: {e}")

while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)

        if results != []:
            print(results)
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj["pk"])
                order.status = "refunded"
                order.save()

    except Exception as e:
        print(str(e))
    time.sleep(1)
