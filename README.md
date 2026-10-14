# Team Lab 4 — Innovation Classification Agent

**Status:** unanimously approved by five team members in the October 13, 2026 workshop (team-reported). **Version:** `lab4-team-approved-v1.0`, approved from merge commit `b635e695148e42b639771f15a5102752da43d711`. Saved demonstrations remain labeled candidate v0.1; no independent rerun is claimed.

This repository starts from the course's frozen MASY1800 specialist context/output contract. The seven files listed in `FROZEN_CORE_SHA256.txt` are byte-for-byte copies of the supplied scaffold. Team edits live in `agents/innovation_classification/` and `tests/`.

See [Team Agent Inventory](TEAM_AGENT_INVENTORY.md) and [Team Decision Log](TEAM_DECISION_LOG.md) for approval and handoff.

## Review order

1. Read [the comparison and Team Agent Record](agents/innovation_classification/records/team_agent_record.md), including retained analytical ambiguity and unanimous approval.
2. Challenge [the classification criteria](agents/innovation_classification/specialist_instructions.md) against the three [constructed cases](agents/innovation_classification/cases/).
3. Inspect [the saved demonstration outputs](agents/innovation_classification/responses/) and [test record](agents/innovation_classification/records/test_record.md). These are model-assisted examples, not blind or field validation.
4. Consult the Agent Record for the team's unanimous decision and retained limits. The prior candidate PR is already merged; this record update promotes the approved version without altering frozen core.

## Run the course contract checks

```sh
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/innovation_classification --case agents/innovation_classification/cases/primary.json --out /tmp/lab4_primary_prompt.txt
python3 tools/validate_response.py agents/innovation_classification/responses/primary_response.json
python3 tests/check_cases.py
```

The prompt packet is for a ChatGPT specialist run under the common course workflow. The checks verify file integrity, JSON shape, and the stated context contrast using saved candidate v0.1 responses. Human reviewers must still judge evidence quality and classification logic.

**Integration warning:** a first use inside a firm can be highly significant there while the underlying technology is already known. Do not promote a firm's workflow impact to a global invention or Promethean breakthrough, and do not let this specialist make an adoption decision.
