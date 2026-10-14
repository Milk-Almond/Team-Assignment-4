# Team Lab 4 test record — `lab4-team-candidate-v0.1`

## Method and limits

The three case inputs are **constructed teaching scenarios**, not accounts of real firms. The saved response JSON files are model-assisted analytical demonstrations written with the proposed rules visible. They are not blind runs of a deployed agent or evidence of future reliability. The local checks verify the frozen scaffold, prompt construction, response shape, and the explicit context invariant; a human team must challenge the reasoning in the workshop.

| Case | Controlled change | Saved result | Competing view and discriminating evidence |
| --- | --- | --- | --- |
| `primary.json` | Existing LLM; human-reviewed replies; fictional hourly-billed outsourcer | Prospective incremental application; High **conditional** organizational significance because billable-hour economics may be exposed | Moderate if time savings improve capacity or quality without repricing. Check contracts, margins, client renewal and pilot results. |
| `context_contrast.json` | **Same technology and application**; fictional manufacturer's internal cost-center desk | Exact same general and application finding; Low **conditional** organizational significance because product sales remain core | Moderate if warranty operations or customer retention materially change. Check full reviewed cost and product/customer effects. |
| `borderline.json` | Same technology and stated application; deployment and prior workflow unverified | Global invention and commercial success unproven; prospective vs implemented and incremental vs breakthrough remain open; significance Withheld | Deployment logs, before/after roles/autonomy, customer terms and revenue mix decide the competing labels. |

The context contrast is deliberately limited: it shows how the *rules and saved outputs* separate technology classification from organizational significance. It does not prove that the model will do so reliably in an unseen run. The borderline output preserves at least two plausible classifications and does not convert a manager's “revolutionary” claim into evidence.

## Informative weakness retained from candidate work

Shuoying Wang's [pre-revision weak response](https://github.com/yicrry777/1800Lab3/blob/assignment-3-innovation-disruption/agents/innovation_disruption_agent/responses/primary_pre_revision_weak.json) passed a structural validator while claiming certain existential disruption from hourly exposure. Meilin's [first fintech response](https://github.com/mp7240-sudo/MASY1800-Emerging-Technology-Innovation-Disruption-Agent/blob/main/agents/innovation_disruption_agent/responses/contrast_1_response_v1.json) withheld a single label yet allowed an unhelpfully wide conditional range. Yulia's [test record](https://github.com/yanisimova/Sub-Agent-2-Cycles/blob/main/Anisimova_Assignment_3_Agent_Package/innovation_disruption/records/test_record.md) also preserves generic timing-risk language in earlier outputs. These are different failure modes, not failures of the current three saved outputs.

**Revision embodied in this synthesis:** separate stage, degree, and organizational significance; require a named comparator; show a competing adjacent interpretation; withhold when decisive baseline information is absent; tie monitoring to observable evidence. No claim is made that these changes were tested in independent fresh-context model runs.

## Executed verification

See `tests/check_cases.py` and the standard course tools. The test checks exact schema keys and the intended stable/change pattern; it does not establish factual accuracy or team approval. Record actual classroom prompts, outputs, dissent, reviewer names, and any resulting revision in the Agent Record before promotion.
