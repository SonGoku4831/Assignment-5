import subprocess,sys,pathlib,textwrap
from PIL import Image,ImageDraw,ImageFont
root=pathlib.Path(__file__).resolve().parent
name,command=sys.argv[1:3]
p=subprocess.run(command,shell=True,cwd=root,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
text='$ '+command+'\n\n'+p.stdout+'\nExit status: '+str(p.returncode)
(root/'evidence'/f'{name}.txt').write_text(text)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',15)
lines=[]
for line in text.splitlines(): lines.extend(textwrap.wrap(line,125,replace_whitespace=False,drop_whitespace=False) or [''])
for page,offset in enumerate(range(0,len(lines),90),1):
    subset=lines[offset:offset+90]; im=Image.new('RGB',(1180,60+len(subset)*21),'#101923'); d=ImageDraw.Draw(im)
    for i,line in enumerate(subset): d.text((20,20+i*21),line,font=font,fill='#dce8ef')
    im.save(root/'evidence'/f'{name}_{page:02}.png')
print(text)
sys.exit(p.returncode)
