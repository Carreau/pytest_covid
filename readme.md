# Pytest covid. 


> When you do testing to that extent, you're going to find more people, you're
> going to find more cases. So I said to my people, slow the testing down —
> please.

The more failures you get, the more tests it will skip.

```
# pytest.ini
[pytest]
[covid]
enabled = True
fake_news = False
```

Or if you like Fox News set `fake_news = True` and test failures will be reported as success.

# test failure contamination

For each test failure, 4% of the remaining tests will randomly fail (they get
contaminated), and 1% will be skipped. The effect compounds, so a contaminated test,
will contaminate more tests and skip even more. Even with `fake_news=True`, except
a failing test will _appear_ to be passing.


# Example:

Running 500 test with a 1% change of failing:

```
tests/test_covid.py ...........F.........s...............F.....s..sF...s....FsF..F.sFFs....sFs...s..F [ 16%]
FFsFFFssFsFss.s..sFFsFssssFFssssFs.sFssssss.sFss.sssss.sss.sss.sFsFssssssssFsssFssssss.sssssFssFsssss [ 36%]
ssssssssssssssssssssssssssss.sss.sssss.ss.ssssssFsFssssssFsssssssFsssssssssssssFFsssFssssssssFsFsFsFs [ 56%]
sssssFsssFssssFssssssssssssFssssssssssssFFsssssssssssssssFsssssssssssFssssssssssssssssssssssss.ssssss [ 76%]
ssssssFssssssssssssssssssssssFssssssFsssssssssssFssssssssssssssssFsssssssssssssssssssFssssssssssssFs. [ 97%]
sssssssssssssss
```


Same while watching Fox News, or if you believe you'll safe in church:


```
tests/test_covid.py .....................s....ss..........sssssss.s..s......ss.....s...sss.sss...ss.s [ 16%]
s.s.s..s.ss.s...s..s.s.ss.ss..ssss.s..sssssssssss.ss..sss.sss..s.s.sssssss.s.ss.ss.ssssss.ssss...s..s [ 36%]
ss.ss.ssss.ss...s.sssssss.sssssssssssssssssssssssss.ssss.ssssssssssssssssssssss.ssssssssssssssss.ssss [ 56%]
sssssssssssssssss.ssssssssssssssss.sssssssss.ssssssssssssssssssssssss.s.sssssssssssssssssssssssssss.s [ 76%]
sssssss.ssssssssssssssss.sssss.sssss.sssssssssssssssssssssssssssssssssssssssssss.sssssss.ssssss.sssss [ 97%]
ssssssssssssss
```
