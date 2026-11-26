import numpy as np, wave, sys
sr=44100; dur=float(sys.argv[2]); out=sys.argv[1]
ticks=[float(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else []
t=np.arange(int(sr*dur))/sr
def hz(n): return 440*2**((n-69)/12)
chords=[[57,60,64,45],[53,57,60,41],[48,52,55,60],[55,59,62,43]]  # Am F C G
seg=dur/4
pad=np.zeros_like(t)
for i,ch in enumerate(chords):
    s0=i*seg; m=(t>=s0-0.6)&(t<s0+seg+0.6)
    tt=t[m]-s0
    env=np.clip(np.minimum((tt+0.6)/1.2,(seg+0.6-tt)/1.2),0,1)**1.5
    for n in ch:
        f=hz(n)
        for d in (-0.15,0.15):
            pad[m]+=env*np.sin(2*np.pi*(f+d)*tt)*(0.5 if n<50 else 0.22)
# soft pulse on beats (~92 bpm)
beat=60/92
pulse=np.zeros_like(t)
for b in np.arange(0.0,dur,beat):
    m=(t>=b)&(t<b+0.25); tt=t[m]-b
    pulse[m]+=np.sin(2*np.pi*55*tt)*np.exp(-tt*18)*0.5
# ticks at visual events
tick=np.zeros_like(t)
for k in ticks:
    m=(t>=k)&(t<k+0.09); tt=t[m]-k
    tick[m]+=np.sin(2*np.pi*1150*tt)*np.exp(-tt*55)*0.35
mix=pad*0.55+pulse*0.6+tick
# master fades
fade=np.ones_like(t); fade[t<0.4]=t[t<0.4]/0.4; e=t>dur-1.6; fade[e]=(dur-t[e])/1.6
mix*=fade
mix/=np.max(np.abs(mix))+1e-9; mix*=0.45
st=np.stack([mix,mix],1)
with wave.open(out,'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes())
print('audio ok', out)
