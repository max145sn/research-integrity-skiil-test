import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).parents[1]

def valid_ledger(tmp_path):
    return {
      "audit_id":"A-1","package":{"title":"Test","scope_status":"COMPLETE"},
      "files":[{"file_id":"FILE-1","path":"data.csv","classification":"STRUCTURED_DATA","readable":True}],
      "section_coverage":[{"section":"Results","status":"READ","claims_identified":1,"claims_classified":1}],
      "studies":[{"study_id":"S-1"}],
      "claims":[{"claim_id":"C-001","canonical_text":"There are two taxa","centrality":"DESCRIPTIVE","population_id":"P-001","calculation_required":True,"outcome":"MATCH"}],
      "populations":[{"population_id":"P-001","source_file_ids":["FILE-1"],"unit_of_analysis":"taxon","inclusion_rules":["count > 0"],"exclusion_rules":["taxon != ND"],"placeholder_handling":"exclude ND","missing_value_handling":"exclude","grouping":[],"mapping_confidence":"CONFIRMED"}],
      "findings":[],"limitations":[],
      "coverage":{"claims_total":1,"claim_outcomes":{"MATCH":1},"reconciliation":"PASS"},
      "validation":{"status":"NOT_RUN","errors":[],"warnings":[]}
    }

def test_valid_ledger(tmp_path):
    p=tmp_path/'ledger.json'; p.write_text(json.dumps(valid_ledger(tmp_path)))
    r=subprocess.run([sys.executable,str(ROOT/'scripts/validate_audit.py'),str(p)],capture_output=True,text=True)
    assert r.returncode==0
    assert json.loads(p.read_text())['validation']['status']=='PASS'

def test_coverage_failure(tmp_path):
    d=valid_ledger(tmp_path); d['coverage']['claims_total']=2
    p=tmp_path/'ledger.json'; p.write_text(json.dumps(d))
    r=subprocess.run([sys.executable,str(ROOT/'scripts/validate_audit.py'),str(p)],capture_output=True,text=True)
    assert r.returncode==1
    assert json.loads(p.read_text())['validation']['status']=='FAILED'
