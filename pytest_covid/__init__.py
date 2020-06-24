"""
Too many faillure, less tests.
"""
import sys
import pytest
import random

__version__ = "0.0.2"

oh_no = False


class Covid:
    def __init__(self, config):
        self.config = config

    @pytest.hookimpl(hookwrapper=True)
    def pytest_pyfunc_call(self, pyfuncitem):

        marks = list(pyfuncitem.iter_markers())
        print("MARKS:", marks)

        outcome = yield

        failing = False
        try:
            res = outcome.get_result()  # will raise if outcome was exception
        except Exception:
            failing = True

        if marks:
            try:
                raise ValueError("Testing positive to Covid 19")
            except ValueError:
                excinfo = sys.exc_info()
                outcome._execinfo = excinfo
            failing = True

        if failing:
            for test in pyfuncitem.session.items:
                r = random.random()
                if r < 0.005:
                    test.add_marker(pytest.mark.contaminated)
                elif r < 0.01:
                    test.add_marker(
                        pytest.mark.skipif(True, reason="to affraid to test")
                    )
        if self.config.get("fake_news") == "True":
            outcome.force_result(None)

    @pytest.hookimpl(trylast=True)
    def pytest_sessionfinish(self, session, exitstatus):
        try:
            # Before pytest 5 the values were contants
            from _pytest.main import EXIT_OK

            ok = EXIT_OK
        except ImportError:
            # From pytest 5 on the values are inside an enum
            from pytest import ExitCode

            ok = ExitCode.OK

        session.exitstatus = ok


def pytest_configure(config):
    try:
        c = config.inicfg.config.sections.get("covid", {})
    except Exception:
        pass

    if c["enabled"] == "True":
        config.pluginmanager.register(Covid(c))
