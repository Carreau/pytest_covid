# Pytest covid. 


> When you do testing to that extent, you're going to find more people, you're
> going to find more cases. So I said to my people, slow the testing down —
> please.

The more failures you'll get the more tests it will skip.

```
# pytest.ini
[pytest]
[covid]
enabled = True
fake_news = False
```

Or if you like Fox News set `fake_news = True` and test failures will be reported as success.

# test failure contamination

For each test failure, 5% of the remaining tests will randomly fail, and 5% of
the remaining tests will be skipped. Effect compounds even with `fake_news=True`
except Failing test _appear_ to be passing.
