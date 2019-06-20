import invokust

settings = invokust.create_settings(
    locustfile='websocket_locust.py',
    host='http://example.com',
    num_clients=2,
    hatch_rate=1,
    run_time='2s'
    )

loadtest = invokust.LocustLoadTest(settings)
loadtest.run()
print(loadtest.stats())
