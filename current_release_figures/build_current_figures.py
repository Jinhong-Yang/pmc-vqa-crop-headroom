from pathlib import Path
import json,runpy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
V=Path(__file__).resolve().parent;O=V/'figures';O.mkdir(exist_ok=True)
runpy.run_path(str(V/'create_figure1.py'))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'ps.fonttype':42,'pdf.fonttype':42,'savefig.facecolor':'white'})
data=json.loads((V/'figure_S2_source_values.json').read_text())
labels=list(dict.fromkeys(r['cohort_model'] for r in data));fig,ax=plt.subplots(figsize=(7,3.8));ax.axvline(0,color='#555555',lw=.8)
for i,label in enumerate(labels):
 for shift,name,color,marker in [(.11,'All controls','#007F89','o'),(-.11,'Zero overlap','#C56321','s')]:
  r=next(v for v in data if v['cohort_model']==label and v['condition']==name);m=r['estimate']*100;lo,hi=np.array(r['ci95'])*100
  ax.errorbar(m,3-i+shift,xerr=[[m-lo],[hi-m]],fmt=marker,color=color,capsize=3,label=name if i==0 else None)
  ax.text(2.7,3-i+shift,f"n = {r['n']:,}",va='center',size=8)
ax.set_yticks(np.arange(4)[::-1],labels);ax.set_xlim(-2.8,4);ax.set_xlabel('Guided minus mean control oracle (percentage points)');ax.legend(frameon=False,ncol=2,loc='upper center',bbox_to_anchor=(.5,1.18));fig.tight_layout()
for ext in ['png','eps']:fig.savefig(O/f'FigS2.{ext}',dpi=400,bbox_inches='tight')
with Image.open(O/'FigS2.png') as im:im.convert('RGB').save(O/'FigS2.tif',compression='tiff_lzw',dpi=(400,400))
plt.close(fig)
print('Current Figure 1 and S2 generated from included source values. No planning band.')
