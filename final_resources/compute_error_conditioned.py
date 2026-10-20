"""Recalculate descriptive correction rates using every released question row."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import csv,json
root=Path(__file__).resolve().parent.parent
source=root/'revision_2026_analyses/question_level_revision.csv'
counts=defaultdict(lambda:dict(n=0,errors=0,rescues=0))
with source.open(encoding='utf-8-sig',newline='') as f:
    for r in csv.DictReader(f):
        c=counts[(r['run'],int(r['quartile']))];c['n']+=1
        if int(r['baseline_correct'])==0:
            c['errors']+=1;c['rescues']+=int(r['guided_correct'])
rows=[dict(evaluation=run,quartile=q,**c,rescue_rate_among_errors=float(Fraction(c['rescues'],c['errors'])))
      for (run,q),c in sorted(counts.items())]
saved=json.loads((root/'final_resources/error_conditioned_rescue.json').read_text())
assert rows==saved,(rows,saved)
print(json.dumps({'status':'PASS','strata':len(rows),'questions':sum(r['n'] for r in rows)},indent=2))
