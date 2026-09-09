#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, RefResolver

def duplicates(values):
    seen=set(); dup=set()
    for v in values:
        if v in seen: dup.add(v)
        seen.add(v)
    return sorted(dup)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('ledger'); ap.add_argument('--schema',default=str(Path(__file__).parents[1]/'schemas/audit-ledger.schema.json')); a=ap.parse_args()
    ledger_path=Path(a.ledger); schema_path=Path(a.schema)
    data=json.loads(ledger_path.read_text(encoding='utf-8')); schema=json.loads(schema_path.read_text(encoding='utf-8'))
    resolver=RefResolver(base_uri=schema_path.parent.as_uri()+'/',referrer=schema)
    errors=[f'{list(e.path)}: {e.message}' for e in Draft202012Validator(schema,resolver=resolver).iter_errors(data)]
    warnings=[]
    claim_ids=[x.get('claim_id') for x in data.get('claims',[])]
    finding_ids=[x.get('finding_id') for x in data.get('findings',[])+data.get('limitations',[])]
    if duplicates(claim_ids): errors.append(f'Duplicate claim IDs: {duplicates(claim_ids)}')
    if duplicates(finding_ids): errors.append(f'Duplicate finding/limitation IDs: {duplicates(finding_ids)}')
    claim_set=set(claim_ids)
    for item in data.get('findings',[])+data.get('limitations',[]):
        missing=[x for x in item.get('claim_ids',[]) if x not in claim_set]
        if missing: errors.append(f"{item.get('finding_id')} references missing claims {missing}")
        if item.get('impact_status')=='NOT_EVALUATED' and item.get('severity') not in {'UNDETERMINED','NOT_APPLICABLE'}:
            errors.append(f"{item.get('finding_id')} has unsupported severity")
    cov=data.get('coverage',{}); total=cov.get('claims_total',0); subtotal=sum(cov.get('claim_outcomes',{}).values())
    if total!=subtotal: errors.append(f'Coverage mismatch: claims_total={total}, outcomes={subtotal}')
    if cov.get('reconciliation')=='PASS' and total!=subtotal: errors.append('Coverage marked PASS despite mismatch')
    for claim in data.get('claims',[]):
        if claim.get('outcome') in {'MATCH','ROBUST_MISMATCH','SPECIFICATION_DEPENDENT'} and not claim.get('population_id') and claim.get('calculation_required',False):
            warnings.append(f"{claim.get('claim_id')} has calculation outcome without population record")
    status='FAILED' if errors else ('CONDITIONAL_PASS' if warnings else 'PASS')
    result={'status':status,'errors':errors,'warnings':warnings}
    data['validation']=result; ledger_path.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
    sys.exit(1 if errors else 0)
if __name__=='__main__': main()
