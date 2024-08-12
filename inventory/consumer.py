import time

from main import Product, redis
from redis.exceptions import ConnectionError, ResponseError

key = "order_completed"
group = "inventory-group"

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

        if results:
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj["product_id"])
                    product.quantity = product.quantity - int(obj["quantity"])
                    product.save()
                except Exception as e:
                    print(f"Error processing product: {e}")
                    redis.xadd("refund_order", mapping=obj, id="*")

    except (ResponseError, ConnectionError) as e:
        print(f"Redis error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    time.sleep(1)
