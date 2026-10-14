#!/usr/bin/env python3
"""Check saved Lab 4 examples against the unchanged course output contract."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "agents" / "innovation_classification"
schema = json.loads((ROOT / "core" / "output_schema.json").read_text())
required = set(schema["required"])
allowed = set(schema["properties"])
cases = {}
responses = {}
for name in ("primary", "context_contrast", "borderline"):
    cases[name] = json.loads((AGENT / "cases" / f"{name}.json").read_text())
    responses[name] = json.loads((AGENT / "responses" / f"{name}_response.json").read_text())
    assert set(cases[name]) >= set(json.loads((ROOT / "core" / "input_schema.json").read_text())["required"])
    assert set(responses[name]) == required == allowed
    assert responses[name]["agent"]["version"] == "lab4-team-candidate-v0.1"
    assert responses[name]["evidence"] and responses[name]["contrary_evidence_or_limitations"]
    assert "Organizational Significance:" in responses[name]["organization_specific_finding"]

assert len({cases[n]["emerging_technology"] for n in cases}) == 1
assert len({cases[n]["intended_application"] for n in cases}) == 1
assert responses["primary"]["general_et_finding"] == responses["context_contrast"]["general_et_finding"]
assert responses["primary"]["application_finding"] == responses["context_contrast"]["application_finding"]
assert "Significance: High" in responses["primary"]["organization_specific_finding"]
assert "Significance: Low" in responses["context_contrast"]["organization_specific_finding"]
assert "Significance: Withheld" in responses["borderline"]["organization_specific_finding"]
assert "competing" in " ".join(responses["borderline"]["contrary_evidence_or_limitations"])
print("CASE CONTRACT AND CONTEXT CONTRAST PASSED")
