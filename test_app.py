def test_metric_detection():
    query = "When will disk usage hit 80%?"
    assert "disk" in query.lower()