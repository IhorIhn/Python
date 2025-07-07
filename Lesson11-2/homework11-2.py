import os
import re
from log_event_module import log_event, LOG_FILE, logger

def log_separator():
    logger.info("=" * 50)

if __name__ == "__main__":
    log_separator()
    log_event("admin", "success")



def flush_logger():
    for handler in logger.handlers:
        handler.flush()

def read_log_file():
    assert os.path.exists(LOG_FILE), "Файл логування не створено"
    with open(LOG_FILE, "r") as f:
        return f.read()

def test_log_success():
    log_event("alice", "success")
    flush_logger()
    content = read_log_file()
    assert "INFO" in content
    assert "Username: alice, Status: success" in content

def test_log_expired():
    log_event("bob", "expired")
    flush_logger()
    content = read_log_file()
    assert "WARNING" in content
    assert "Username: bob, Status: expired" in content

def test_log_failed():
    log_event("carol", "failed")
    flush_logger()
    content = read_log_file()
    assert "ERROR" in content
    assert "Username: carol, Status: failed" in content

def test_log_unknown():
    log_event("dave", "invalid")
    flush_logger()
    content = read_log_file()
    assert "ERROR" in content
    assert "Username: dave, Status: invalid" in content

def test_logger_format():
    log_event("eve", "success")
    flush_logger()
    content = read_log_file()
    assert " - INFO - Login event - Username: eve, Status: success" in content

def test_log_with_invalid_types():
    log_event(123, None)
    flush_logger()
    content = read_log_file()
    assert "ERROR" in content
    assert "Username: 123, Status: None" in content

def test_log_format():
    log_event("testuser", "success")
    content = read_log_file()
    pattern = pattern = r"\d{4}/\d{2}/\d{2}.* - INFO - Login event - Username: testuser, Status: success"
    assert re.search(pattern, content), "Лог не відповідає очікуваному формату"
