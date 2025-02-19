from datetime import datetime

class Logger:
    _instance = None  # Class variable to hold the single instance
    _logs = []        # List to store log messages

    def __new__(cls):
        if cls._instance is None:
            # If no instance exists, create one
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def add_log(self, message: str, level: str = "INFO"):
        """Add a log message with a timestamp and log level."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self._logs.append(log_entry)

    def get_logs(self) -> list:
        """Get all log messages."""
        return self._logs

    def clear_logs(self):
        """Clear all log messages."""
        self._logs.clear()