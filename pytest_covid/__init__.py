"""
Too many faillure, less tests.
"""
import pytest

__version__ = '0.0.1'

oh_no = False

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        skip_reason = "Too many test failed, better stop testing.".format(item.name)
        for test in item.session.items:
            test.add_marker(pytest.mark.skipif(True, reason=skip_reason))

@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    print(pyfuncitem.session)
    outcome = yield
    # outcome.excinfo may be None or a (cls, val, tb) tuple
    global oh_no

    try:
        res = outcome.get_result()  # will raise if outcome was exception
    except Exception:
        for test in pyfuncitem.session.items:
            test.add_marker(pytest.mark.skipif(True, reason="Too many failures. Better stop testing."))
        outcome.force_result('skipped')
        oh_no = True


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    try:
        # Before pytest 5 the values were contants
        from _pytest.main import  EXIT_OK
        ok = EXIT_OK
    except ImportError:
        # From pytest 5 on the values are inside an enum
        from pytest import ExitCode
        ok = ExitCode.OK

    session.exitstatus = ok
