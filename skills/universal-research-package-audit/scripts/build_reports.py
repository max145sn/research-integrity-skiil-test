#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def esc(x): return str(x).replace('|','\\|').replace('\n',' ')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('ledger'); ap.add_argument('--technical',required=True); ap.add_argument('--brief',required=True); a=ap.parse_args()
    d=json.loads(Path(a.ledger).read_text(encoding='utf-8'))
    val=d.get('validation',{}).get('status','NOT_RUN')
    findings=d.get('findings',[]); limitations=d.get('limitations',[])
    tech=[f"# {d['package']['title']}: Comprehensive Technical Audit","",f"**Validation:** {val}","","## Findings"]
    for f in findings:
        tech += [f"### {f['finding_id']}: {f['title']}","",f"- Type: {f['item_type']}",f"- Assessment: {f['assessment_label']}",f"- Severity: {f['severity']}",f"- Verification impact: {f['verification_impact']}",f"- Result-correctness impact: {f['result_correctness_impact']}",""]
    tech += ["## Limitations"]
    for f in limitations: tech += [f"- **{f['finding_id']} {f['title']}**: {f['assessment_label']}"]
    tech += ["", "## Coverage", "", f"Claims: {d.get('coverage',{}).get('claims_total',0)}", "", f"Output validation: {val}"]
    Path(a.technical).write_text('\n'.join(tech)+'\n',encoding='utf-8')
    brief=[f"# {d['package']['title']}: Review Brief","","## Review at a glance","","| Area | Assessment | What this means |","|---|---|---|",f"| Audit output | {val} | The ledger validator returned {val}. |","","## Issues requiring attention","","| Priority | Assessment | Issue | Why it matters | Reviewer action |","|---:|---|---|---|---|"]
    for f in sorted([x for x in findings if x.get('include_in_brief',True)],key=lambda x:x.get('review_priority',999)):
        brief.append(f"| {f.get('review_priority','')} | {esc(f['assessment_label'])} | [{esc(f['finding_id'])}] {esc(f['title'])} | Verification: {esc(f['verification_impact'])}; result correctness: {esc(f['result_correctness_impact'])}. | {esc(f.get('reviewer_action','Review the detailed audit.'))} |")
    brief += ["","## What could not be verified","","| Assessment | Item | Meaning |","|---|---|---|"]
    for f in limitations: brief.append(f"| {esc(f['assessment_label'])} | [{esc(f['finding_id'])}] {esc(f['title'])} | This limits verification and does not by itself show the research result is wrong. |")
    brief += ["","## Bottom line","","- **What is good:** See completed positive checks in the technical audit.","- **What needs attention:** See the concern rows above.","- **What remains unknown:** See the verification and audit limitations.","- **What this does not mean:** The audit does not infer misconduct or make a publication decision.","",f"**Output validation:** {val}"]
    Path(a.brief).write_text('\n'.join(brief)+'\n',encoding='utf-8')
    print(json.dumps({'technical':a.technical,'brief':a.brief,'validation':val}))
if __name__=='__main__': main()
