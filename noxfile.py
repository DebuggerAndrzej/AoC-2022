import nox
import os

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = [
    "tests",
    "check_black",
    "check_isort",
]

BLACK_VERSION = "black==22.10.0"
ISORT_VERSION = "isort==5.10.1"
PYTEST_VERSION = "pytest==7.2.0"
CONFIG_PATH = "configuration/pyproject.toml"


@nox.session
def tests(session):
    """Run the test suite."""
    session.install(PYTEST_VERSION)
    with session.chdir("python"):
        session.run("python", "-m", "pytest", "-v", "-c", os.path.join("..", CONFIG_PATH))



@nox.session
def check_black(session):
    """Check code compatibility with black"""
    session.install(BLACK_VERSION)
    session.run("black", "--config", CONFIG_PATH, "--check", "--diff", "python")


@nox.session
def check_isort(session):
    """Check if imports are sorted correctly"""
    session.install(ISORT_VERSION)
    session.run("isort", "--sp", CONFIG_PATH, "--check-only", "--diff", "python")


@nox.session
def format_code(session):
    """Format code according to rules used in project"""
    session.install(BLACK_VERSION, ISORT_VERSION)
    session.run("black", "--config", CONFIG_PATH, "python")
    session.run("isort", "--sp", CONFIG_PATH, "python")