''' 
The conftest.py file serves as a means of providing fixtures for an entire directory
Fixtures defined in a conftest.py can be used by any test in that package without needing to import them (pytest will automatically discover them)
'''
import pytest
from src.utility import Utility

@pytest.fixture
def utility(scope="session"):
    return Utility()

# scope="session" only fired once for every single unit test session and reuses the value previously