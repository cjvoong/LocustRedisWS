# LocustRedisWS

* Locust script reads data from a redis set.
* Calls spop so other readers cannot access the same data
* Data is batch loaded on start of a Locust
