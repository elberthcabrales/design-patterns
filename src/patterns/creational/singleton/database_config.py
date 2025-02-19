import sqlite3

class DatabaseConfig:
    """
    Singleton class for database configuration and connection management.
    Ensures only one instance for the entire application.
    """
    _instance = None
    _connection = None

    def __new__(cls, db_path=None):
        # If we haven't instantiated yet, create an instance
        if cls._instance is None:
            cls._instance = super(DatabaseConfig, cls).__new__(cls)
            # You can set any defaults you want here; just placeholders:
            cls._instance.db_path = db_path
        return cls._instance

    def connect(self):
        """
        Creates a new DB connection if one doesn't exist yet, or returns the existing one.
        """
        if not self._connection:
            if not self.db_path:
                raise ValueError("Database path is not configured.")
            # Example using SQLite, but you can adapt to any DB engine
            self._connection = sqlite3.connect(self.db_path)
        return self._connection

    def close_connection(self):
        """
        Closes the DB connection if it's open.
        """
        if self._connection:
            self._connection.close()
            self._connection = None
