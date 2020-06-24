"""
Too many faillure, less tests.
"""
import pytest
import random

__version__ = '0.0.1'

oh_no = False


class Covid:

    def __init__(self, config):
        self.config = config

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()
        if report.failed:
            skip_reason = "Too many test failed, better stop testing.".format(item.name)
            for test in item.session.items:
                test.add_marker(pytest.mark.contaminated)
                #test.add_marker(pytest.mark.skipif(True, reason=skip_reason))

    @pytest.hookimpl(hookwrapper=True)
    def pytest_pyfunc_call(self, pyfuncitem):

        outcome = yield
        # outcome.excinfo may be None or a (cls, val, tb) tuple

        try:
            res = outcome.get_result()  # will raise if outcome was exception
        except Exception:
            failing = True
        if pyfuncitem.iter_markers('contaminated'):
            failing = True

            for test in pyfuncitem.session.items:
                r = random.random()
                if r < 0.05:
                    test.add_marker(pytest.mark.contaminated)
                elif r  < 0.1:
                    test.add_marker(pytest.mark.skipif(True, reason='to affraid to test'))
            outcome.force_result('skipped')


    @pytest.hookimpl(trylast=True)
    def pytest_sessionfinish(self, session, exitstatus):
        try:
            # Before pytest 5 the values were contants
            from _pytest.main import  EXIT_OK
            ok = EXIT_OK
        except ImportError:
            # From pytest 5 on the values are inside an enum
            from pytest import ExitCode
            ok = ExitCode.OK

        session.exitstatus = ok
        
def pytest_configure(config):
    c = config.inicfg.config.sections.get('covid', {})
    print(config.inicfg.config.sections.get('covid', {}))
    
    if c['enabled']:
        config.pluginmanager.register(Covid(config))

