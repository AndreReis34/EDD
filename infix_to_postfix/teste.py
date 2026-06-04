import redis

r = redis.Redis(
    host='redis-10060.c241.us-east-1-4.ec2.cloud.redislabs.com',
    port=10060,
    decode_responses=True,
    username="default",
    password="5WuOM3fKsibGskDvSb0ZcapF416orTra",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

