from app import detect_metric

def test_metric_detection():
    assert detect_metric("When will disk usage hit 80%?") == "Disk"
    assert detect_metric("CPU usage forecast") == "CPU"
    assert detect_metric("Memory alert prediction") == "Memory"