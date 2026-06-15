# Test Cases

## Test Case 1 – CPU Forecast Prediction

**Input Query:**

```
when will cpu hit 120?
```

**Expected Output:**

```
CPU utilization is expected to reach 120 on 18-03-2026.
```

---

## Test Case 2 – Memory Forecast Prediction

**Input Query:**

```
when will memory hit 130?
```

**Expected Output:**

```
Memory utilization is expected to reach 130 on 12-03-2026.
```

---

## Test Case 3 – Disk Forecast Prediction

**Input Query:**

```
when will disk hit 130?
```

**Expected Output:**

```
Disk utilization is expected to reach 130 on 13-03-2026.
```

---

## Test Case 4 – Threshold Not Reached

**Input Query:**

```
when will cpu hit 300?
```

**Expected Output:**

```
Threshold not expected to be reached within the forecast horizon (30 days).
```

---

## Test Case 5 – Invalid Query Handling

**Input Query:**

```
hello
```

**Expected Output:**

```
Invalid query format.
Please ask questions like:
"When will disk hit 130?"
"When will cpu hit 80?"
```

---

## Test Case 6 – Unsupported Metric

**Input Query:**

```
when will network hit 100?
```

**Expected Output:**

```
Unsupported metric.
Available metrics: CPU, Memory, Disk.
```
