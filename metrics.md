# System Metrics Reference

## 🏆 Core Metrics

| Metric | Why It Matters |
|---|---|
| CPU % per core | Catches rogue processes pinning one core |
| Memory % used | Memory leaks show up clearly here |
| Bytes sent/recv delta | Sudden spikes may indicate suspicious network activity |
| Disk read/write bytes | Ransomware typically causes massive disk write spikes |
| Process count | A sudden jump means something is spawning processes |

---

## 🥈 Secondary Metrics

| Metric | Why It Matters |
|---|---|
| CPU load average (1m, 5m, 15m) | Smoothed signal, less noisy than raw CPU % |
| Swap memory used | Indicates the system is under memory pressure |
| Open file descriptors | Reveals file descriptor leaks |
| Context switches / sec | High values indicate thrashing or scheduler stress |
| Top 3 processes by CPU | Identifies who is causing the anomaly |

---

## 🥉 Stretch Metrics

| Metric | Why It Matters |
|---|---|
| Per-process CPU & memory | Fine-grained blame assignment per process |
| Network connections count | Too many open sockets may indicate suspicious activity |
| Battery drain rate | Catches unexpected background drain on laptops |
| Temperature sensors | Detects thermal throttling |
| `/proc/vmstat` page faults | Deep signal for memory pressure |
