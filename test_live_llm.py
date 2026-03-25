"""Quick live E2E test: create student → run analysis → generate report → check source."""
import httpx
import sys

BASE = "http://localhost:8000"

# Create student
r = httpx.post(f"{BASE}/api/students", json={
    "name": "Live Test",
    "standard": "10th",
    "board": "CBSE",
    "state": "Maharashtra",
    "year_of_study": 2025,
    "percentage_10th": 85.0,
    "stream_interest": "Engineering & Technology",
}, timeout=10)
assert r.status_code == 200, f"Create student failed: {r.status_code}"
student_id = r.json()["id"]
print(f"Student created: {student_id}")

# Run analysis
r = httpx.post(f"{BASE}/api/analysis/{student_id}", timeout=30)
assert r.status_code == 200, f"Analysis failed: {r.status_code}"
analysis_id = r.json()["id"]
print(f"Analysis created: {analysis_id}")

# Generate report (this calls the LLM pipeline)
print("Generating report via LLM pipeline... (this may take ~60s)")
r = httpx.post(f"{BASE}/api/report/{analysis_id}", timeout=300)
assert r.status_code == 200, f"Report failed: {r.status_code} {r.text}"
data = r.json()
source = data["enrichment"]["source"]
print(f"\nReport source: {source}")
print(f"Executive summary (first 200 chars): {data['enrichment']['executive_summary'][:200]}")
print(f"\nStream recommendation (first 200 chars): {data['enrichment']['stream_recommendation_narrative'][:200]}")

if source == "llm":
    print("\n✓ SUCCESS: Report generated using Ollama LLM!")
else:
    print(f"\n✗ FALLBACK: Report used '{source}' instead of LLM")
    sys.exit(1)
