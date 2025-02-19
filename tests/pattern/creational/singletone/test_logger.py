import pytest

from src.patterns.creational.singleton.logger import Logger

def test_singleton_logger_instance():
    # Create two instances of Logger
    logger1 = Logger()
    logger2 = Logger()

    # Assert that both instances are the same
    assert logger1 is logger2, "Singleton failed: multiple logger instances created"

def test_logger_add_log():
    # Create an instance and add a log message
    logger1 = Logger()
    logger1.add_log("User logged in", level="INFO")

    # Create another instance and check if the log is shared
    logger2 = Logger()
    logs = logger2.get_logs()
    assert any("User logged in" in log for log in logs), "Singleton failed: logs not shared"

def test_logger_clear_logs():
    # Clear logs from one instance and ensure they are cleared globally
    logger1 = Logger()
    logger1.add_log("Processing payment", level="INFO")
    logger1.clear_logs()

    logger2 = Logger()
    assert logger2.get_logs() == [], "Logs were not cleared globally"
