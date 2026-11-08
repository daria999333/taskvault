import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
import pytest
from taskvault import database
from taskvault import database


@pytest.fixture(autouse=True)
def setup_test_db(monkeypatch, tmp_path):
    """Isolate tests by redirecting database to a temporary file."""
    test_db = tmp_path / "test_tasks.db"
    monkeypatch.setattr(database, "DB_NAME", str(test_db))
    database.init_db()


def test_add_and_get_tasks():
    """Test adding a task and retrieving it from the database."""
    task_id = database.add_task("Write software architecture report", "High")
    assert task_id == 1

    tasks = database.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Write software architecture report"
    assert tasks[0]["priority"] == "High"
    assert tasks[0]["status"] == "Pending"


def test_complete_task():
    """Test marking a task as completed."""
    task_id = database.add_task("Review pull request", "Medium")
    success = database.complete_task(task_id)
    assert success is True

    tasks = database.get_all_tasks()
    assert tasks[0]["status"] == "Completed"


def test_delete_task():
    """Test deleting a task from the database."""
    task_id = database.add_task("Temporary task", "Low")
    success = database.delete_task(task_id)
    assert success is True

    tasks = database.get_all_tasks()
    assert len(tasks) == 0