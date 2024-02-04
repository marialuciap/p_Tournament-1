
import json

def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    tests_failed = session.testsfailed
    tests_collected = session.testscollected
    output = {
        "tests_failed": tests_failed,
        "tests_collected": tests_collected,
        
    }
    print("\n",output )

