import toml


class RedisCache:
    def get_redis_settings(self):
        with open('redis.toml', 'r') as r:
            redis_settings = toml.load(r)['redis']
        return redis_settings    