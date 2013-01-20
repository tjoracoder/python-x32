import itertools
settings_from_doc = """--------- config data ---------
/config/chlink/1-2 enum {OFF,ON}
/config/chlink/3-4 enum {OFF,ON}
/config/chlink/5-6 enum {OFF,ON}
/config/chlink/7-8 enum {OFF,ON}
/config/chlink/9-10 enum {OFF,ON}
/config/chlink/11-12 enum {OFF,ON}
/config/chlink/13-14 enum {OFF,ON}
/config/chlink/15-16 enum {OFF,ON}
/config/chlink/17-18 enum {OFF,ON}
/config/chlink/19-20 enum {OFF,ON}
/config/chlink/21-22 enum {OFF,ON}
/config/chlink/23-24 enum {OFF,ON}
/config/chlink/25-26 enum {OFF,ON}
/config/chlink/27-28 enum {OFF,ON}
/config/chlink/29-30 enum {OFF,ON}
/config/chlink/31-32 enum {OFF,ON}
/config/auxlink/1-2 enum {OFF,ON}
/config/auxlink/3-4 enum {OFF,ON}
/config/auxlink/5-6 enum {OFF,ON}
/config/auxlink/7-8 enum {OFF,ON}
/config/fxlink/1-2 enum {OFF,ON}
/config/fxlink/3-4 enum {OFF,ON}
/config/fxlink/5-6 enum {OFF,ON}
/config/fxlink/7-8 enum {OFF,ON}/config/buslink/1-2 enum {OFF,ON}
/config/buslink/3-4 enum {OFF,ON}
/config/buslink/5-6 enum {OFF,ON}
/config/buslink/7-8 enum {OFF,ON}
/config/buslink/9-10 enum {OFF,ON}
/config/buslink/11-12 enum {OFF,ON}
/config/buslink/13-14 enum {OFF,ON}
/config/buslink/15-16 enum {OFF,ON}
/config/mtxlink/1-2 enum {OFF,ON}
/config/mtxlink/3-4 enum {OFF,ON}
/config/mtxlink/5-6 enum {OFF,ON}
/config/mute/[1..6] enum {OFF,ON}
/config/linkcfg/hadly enum {OFF,ON}
/config/linkcfg/eq enum {OFF,ON}
/config/linkcfg/dyn enum {OFF,ON}
/config/linkcfg/fdrmute enum {OFF,ON}
/config/mono/mode enum {LR+M,LCR}
/config/mono/link enum {OFF,ON}
/config/solo/level level [0.0...1.0 (+10 dB), 161] dB
/config/solo/source enum {OFF,LR,LR+C,LRPFL,LRAFL,AUX56,AUX78}
/config/solo/sourcetrim linf [-18.000,18.000,0.500] dB
/config/solo/chmode enum {PFL,AFL}
/config/solo/busmode enum {PFL,AFL}
/config/solo/dcamode enum {PFL,AFL}
/config/solo/exclusive enum {OFF,ON}
/config/solo/followsel enum {OFF,ON}
/config/solo/followsolo enum {OFF,ON}
/config/solo/dimatt linf [-40.000,0.000,1.000] dB
/config/solo/dim enum {OFF,ON}
/config/solo/mono enum {OFF,ON}
/config/solo/delay enum {OFF,ON}
/config/solo/delaytime linf [0.300,500.000,0.100] ms
/config/solo/masterctrl enum {OFF,ON}
/config/solo/mute enum {OFF,ON}
/config/solo/dimpfl enum {OFF,ON}
/config/talk/enable enum {OFF,ON}
/config/talk/source enum {INT,EXT}
/config/talk/A/level level [0.0...1.0 (+10 dB), 161] dB
/config/talk/A/dim enum {OFF,ON}
/config/talk/A/latch enum {OFF,ON}
/config/talk/A/destmap int [0,262143] (bitmap)
/config/talk/B/level level [0.0...1.0 (+10 dB), 161] dB
/config/talk/B/dim enum {OFF,ON}
/config/talk/B/latch enum {OFF,ON}
/config/talk/B/destmap int [0,262143] (bitmap)
/config/osc/level level [0.0...1.0 (+10 dB), 161] dB
/config/osc/f1 logf [20.000,20000,121] Hz/config/osc/f2 logf [20.000,20000,121] Hz
/config/osc/fsel enum {F1,F2}
/config/osc/type enum {SINE,PINK,WHITE}
/config/osc/dest int [0,25]
/config/routing/IN/1-8 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32}
/config/routing/IN/9-16 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32}
/config/routing/IN/17-24 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32}
/config/routing/IN/25-32 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32}
/config/routing/IN/AUX1-4 enum {AUX1-4,AN1-4,A1-4,B1-4,CARD1-
4}
/config/routing/AES50A/1-8 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50A/9-16 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50A/17-24 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50A/25-32 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50A/33-40 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}/config/routing/AES50A/41-48 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/1-8 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/9-16 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/17-24 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/25-32 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/33-40 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/AES50B/41-48 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/CARD/1-8 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/CARD/9-16 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}/config/routing/CARD/17-24 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/routing/CARD/25-32 enum {AN1-8,AN9-16,AN17-24,AN25-32,A1-8,A9-
16,A17-24,A25-32,A33-40,A41-48,B1-8,B9-
16,B17-24,B25-32,B33-40,B41-48,CARD1-
8,CARD9-16,CARD17-24,CARD25-32,OUT1-
8,OUT9-16,P161-8,P169-16,AUX/CR}
/config/tape/gainL linf [-6.000,24.000,0.500] dB
/config/tape/gainR linf [-6.000,24.000,0.500] dB
/config/tape/autoplay enum {OFF,ON}
--------- channel [01..32] (channel id 0..31) ---------
/ch/[01..32]/config/name string [12]
/ch/[01..32]/config/icon int [1,74]
/ch/[01..32]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/ch/[01..32]/config/source int [0,64]
/ch/[01..32]/delay/on enum {OFF,ON}
/ch/[01..32]/delay/time linf [0.300,500.000,0.100] ms
/ch/[01..32]/preamp/trim linf [-12.000,12.000,0.250] (digital sources only) dB
/ch/[01..32]/preamp/invert enum {OFF,ON}
/ch/[01..32]/preamp/hpon enum {OFF,ON}
/ch/[01..32]/preamp/hpslope enum {12,18,24}
/ch/[01..32]/preamp/hpf logf [20.000,400.000,101] Hz
/ch/[01..32]/gate/on enum {OFF,ON}
/ch/[01..32]/gate/mode enum {GATE,DUCK}
/ch/[01..32]/gate/thr linf [-80.000,0.000,0.500] dB
/ch/[01..32]/gate/range linf [3.000,60.000,1.000] dB
/ch/[01..32]/gate/attack linf [0.000,120.000,1.000] ms
/ch/[01..32]/gate/hold logf [0.020,2000,101] ms
/ch/[01..32]/gate/release logf [5.000,4000.000,101] ms
/ch/[01..32]/gate/keysrc int [0,64]
/ch/[01..32]/gate/filter/on enum {OFF,ON}
/ch/[01..32]/gate/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/ch/[01..32]/gate/filter/f logf [20.000,20000,201] Hz
/ch/[01..32]/dyn/on enum {OFF,ON}
/ch/[01..32]/dyn/mode enum {COMP,EXP}
/ch/[01..32]/dyn/det enum {PEAK,RMS}
/ch/[01..32]/dyn/env enum {LIN,LOG}
/ch/[01..32]/dyn/thr linf [-80.000,0.000,0.500] dB
/ch/[01..32]/dyn/ratio enum {1.1,1.3,1.5,2.0,2.5,3.0,4.0,5.0,7.0,10,20,100}
/ch/[01..32]/dyn/knee linf [0.000,5.000,1.000]
/ch/[01..32]/dyn/mgain linf [0.000,24.000,0.500] dB
/ch/[01..32]/dyn/attack linf [0.000,120.000,1.000] ms
/ch/[01..32]/dyn/hold logf [0.020,2000,101] ms/ch/[01..32]/dyn/release logf [5.000,4000.000,101] ms
/ch/[01..32]/dyn/pos enum {PRE,POST}
/ch/[01..32]/dyn/keysrc int [0,64]
/ch/[01..32]/dyn/filter/on enum {OFF,ON}
/ch/[01..32]/dyn/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/ch/[01..32]/dyn/filter/f logf [20.000,20000,201] Hz
/ch/[01..32]/insert/on enum {OFF,ON}
/ch/[01..32]/insert/pos enum {PRE,POST}
/ch/[01..32]/insert/sel enum {OFF,FX1L,FX1R,FX2L,FX2R,FX3L,FX3R,FX4L,
FX4R,FX5L,FX5R,FX6L,FX6R,FX7L,FX7R,FX8L,
FX8R,AUX1,AUX2,AUX3,AUX4,AUX5,AUX6}
/ch/[01..32]/eq/on enum {OFF,ON}
/ch/[01..32]/eq/[1..4]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/ch/[01..32]/eq/[1..4]/f logf [20.000,20000,201] Hz
/ch/[01..32]/eq/[1..4]/g linf [-15.000,15.000,0.250] dB
/ch/[01..32]/eq/[1..4]/q logf [10.000,0.300,72]
/ch/[01..32]/mix/on enum {OFF,ON}
/ch/[01..32]/mix/fader level [0.0...1.0 (+10 dB), 1024] dB
/ch/[01..32]/mix/st enum {OFF,ON}
/ch/[01..32]/mix/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/mono enum {OFF,ON}
/ch/[01..32]/mix/mlevel level [0.0...1.0 (+10 dB), 161] dB
/ch/[01..32]/mix/[01..16]/on enum {OFF,ON}
/ch/[01..32]/mix/[01..16]/level level [0.0...1.0 (+10 dB), 161] dB
/ch/[01..32]/mix/01/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/01/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/03/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/03/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/05/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/05/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/07/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/07/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/09/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/09/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/11/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/11/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/13/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/13/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/mix/15/pan linf [-100.000,100.000,2.000]
/ch/[01..32]/mix/15/type enum {<-EQ,EQ->,PRE,POST,GRP}
/ch/[01..32]/grp/dca int [0,255] (bitmap)
/ch/[01..32]/grp/mute int [0,63] (bitmap)
--------- auxin [01..08] (channel id 32..39) ---------
/auxin/[01..08]/config/name string [12]
/auxin/[01..08]/config/icon int [1,74]
/auxin/[01..08]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}/auxin/[01..08]/config/source int [0,64]
/auxin/[01..08]/preamp/trim linf [-12.000,12.000,0.250] dB
/auxin/[01..08]/preamp/invert enum {OFF,ON}
/auxin/[01..08]/eq/on enum {OFF,ON}
/auxin/[01..08]/eq/[1..4]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/auxin/[01..08]/eq/[1..4]/f logf [20.000,20000,201] Hz
/auxin/[01..08]/eq/[1..4]/g linf [-15.000,15.000,0.250] dB
/auxin/[01..08]/eq/[1..4]/q logf [10.000,0.300,72]
/auxin/[01..08]/mix/on enum {OFF,ON}
/auxin/[01..08]/mix/fader level [0.0...1.0 (+10 dB), 1024]
/auxin/[01..08]/mix/st enum {OFF,ON}
/auxin/[01..08]/mix/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/mono enum {OFF,ON}
/auxin/[01..08]/mix/mlevel level [0.0...1.0 (+10 dB), 161]
/auxin/[01..08]/mix/[01..16]/on enum {OFF,ON}
/auxin/[01..08]/mix/[01..16]/level level [0.0...1.0 (+10 dB), 161]
/auxin/[01..08]/mix/01/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/01/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/03/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/03/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/05/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/05/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/07/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/07/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/09/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/09/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/11/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/11/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/13/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/13/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/mix/15/pan linf [-100.000,100.000,2.000]
/auxin/[01..08]/mix/15/type enum {<-EQ,EQ->,PRE,POST,GRP}
/auxin/[01..08]/grp/dca int [0,255] (bitmap)
/auxin/[01..08]/grp/mute int [0,63] (bitmap)
--------- fxrtn [01..08] (channel id 40..47) ---------
/fxrtn/[01..08]/config/name string [12]
/fxrtn/[01..08]/config/icon int [1,74]
/fxrtn/[01..08]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/fxrtn/[01..08]/mix/on enum {OFF,ON}
/fxrtn/[01..08]/mix/fader level [0.0...1.0 (+10 dB), 1024] dB
/fxrtn/[01..08]/mix/st enum {OFF,ON}
/fxrtn/[01..08]/mix/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/mono enum {OFF,ON}
/fxrtn/[01..08]/mix/mlevel level [0.0...1.0 (+10 dB), 161] dB
/fxrtn/[01..08]/mix/[01..16]/on enum {OFF,ON}
/fxrtn/[01..08]/mix/[01..16]/level level [0.0...1.0 (+10 dB), 161] dB/fxrtn/[01..08]/mix/01/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/01/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/03/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/03/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/05/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/05/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/07/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/07/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/09/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/09/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/11/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/11/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/13/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/13/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/mix/15/pan linf [-100.000,100.000,2.000]
/fxrtn/[01..08]/mix/15/type enum {<-EQ,EQ->,PRE,POST,GRP}
/fxrtn/[01..08]/grp/dca int [0,255] (bitmap)
/fxrtn/[01..08]/grp/mute int [0,63] (bitmap)
--------- bus [01..16] (channel id 48..63) ---------
/bus/[01..16]/config/name string [12]
/bus/[01..16]/config/icon int [1,74]
/bus/[01..16]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/bus/[01..16]/dyn/on enum {OFF,ON}
/bus/[01..16]/dyn/mode enum {COMP,EXP}
/bus/[01..16]/dyn/det enum {PEAK,RMS}
/bus/[01..16]/dyn/env enum {LIN,LOG}
/bus/[01..16]/dyn/thr linf [-80.000,0.000,0.500] dB
/bus/[01..16]/dyn/ratio enum {1.1,1.3,1.5,2.0,2.5,3.0,4.0,5.0,7.0,10,20,100}
/bus/[01..16]/dyn/knee linf [0.000,5.000,1.000]
/bus/[01..16]/dyn/mgain linf [0.000,24.000,0.500] dB
/bus/[01..16]/dyn/attack linf [0.000,120.000,1.000] ms
/bus/[01..16]/dyn/hold logf [0.020,2000,101] ms
/bus/[01..16]/dyn/release logf [5.000,4000.000,101] ms
/bus/[01..16]/dyn/pos enum {PRE,POST}
/bus/[01..16]/dyn/keysrc int [0,64]
/bus/[01..16]/dyn/filter/on enum {OFF,ON}
/bus/[01..16]/dyn/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/bus/[01..16]/dyn/filter/f logf [20.000,20000,201] Hz
/bus/[01..16]/insert/on enum {OFF,ON}
/bus/[01..16]/insert/pos enum {PRE,POST}
/bus/[01..16]/insert/sel enum {OFF,FX1L,FX1R,FX2L,FX2R,FX3L,FX3R,FX4L,
FX4R,FX5L,FX5R,FX6L,FX6R,FX7L,FX7R,FX8L,
FX8R,AUX1,AUX2,AUX3,AUX4,AUX5,AUX6}
/bus/[01..16]/eq/on enum {OFF,ON}
/bus/[01..16]/eq/[1..6]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/bus/[01..16]/eq/[1..6]/f logf [20.000,20000,201] Hz/bus/[01..16]/eq/[1..6]/g linf [-15.000,15.000,0.250] dB
/bus/[01..16]/eq/[1..6]/q logf [10.000,0.300,72]
/bus/[01..16]/mix/on enum {OFF,ON}
/bus/[01..16]/mix/fader level [0.0...1.0 (+10 dB), 1024] dB
/bus/[01..16]/mix/st enum {OFF,ON}
/bus/[01..16]/mix/pan linf [-100.000,100.000,2.000]
/bus/[01..16]/mix/mono enum {OFF,ON}
/bus/[01..16]/mix/mlevel level [0.0...1.0 (+10 dB), 161] dB
/bus/[01..16]/mix/[01..06]/on enum {OFF,ON}
/bus/[01..16]/mix/[01..06]/level level [0.0...1.0 (+10 dB), 161] dB
/bus/[01..16]/mix/01/pan linf [-100.000,100.000,2.000]
/bus/[01..16]/mix/03/pan linf [-100.000,100.000,2.000]
/bus/[01..16]/mix/05/pan linf [-100.000,100.000,2.000]
/bus/[01..16]/grp/dca int [0,255] (bitmap)
/bus/[01..16]/grp/mute int [0,63] (bitmap)
--------- mtx [01..06] (channel id 64..69) ---------
/mtx/[01..06]/config/name string [12]
/mtx/[01..06]/config/icon int [1,74]
/mtx/[01..06]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/mtx/[01..06]/dyn/on enum {OFF,ON}
/mtx/[01..06]/dyn/mode enum {COMP,EXP}
/mtx/[01..06]/dyn/det enum {PEAK,RMS}
/mtx/[01..06]/dyn/env enum {LIN,LOG}
/mtx/[01..06]/dyn/thr linf [-80.000,0.000,0.500] dB
/mtx/[01..06]/dyn/ratio enum {1.1,1.3,1.5,2.0,2.5,3.0,4.0,5.0,7.0,10,20,100}
/mtx/[01..06]/dyn/knee linf [0.000,5.000,1.000]
/mtx/[01..06]/dyn/mgain linf [0.000,24.000,0.500] dB
/mtx/[01..06]/dyn/attack linf [0.000,120.000,1.000] ms
/mtx/[01..06]/dyn/hold logf [0.020,2000,101] ms
/mtx/[01..06]/dyn/release logf [5.000,4000.000,101] ms
/mtx/[01..06]/dyn/pos enum {PRE,POST}
/mtx/[01..06]/dyn/filter/on enum {OFF,ON}
/mtx/[01..06]/dyn/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/mtx/[01..06]/dyn/filter/f logf [20.000,20000,201] Hz
/mtx/[01..06]/insert/on enum {OFF,ON}
/mtx/[01..06]/insert/pos enum {PRE,POST}
/mtx/[01..06]/insert/sel enum {OFF,FX1L,FX1R,FX2L,FX2R,FX3L,FX3R,FX4L,
FX4R,FX5L,FX5R,FX6L,FX6R,FX7L,FX7R,FX8L,
FX8R,AUX1,AUX2,AUX3,AUX4,AUX5,AUX6}
/mtx/[01..06]/eq/on enum {OFF,ON}
/mtx/[01..06]/eq/[1..6]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/mtx/[01..06]/eq/[1..6]/f logf [20.000,20000,201] Hz
/mtx/[01..06]/eq/[1..6]/g linf [-15.000,15.000,0.250] dB
/mtx/[01..06]/eq/[1..6]/q logf [10.000,0.300,72]
/mtx/[01..06]/mix/on enum {OFF,ON}
/mtx/[01..06]/mix/fader level [0.0...1.0 (+10 dB), 1024] dB--------- main stereo (channel id 70) ---------
/main/st/config/name string [12]
/main/st/config/icon int [1,74]
/main/st/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/main/st/dyn/on enum {OFF,ON}
/main/st/dyn/mode enum {COMP,EXP}
/main/st/dyn/det enum {PEAK,RMS}
/main/st/dyn/env enum {LIN,LOG}
/main/st/dyn/thr linf [-80.000,0.000,0.500] dB
/main/st/dyn/ratio enum {1.1,1.3,1.5,2.0,2.5,3.0,4.0,5.0,7.0,10,20,100}
/main/st/dyn/knee linf [0.000,5.000,1.000]
/main/st/dyn/mgain linf [0.000,24.000,0.500] dB
/main/st/dyn/attack linf [0.000,120.000,1.000] ms
/main/st/dyn/hold logf [0.020,2000,101] ms
/main/st/dyn/release logf [5.000,4000.000,101] ms
/main/st/dyn/pos enum {PRE,POST}
/main/st/dyn/filter/on enum {OFF,ON}
/main/st/dyn/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/main/st/dyn/filter/f logf [20.000,20000,201] Hz
/main/st/insert/on enum {OFF,ON}
/main/st/insert/pos enum {PRE,POST}
/main/st/insert/sel enum {OFF,FX1L,FX1R,FX2L,FX2R,FX3L,FX3R,FX4L,
FX4R,FX5L,FX5R,FX6L,FX6R,FX7L,FX7R,FX8L,
FX8R,AUX1,AUX2,AUX3,AUX4,AUX5,AUX6}
/main/st/eq/on enum {OFF,ON}
/main/st/eq/[1..6]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/main/st/eq/[1..6]/f logf [20.000,20000,201] Hz
/main/st/eq/[1..6]/g linf [-15.000,15.000,0.250] dB
/main/st/eq/[1..6]/q logf [10.000,0.300,-0.049]
/main/st/mix/on enum {OFF,ON}
/main/st/mix/fader level [0.0...1.0 (+10 dB), 1024] dB
/main/st/mix/pan linf [-100.000,100.000,2.000]
/main/st/mix/[01..06]/on enum {OFF,ON}
/main/st/mix/[01..06]/level level [0.0...1.0 (+10 dB), 161] dB
/main/st/mix/01/pan linf [-100.000,100.000,2.000]
/main/st/mix/03/pan linf [-100.000,100.000,2.000]
/main/st/mix/05/pan linf [-100.000,100.000,2.000]
--------- main mono (channel id 71) ---------
/main/m/config/name string [12]
/main/m/config/icon int [1,74]
/main/m/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
/main/m/dyn/on enum {OFF,ON}
/main/m/dyn/mode enum {COMP,EXP}
/main/m/dyn/det enum {PEAK,RMS}
/main/m/dyn/env enum {LIN,LOG}
/main/m/dyn/thr linf [-80.000,0.000,0.500] dB/main/m/dyn/ratio enum {1.1,1.3,1.5,2.0,2.5,3.0,4.0,5.0,7.0,10,20,100}
/main/m/dyn/knee linf [0.000,5.000,1.000]
/main/m/dyn/mgain linf [0.000,24.000,0.500] dB
/main/m/dyn/attack linf [0.000,120.000,1.000] ms
/main/m/dyn/hold logf [0.020,2000,101] ms
/main/m/dyn/release logf [5.000,4000.000,101] ms
/main/m/dyn/pos enum {PRE,POST}
/main/m/dyn/filter/on enum {OFF,ON}
/main/m/dyn/filter/type enum {LC6,LC12,HC6,HC12,1.0,2.0,3.0,5.0,10.0}
/main/m/dyn/filter/f logf [20.000,20000,201] Hz
/main/m/insert/on enum {OFF,ON}
/main/m/insert/pos enum {PRE,POST}
/main/m/insert/sel enum {OFF,FX1L,FX1R,FX2L,FX2R,FX3L,FX3R,FX4L,
FX4R,FX5L,FX5R,FX6L,FX6R,FX7L,FX7R,FX8L,
FX8R,AUX1,AUX2,AUX3,AUX4,AUX5,AUX6}
/main/m/eq/on enum {OFF,ON}
/main/m/eq/[1..6]/type enum {LCut,LShv,PEQ,VEQ,HShv,HCut}
/main/m/eq/[1..6]/f logf [20.000,20000,201] Hz
/main/m/eq/[1..6]/g linf [-15.000,15.000,0.250] dB
/main/m/eq/[1..6]/q logf [10.000,0.300,72]
/main/m/mix/on enum {OFF,ON}
/main/m/mix/fader level [0.0...1.0 (+10 dB), 1024] dB
/main/m/mix/[01..06]/on enum {OFF,ON}
/main/m/mix/[01..06]/level level [0.0...1.0 (+10 dB), 161] dB
/main/m/mix/01/pan linf [-100.000,100.000,2.000]
/main/m/mix/03/pan linf [-100.000,100.000,2.000]
/main/m/mix/05/pan linf [-100.000,100.000,2.000]
--------- dca groups (no channel id!) ---------
/dca/[1..8]/on enum {OFF,ON}
/dca/[1..8]/fader level [0.0...1.0 (+10 dB), 1024] dB
/dca/[1..8]/config/name string [12]
/dca/[1..8]/config/icon int [1,74]
/dca/[1..8]/config/color enum {OFF,RD,GN,YE,BL,MG,CY,WH}
--------- effects fx [1..4] ---------
/fx/[1..4]/type enum {HALL,PLAT,VREV,VRM,AMBI,GATE,RVRS,DL
Y,3TAP,CRS,FLNG,PHAS,FILT,ROTA,PAN,D/R
V,CR/R,FL/R,D/CR,D/FL,GEQ2,GEQ,TEQ2,TE
Q,WAVD,LIM,ENH2,ENH,EXC2,EXC,IMG,AM
P2,AMP,DRV2,DRV,PIT2,PIT}
/fx/[1..4]/source/l enum {INS,MIX1,MIX2,MIX3,MIX4,MIX5,MIX6,MIX
7,MIX8,MIX9,MIX10,MIX11,MIX12,MIX13,
MIX14,MIX15,MIX16}
/fx/[1..4]/source/r enum {INS,MIX1,MIX2,MIX3,MIX4,MIX5,MIX6,MIX
7,MIX8,MIX9,MIX10,MIX11,MIX12,MIX13,
MIX14,MIX15,MIX16}/fx/[1..4]/par/[01..64] linf/logf (depending on selected effect type)
--------- effects fx [5..8] ---------
/fx/[5..8]/type enum {GEQ2,GEQ,TEQ2,TEQ,WAVD,LIM,ENH2,EN
H,EXC2,EXC,IMG,AMP2,AMP,DRV2,DRV,PH
AS,FILT,PAN}
/fx/[5..8]/par/[01..64] linf/logf (depending on selected effect type)
--------- outputs main [01..16] ---------
/outputs/main/[01..16]/src int [0,76]
/outputs/main/[01..16]/pos enum {<-EQ,EQ->,PRE,POST}
/outputs/main/[01..16]/delay/on enum {OFF,ON}
/outputs/main/[01..16]/delay/time
e
linf [0.300,500.000,0.100] ms
--------- outputs aux [01..06] ---------
/outputs/aux/[01..06]/src int [0,76]
/outputs/aux/[01..06]/pos enum {<-EQ,EQ->,PRE,POST}
--------- outputs P16 [01..16] ---------
/outputs/p16/[01..16]/src int [0,76]
/outputs/p16/[01..16]/pos enum {<-EQ,EQ->,PRE,POST}
--------- outputs AES [01..02] ---------
/outputs/aes/[01..02]/src int [0,76]
/outputs/aes/[01..02]/pos enum {<-EQ,EQ->,PRE,POST}
--------- outputs REC [01..02] ---------
/outputs/rec/[01..02]/src int [0,76]
/outputs/rec/[01..02]/pos enum {<-EQ,EQ->,PRE,POST}
--------- headamps [000..127] ---------
/headamp/[000..127]/gain linf [-12.000,60.000,0.500] dB
/headamp/[000..127]/phantom enum {OFF,ON}
000..031: local XLR inputs
032..079: AES50 port A connected devices
080..127: AES50 port B connected devices

/-prefs/confirm_general [0]
/-prefs/confirm_overwrite [0]
/-prefs/confirm_sceneload [0]
/-prefs/viewrtn [0]
/-prefs/selfollowsbank [1]
/-prefs/scene_advance [1]
/-prefs/safe_masterlevels [0]
/-prefs/stagelock [1]
/-prefs/ledbright [0.9444444179534912]
/-prefs/bright [0.7222222089767456]
/-prefs/lcdcont [0.47999998927116394]
/-stat/lock [1]
"""

def get_settings():
    """This will generate a list with osc-paths to all settings from
    settings_from_doc
    All [01..32] etc will be expanded.
    
    This is all settings that need to be set for audiopath of control to be set to known state.
    """
    setting_lines = []
    for line in settings_from_doc.splitlines():
        if line.startswith("/"):
            setting_lines.append(line.split()[0])
    settings = []
    for setting_line in setting_lines:
        indexes = []
        template = ""
        for part in setting_line.strip().split("/"):
            if len(part):
                if part.startswith("["):
                    first, last = part.split("..")
                    n_digits = len(first[1:])
                    first = int(first[1:])
                    last = int(last[:-1])
                    template += "/%0{n_digits}d".format(n_digits = n_digits)
                    indexes.append(range(first, last+1))
                else:
                    template += "/"+part
        if not indexes:
            settings.append(template)
        else:
            for current in itertools.product(*indexes):
                settings.append(template % current)
    return settings
                
if __name__=="__main__":
    settings = get_settings()
    
    for setting in settings:
        print setting
    print len(settings)