import pytest
from src.patterns.creational.singleton.database_config import DatabaseConfig

@pytest.fixture
def reset_singleton(request):
    """
    Fixture to reset the Singleton state before and after each test.
    This uses addfinalizer instead of yield, as requested.
    """
    # Pre-test reset
    DatabaseConfig._instance = None
    DatabaseConfig._connection = None

    def finalize():
        # Post-test reset
        print("Finalizing...")
        DatabaseConfig._instance = None
        DatabaseConfig._connection = None

    request.addfinalizer(finalize)

def test_singleton_database_config_identity(reset_singleton):
    """
    Ensure that multiple attempts to create DatabaseConfig result
    in the same instance (Singleton property).
    """
    config1 = DatabaseConfig(db_path=":memory:")
    config2 = DatabaseConfig(db_path=":memory:")
    assert config1 is config2, "Multiple instances of the database config were created"

def test_database_config_initialization(reset_singleton):
    """
    Ensure that the config is initialized properly once,
    and ignores subsequent initializations.
    """
    config = DatabaseConfig(db_path=":memory:")
    assert config.db_path == ":memory:", "Database path was not set correctly"

    # Attempt re-initialization
    config_new = DatabaseConfig(db_path="ignored_db.sqlite")
    # The property should remain the same if the config was already set
    assert config_new.db_path == ":memory:", "Singleton config should not be reinitialized"

def test_database_connection(reset_singleton):
    """
    Test that connect() returns a live, shared DB connection.
    """
    config = DatabaseConfig(db_path=":memory:")
    connection = config.connect()
    assert connection is not None, "Database connection is None"

    # Try a quick SQL statement
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY);")
        cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table'")
        tables = cursor.fetchall()
        assert len(tables) == 1, "Failed to create 'test_table' in the in-memory database"

def test_clearing_connection(reset_singleton):
    """
    Test that closing a connection via close_connection() is reflected globally.
    """
    config = DatabaseConfig(db_path=":memory:")
    connection_before = config.connect()

    config.close_connection()
    connection_after = config._connection  # Access the internal var for testing

    assert connection_before is not None, "Expected open connection before closure"
    assert connection_after is None, "Expected connection to be cleared after closure"

def test_create_table_and_insert(reset_singleton):
    """
    Demonstrates using DatabaseConfig Singleton to create a table and insert records
    in an in-memory database.
    """
    config = DatabaseConfig(db_path=":memory:")
    conn = config.connect()

    # Create a 'products' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
    """

    with conn:
        conn.execute(create_table_query)
        # Insert sample record
        insert_query = "INSERT INTO products (name, price) VALUES (?, ?)"
        conn.execute(insert_query, ("Sample Product", 10.99))

    # Read back what we inserted
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()

    assert len(rows) == 1, "Expected one product in the table"
    product = rows[0]
    assert product[1] == "Sample Product", "Product name mismatch"
    assert product[2] == 10.99, "Product price mismatch"

    # Close the connection
    config.close_connection()
