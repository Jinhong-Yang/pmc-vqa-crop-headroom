"""Vector schematic of the actual design; contains no synthetic experimental values."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image

V=Path(__file__).resolve().parent;O=V/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'pdf.fonttype':42,'ps.fonttype':42})
fig=plt.figure(figsize=(7.2,7.4),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,7.2),ylim=(0,7.4));ax.axis('off')
ink='#202B33';muted='#52616B';blue='#007A87';orange='#B75B15';line='#C6CFD4'
def text(x,y,t,size=8,weight='normal',color=ink,ha='left',va='top'):
    return ax.text(x,y,t,fontsize=size,fontweight=weight,color=color,ha=ha,va=va,linespacing=1.35)
def box(x,y,w,h,title,body,color=line):
    ax.add_patch(Rectangle((x,y),w,h,facecolor='white',edgecolor=color,lw=1))
    text(x+.12,y+h-.12,title,8.8,'bold',color if color!=line else ink)
    text(x+.12,y+h-.37,body,8)
def arrow(x1,y1,x2,y2,color=muted):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=9,lw=1,color=color))
def heading(y,letter,title):
    text(.22,y,letter,12,'bold');text(.52,y,title,10.5,'bold')
heading(7.19,'A','Cohorts and analysis sequence')
box(.22,5.98,1.90,.85,'Discovery','1,350 questions\n21,600 predictions')
box(2.53,5.98,1.92,.85,'Technical pilots','128 primary + 64 curated\nExcluded from main estimates')
box(4.86,5.98,2.12,.85,'Main evaluation','2,048 primary + 825 curated\nSame questions, 2B and 4B',blue)
arrow(2.14,6.40,2.5,6.40);arrow(4.47,6.40,4.83,6.40)
text(.23,5.82,'Frozen models; local protocol freezes and linkage exclusions (not external registration).',7.7,color=muted)
ax.plot([.22,6.98],[5.56,5.56],color=line,lw=.8)
heading(5.4,'B','One crop response per arm; matched visual budget')
text(.23,4.98,'Nine overlapping windows',8.7,'bold')
text(.23,4.77,'Width = height = 1/2 of image',7.4,color=muted)
# Small multiples display every half-frame crop unambiguously.
for j in range(9):
    r,c=divmod(j,3);x=.25+c*.52;y=3.02+(2-r)*.52
    ax.add_patch(Rectangle((x,y),.43,.43,facecolor='white',edgecolor=line,lw=.7))
    ax.add_patch(Rectangle((x+(c*.25)*.43,y+(.5-r*.25)*.43),.215,.215,facecolor='#D6E9EB',edgecolor=blue,lw=.8))
    text(x+.025,y+.04,str(j),6.6,va='bottom')
text(.23,2.83,'Offsets: 0, 1/4, 1/2 per axis',7.4,color=muted)
arrow(1.89,3.82,2.22,3.82)
box(2.24,3.35,1.50,.91,'SigLIP 2 ranking','Question-to-crop\nsimilarity; no labels',blue)
arrow(3.76,4.01,4.13,4.49,blue);arrow(3.76,3.61,4.13,3.43,orange)
box(4.16,4.02,2.82,.91,'Guided response G','Global image + highest-ranked crop',blue)
box(4.16,2.87,2.82,.91,'Control response U\u209b','Global image + one of eight other crops\nSeeds 1, 7, 42; repetitions retained',orange)
text(2.24,3.15,'Baseline response B',8.2,'bold')
text(2.24,2.92,'Question + global image',7.6)
text(.23,2.49,'Guided / controls: same question, options, global image, extra-view dimensions and tokens.',7.6,color=muted)
ax.plot([.22,6.98],[2.26,2.26],color=line,lw=.8)
heading(2.1,'C','Separate available answers from improved decisions')
text(.23,1.71,'Locally prespecified primary: 2B, primary cohort',8.6,'bold')
text(.23,1.40,r'$D_i=\max(B_i,G_i)-\frac{1}{3}\sum_{s\in\{1,7,42\}}\max(B_i,U_{is})$',11.2)
text(.23,.97,'Two candidates in every oracle pair; reference labels choose the correct answer.',7.6,color=muted)
text(.23,.66,'Decision check',8.1,'bold',blue)
text(.23,.43,'Direct accuracy, rescue / harm,\nand executable answer selection',7.6)
text(3.73,.66,'Completed-grid sensitivity',8.1,'bold',orange)
text(3.73,.43,'All eight non-selected pair oracles;\nbaseline + nine crops for union coverage',7.6)
fig.savefig(O/'Fig1.pdf')
fig.savefig(O/'Fig1.eps')
fig.savefig(O/'Fig1.svg')
fig.savefig(O/'Fig1.png',dpi=300)
fig.savefig(O/'Fig1.tif',dpi=600,pil_kwargs={'compression':'tiff_lzw'})
with Image.open(O/'Fig1.tif') as im:
    im.convert('RGB').save(O/'Fig1.tif',compression='tiff_lzw',dpi=(600,600))
print('Figure 1: 7.2 x 7.4 in; vector PDF/EPS/SVG + 600 dpi RGB TIFF')
