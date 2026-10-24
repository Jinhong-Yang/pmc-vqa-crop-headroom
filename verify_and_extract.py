"""Verify archived data and optionally reproduce all CPU analyses in a new folder."""
from pathlib import Path
import argparse,hashlib,json,zipfile,subprocess,sys,shutil,datetime,os
p=argparse.ArgumentParser();p.add_argument('--destination',required=True);p.add_argument('--run',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parent;dest=Path(args.destination).resolve()
assert not dest.exists(),f'Choose a fresh destination: {dest}'
manifest=json.loads((root/'SHA256SUMS.json').read_text())
def archive_path(name):
    path=root/name
    return path if path.exists() else root/Path(name).name
for name,digest in manifest.items():assert hashlib.sha256(archive_path(name).read_bytes()).hexdigest()==digest,name
dest.mkdir(parents=True)
for name in sorted(manifest,key=lambda n:int(Path(n).name.split('_')[0][1:])):
    with zipfile.ZipFile(archive_path(name)) as z:
        for info in z.infolist():
            target=(dest/info.filename).resolve()
            assert target.is_relative_to(dest),info.filename
        z.extractall(dest)
shutil.copytree(root/'final_resources',dest/'final_resources',dirs_exist_ok=True)
shutil.copytree(root/'current_release_figures',dest/'current_release_figures',dirs_exist_ok=True)
commands=[
['reproducibility_bundle/portable_reanalysis.py','reproducibility_bundle'],
['rerun_additional_analysis.py'],['verify_additional_analysis.py'],
['reproduce_added_analyses.py'],
['window_audit_20261019/analyze_windows.py'],['window_audit_20261019/review_checks.py'],['window_audit_20261019/verify_windows.py'],
['review_extension_20261019/analyze_extension.py'],['review_extension_20261019/verify_extension.py'],
['content_checks_20261019/analyze_content.py'],['content_checks_20261019/verify_content.py'],
['revision_2026_analyses/portable_reproduce.py'],
['final_resources/compute_error_conditioned.py'],
['current_figures/build_figures.py'],['final_resources/create_figure1.py'],
['review_controls_20261024/reproduce_release.py'],
['order_averaging_20261024/reproduce_release.py'],
['current_release_figures/build_current_figures.py']]
receipt={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_hashes':manifest,'commands':[],'status':'EXTRACTED'}
if args.run:
    logs=dest/'reproduction_logs';logs.mkdir()
    for i,command in enumerate(commands,1):
        log=logs/f'{i:02d}_{Path(command[0]).stem}.log'
        with log.open('w',encoding='utf-8') as f:
            process=subprocess.run([sys.executable,'-X','utf8',*command],cwd=dest,stdout=f,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONIOENCODING':'utf-8'})
        receipt['commands'].append({'command':command,'exit_code':process.returncode,'log':str(log.relative_to(dest))})
        receipt['status']='RUNNING' if process.returncode==0 else 'FAILED'
        (dest/'reproduction_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
        print(i,command[0],process.returncode,flush=True)
        if process.returncode:raise SystemExit(process.returncode)
    receipt['status']='PASS'
receipt['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(dest/'reproduction_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(receipt['status'],dest)
