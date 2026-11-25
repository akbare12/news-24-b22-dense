import os, math
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f_kick=F(SANSB,11); f_mast=F(SERIF,30); f_sub=F(SERIF,12); f_reg=F(SANSB,10); f_utc=F(SANSB,9); f_num=F(SERIF,20); f_numl=F(SANSB,8); f_hk=F(SANSB,9); f_hh=F(SERIF,13); f_hd=F(SANS,10); f_ck=F(SANSB,8); f_ch=F(SANSB,10); f_cd=F(SANS,9); f_chip=F(SANSB,7); f_map=F(SANSB,8); f_al=F(SANS,9); f_dc=F(SANSB,10); f_dct=F(SANS,9); f_ft=F(SANS,8)
RED=(178,34,34); NAVY=(18,38,66); CREAM=(252,248,238); INK=(20,20,20); GREY=(90,90,90); LGREY=(225,220,210); GREEN=(34,120,60); BLUE=(30,80,160); ORANGE=(200,100,0)
CHIPCOL={"CONFIRMED":GREEN,"OFFICIAL":BLUE,"REPORTED":(80,90,110),"CLAIM":ORANGE}
def wrap(d,t,font,mw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        s=(cur+" "+w).strip()
        if d.textlength(s,font=font)<=mw: cur=s
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def txt(d,x,y,t,font,fill=INK,anchor="la"):
    d.text((x,y),t,font=font,fill=fill,anchor=anchor)
def chip(d,x,y,label):
    c=CHIPCOL.get(label,(100,100,100)); w=d.textlength(label,font=f_chip)+10
    d.rounded_rectangle([x,y,x+w,y+12],radius=3,fill=c); d.text((x+5,y+2),label,font=f_chip,fill="white"); return w
def scene(im,x,y,w,h,kind):
    tmp=Image.new("RGB",(w,h),(210,225,235)); d=ImageDraw.Draw(tmp); ox,oy=x,y; x=0; y=0
    d.rectangle([x,y,x+w,y+h],fill=(210,225,235),outline=NAVY,width=1)
    if kind=="riyadh":
        d.rectangle([x,y+h*0.55,x+w,y+h],fill=(40,50,80)); d.rectangle([x,y,x+w,y+h*0.55],fill=(25,30,60))
        for i,(bx,bw,bh) in enumerate([(8,22,70),(34,18,95),(56,26,60),(86,20,80),(110,24,55),(138,18,88),(162,22,62),(188,20,75),(212,24,58),(240,18,85),(264,22,60)]):
            d.rectangle([x+bx,y+h-bh,x+bx+bw,y+h],fill=(70,80,120))
        d.rectangle([x+128,y+8,x+142,y+h-20],fill=(200,170,90)); d.polygon([(x+128,y+8),(x+142,y+8),(x+135,y-2)],fill=(230,200,110))
        d.ellipse([x+210,y+12,x+226,y+28],fill=(255,220,120)); d.polygon([(x+150,y+30),(x+165,y+44),(x+138,y+44)],fill=(255,120,60)); d.ellipse([x+140,y+34,x+168,y+58],fill=(255,140,60))
        for sx,sy in [(30,20),(70,14),(200,18),(250,30)]: d.ellipse([x+sx,y+sy,x+sx+3,y+sy+3],fill="white")
    elif kind=="shanghai":
        d.rectangle([x,y,x+w,y+h],fill=(150,40,40)); d.rectangle([x,y+h*0.6,x+w,y+h],fill=(90,20,20))
        d.rectangle([x+20,y+22,x+w-20,y+h-18],fill=(245,235,210),outline=(120,90,40),width=2)
        d.rectangle([x+34,y+34,x+w-34,y+52],fill=(120,30,30)); d.text((x+w//2,y+36),"PARTY OFFICE",font=f_chip,fill="white",anchor="ma")
        d.rectangle([x+60,y+62,x+110,y+92],fill="white",outline=NAVY); d.rectangle([x+170,y+62,x+220,y+92],fill="white",outline=NAVY)
        for lx in (70,180):
            for i in range(4): d.line([x+lx,y+66+i*6,x+lx+40,y+66+i*6],fill=GREY,width=1)
        d.polygon([(x+150,y+58),(x+160,y+72),(x+140,y+72)],fill=RED)
    elif kind=="huawei":
        d.rectangle([x,y,x+w,y+h],fill=(60,70,110)); d.rectangle([x,y+h*0.55,x+w,y+h],fill=(180,180,170))
        d.rectangle([x+18,y+18,x+110,y+52],fill=(240,240,235)); d.text((x+64,y+26),"COURT",font=f_hk,fill=NAVY,anchor="ma")
        for cx in (30,60,90,120,150,180,210,240,270):
            d.rectangle([x+cx,y+58,x+cx+14,y+h-6],fill=(220,225,235),outline=NAVY)
        d.ellipse([x+128,y+62,x+172,y+88],fill=(200,30,30)); d.text((x+150,y+66),"H",font=F(SERIF,16),fill="white",anchor="ma")
        d.rectangle([x+200,y+30,x+206,y+78],fill=(150,110,50)); d.rectangle([x+180,y+28,x+226,y+36],fill=(150,110,50))
    elif kind=="ukraine":
        d.rectangle([x,y,x+w,y+h],fill=(20,25,55)); d.rectangle([x,y+h*0.7,x+w,y+h],fill=(50,45,40))
        for sx,sy in [(20,10),(60,20),(110,8),(150,18),(200,12),(250,22)]: d.ellipse([x+sx,y+sy,x+sx+3,y+sy+3],fill="white")
        for dx,dy in [(40,30),(120,22),(200,34),(260,26)]:
            d.ellipse([x+dx,y+dy,x+dx+10,y+dy+10],fill=(255,180,60)); d.line([x+dx+5,y+dy+10,x+dx+5,y+dy+22],fill=(255,120,40),width=3)
        d.rectangle([x+30,y+h-30,x+90,y+h],fill=(90,80,70)); d.rectangle([x+180,y+h-40,x+250,y+h],fill=(80,75,65))
    elif kind=="senegal":
        d.rectangle([x,y,x+w,y+h],fill=(20,110,60)); d.ellipse([x+w//2-28,y+8,x+w//2+28,y+52],fill=(230,190,60),outline="white",width=2)
        d.polygon([(x+w//2-14,y+14),(x+w//2-6,y+32),(x+w//2+4,y+32),(x+w//2+12,y+16)],fill=(240,200,70))
        d.rectangle([x+20,y+h-22,x+w-20,y+h-12],fill=(200,30,30)); d.rectangle([x+20,y+h-12,x+w-20,y+h-6],fill=(240,200,40))
    elif kind=="hormuz":
        d.rectangle([x,y,x+w,y+h],fill=(40,110,160)); d.rectangle([x,y+h*0.62,x+w,y+h],fill=(20,60,110))
        d.rectangle([x+30,y+34,x+210,y+58],fill=(180,50,40)); d.rectangle([x+40,y+22,x+120,y+34],fill=(220,220,210))
        for cx in (50,80,110,140,170,200): d.rectangle([x+cx,y+40,x+cx+18,y+52],fill=(240,240,230))
        d.polygon([(x+230,y+30),(x+258,y+52),(x+230,y+52)],fill=(90,90,90)); d.ellipse([x+235,y+18,x+245,y+28],fill=(255,120,40))
    elif kind=="dow":
        d.rectangle([x,y,x+w,y+h],fill=(245,245,240)); d.line([x+10,y+h-18,x+60,y+h-40,x+120,y+h-30,x+180,y+h-55,x+240,y+h-58,x+280,y+h-70],fill=GREEN,width=3)
        d.line([x+10,y+30,x+w-10,y+30],fill=RED,width=2); d.text((x+10,y+2),"50,000",font=F(SERIF,12),fill=RED)
        for bx in (20,50,80,110,140,170,200,230,260): d.rectangle([x+bx,y+h-14,x+bx+16,y+h-6],fill=NAVY)
    elif kind=="redmond":
        d.rectangle([x,y,x+w,y+h],fill=(120,30,30)); d.rectangle([x+8,y+6,x+w//2-4,y+22],fill=(240,240,235)); d.text((x+w//4,y+10),"CODE RED",font=f_hk,fill=RED,anchor="ma")
        d.rectangle([x+w//2+4,y+6,x+w-8,y+22],fill=(30,30,40)); d.text((x+3*w//4,y+10),"11,000+ MSGS",font=f_chip,fill=(255,200,80),anchor="ma")
        bw=w//6
        for i in range(6): d.rectangle([x+i*bw+2,y+h-16,x+(i+1)*bw-2,y+h-4],fill=(60,70,100),outline=(200,200,200))
    elif kind=="helicopter":
        d.rectangle([x,y,x+w,y+h],fill=(140,170,200)); d.polygon([(x,y+h),(x+w,y+h),(x+w,y+h-40),(x,y+h-20)],fill=(90,110,80))
        d.ellipse([x+110,y+34,x+190,y+66],fill=(80,90,80)); d.rectangle([x+190,y+44,x+260,y+54],fill=(80,90,80)); d.rectangle([x+60,y+30,x+230,y+38],fill=(60,60,60))
        d.polygon([(x+250,y+20),(x+270,y+50),(x+240,y+50)],fill=(100,100,100))
    elif kind=="cartagena":
        d.rectangle([x,y,x+w,y+h],fill=(230,220,190)); d.rectangle([x+16,y+14,x+w-16,y+44],fill=(200,40,40)); d.text((x+w//2,y+22),"SUPERMARKET",font=f_hk,fill="white",anchor="ma")
        d.rectangle([x+30,y+h-14,x+120,y+h-4],fill=(180,180,170)); d.rectangle([x+160,y+h-14,x+250,y+h-4],fill=(160,160,150))
        for i in range(5): d.ellipse([x+40+i*14,y+h-12,x+48+i*14,y+h-6],fill=NAVY)
    elif kind=="aden":
        d.rectangle([x,y,x+w,y+h],fill=(220,190,130)); d.rectangle([x,y+h*0.6,x+w,y+h],fill=(180,150,90))
        d.polygon([(x+40,y+h-10),(x+90,y+20),(x+140,y+h-10)],fill=(140,120,80)); d.polygon([(x+150,y+h-10),(x+210,y+30),(x+270,y+h-10)],fill=(120,100,70))
        d.rectangle([x+120,y+30,x+180,y+52],fill=(60,60,60)); d.text((x+150,y+34),"60 KM",font=f_hk,fill="white",anchor="ma")
    elif kind=="yemen":
        d.rectangle([x,y,x+w,y+h],fill=(200,170,120)); d.rectangle([x+30,y+40,x+130,y+66],fill=(240,240,230)); d.rectangle([x+150,y+40,x+250,y+66],fill=(200,60,40))
        d.ellipse([x+120,y+18,x+150,y+44],fill=(255,140,40)); d.polygon([(x+135,y+44),(x+145,y+62),(x+125,y+62)],fill=(255,120,30))
        d.line([x+20,y+h-12,x+w-20,y+h-12],fill=(80,70,50),width=4)
    elif kind=="space":
        d.rectangle([x,y,x+w,y+h],fill=(10,15,45))
        for sx,sy in [(20,12),(70,24),(130,10),(200,20),(260,14),(40,50),(180,55)]: d.ellipse([x+sx,y+sy,x+sx+3,y+sy+3],fill="white")
        d.rectangle([x+130,y+18,x+150,y+72],fill=(230,230,230)); d.polygon([(x+130,y+18),(x+150,y+18),(x+140,y+6)],fill=RED)
        d.polygon([(x+150,y+60),(x+178,y+40),(x+178,y+80)],fill=(150,180,220)); d.ellipse([x+175,y+48,x+195,y+68],fill=(200,200,220),outline=(120,140,180))
        d.ellipse([x+40,y+70,x+70,y+88],fill=(100,140,200))
    im.paste(tmp,(ox,oy))

CONT=[ [(-168,66),(-155,58),(-140,60),(-130,55),(-125,49),(-125,40),(-120,34),(-114,29),(-108,24),(-100,20),(-95,18),(-90,15),(-85,12),(-80,9),(-78,7),(-80,12),(-85,16),(-90,20),(-97,26),(-93,30),(-85,30),(-80,32),(-75,35),(-70,42),(-65,45),(-60,47),(-55,52),(-60,55),(-65,60),(-70,62),(-80,66),(-90,68),(-100,68),(-115,68),(-130,70),(-145,70),(-160,70)], [(-78,7),(-75,10),(-72,12),(-65,10),(-60,8),(-55,5),(-50,0),(-45,-5),(-38,-8),(-35,-10),(-40,-20),(-48,-25),(-55,-35),(-65,-40),(-70,-50),(-73,-53),(-70,-45),(-73,-35),(-72,-20),(-70,-18),(-75,-15),(-80,-5),(-81,0),(-80,5)], [(-10,36),(-9,43),(-2,48),(-1,50),(2,51),(5,53),(8,57),(10,59),(18,56),(21,55),(24,59),(28,60),(30,62),(25,65),(20,70),(25,71),(30,70),(35,68),(40,66),(45,64),(50,60),(48,55),(45,50),(40,47),(38,45),(35,42),(30,41),(28,45),(25,42),(22,40),(20,42),(15,44),(12,44),(8,44),(3,43),(0,40),(-2,37),(-6,36)], [(-17,15),(-16,20),(-15,25),(-10,30),(-5,35),(0,36),(10,37),(12,34),(15,32),(20,32),(25,31),(30,31),(32,28),(35,28),(38,22),(40,18),(43,12),(46,11),(51,12),(55,17),(58,20),(57,25),(55,26),(52,26),(50,28),(48,30),(44,29),(42,25),(40,20),(38,15),(35,12),(32,15),(30,18),(28,22),(25,28),(22,32),(20,35),(18,34),(15,32),(12,30),(10,28),(8,25),(5,20),(2,15),(0,10),(-5,5),(-8,4),(-12,8),(-15,10)], [(60,68),(75,72),(90,75),(105,77),(120,73),(135,71),(150,70),(160,69),(170,66),(178,65),(170,60),(162,56),(158,52),(155,50),(150,45),(142,40),(138,35),(132,33),(127,30),(124,22),(120,18),(115,22),(110,20),(108,12),(105,9),(103,2),(100,6),(98,10),(96,16),(92,21),(89,22),(86,20),(83,17),(80,13),(77,8),(75,12),(72,20),(68,23),(65,25),(61,25),(57,26),(56,26),(58,22),(55,17),(52,14),(48,14),(44,12),(42,15),(40,20),(38,25),(36,29),(34,29),(36,36),(38,38),(40,42),(43,45),(46,48),(48,52),(50,55),(52,58),(55,62),(58,66)], [(113,22),(114,28),(115,33),(118,35),(122,34),(125,32),(129,32),(132,32),(135,35),(138,35),(140,38),(142,39),(145,38),(148,37),(150,37),(153,32),(153,27),(150,23),(146,19),(142,15),(142,11),(140,14),(137,12),(135,12),(132,11),(130,13),(126,14),(122,17),(118,20),(114,22)], [(95,5),(98,4),(100,0),(102,-2),(104,-4),(106,-6),(108,-7),(110,-7),(112,-7),(114,-8),(116,-9),(118,-9),(120,-10),(119,-8),(117,-6),(115,-4),(113,-2),(110,0),(108,2),(105,4),(102,5),(100,6),(97,5)], [(109,1),(111,2),(114,4),(117,6),(118,2),(117,-2),(115,-3),(112,-3),(110,-1)], [(131,-1),(134,-3),(137,-4),(140,-5),(143,-7),(146,-8),(148,-9),(150,-10),(147,-9),(144,-8),(141,-6),(138,-5),(135,-4),(132,-2)] ]
def draw_map(d,x,y,w,h):
    d.rectangle([x,y,x+w,y+h],fill=(190,215,235),outline=NAVY,width=1)
    def px(lon,lat): return x+(lon+180)/360*w, y+(90-lat)/150*h
    for poly in CONT:
        pts=[px(lon,lat) for lon,lat in poly]
        d.polygon(pts,fill=(170,200,140),outline=(90,120,70))
    d.text((x+8,y+6),"WORLD MAP",font=f_map,fill=NAVY)
    pins=[(1,24.7,46.7,"RIYADH"),(2,31.2,121.5,"SHANGHAI"),(3,40.7,-74.0,"NEW YORK"),(4,47.8,35.2,"ZAPORIZHZHIA"),(5,14.7,-17.4,"DAKAR"),(6,26.6,56.3,"HORMUZ"),(7,40.7,-74.0,"NEW YORK"),(8,47.7,-122.1,"REDMOND"),(9,39.8,30.5,"ESKISEHIR"),(10,10.4,-75.5,"CARTAGENA"),(11,12.8,45.0,"ADEN"),(12,13.0,44.9,"LAHJ"),(13,39.8,98.5,"JIUQUAN")]
    off={3:(0,0),7:(16,-14),11:(0,0),12:(18,12),1:(0,0),6:(0,0)}
    for n,lat,lon,name in pins:
        cx,cy=px(lon,lat); ox,oy=off.get(n,(0,0))
        if ox or oy:
            d.line([cx,cy,cx+ox,cy+oy],fill=INK,width=1)
        px_,py_=cx+ox,cy+oy
        d.ellipse([px_-8,py_-8,px_+8,py_+8],fill=RED,outline="white",width=1); d.text((px_,py_),str(n),font=f_chip,fill="white",anchor="mm")
        if n in (1,2,3,8,13):
            if n==1: d.text((px_-10,py_-5),name,font=f_map,fill=INK,anchor="ra")
            else: d.text((px_+10,py_-5),name,font=f_map,fill=INK)
    return
HERO=[("riyadh","1 RIYADH · MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. At least 11 people were hurt: 2 Saudis, 2 Indians, 3 Nepalese and 4 Egyptians. (Saudi officials · AP)"),("shanghai","2 SHANGHAI · ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is under investigation for serious violations, the fourth Politburo member to fall this year in the biggest shake-up of the Party elite. (CCDI)"),("huawei","3 NEW YORK · US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering; sentencing is in Sep 2027 and Huawei will appeal. (US court · Reuters)")]
CARDS=[("ukraine","4 ZAPORIZHZHIA · EUROPE","REPORTED","Russian attacks kill 9 across Ukraine in a day","Russia fired 96 drones; 73 were shot down. Nine were killed and 81 wounded. (Ukraine officials)"),("senegal","5 CAS · AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","CAS returned the Africa Cup to Senegal. Morocco forfeited 3-0, making the final 1-0 to Senegal. (CAS)"),("hormuz","6 HORMUZ · MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship in Hormuz at 18:58 UTC, disabling navigation. (UKMTO · wires)"),("dow","7 NEW YORK · MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first finish above 50,000. The Nasdaq fell 1.5%. (Market close)"),("redmond","8 REDMOND · TECH","REPORTED","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage on 12-13 Nov, Microsoft set a one-hour global recovery target. (Reuters)"),("helicopter","9 ESKISEHIR · EUROPE","REPORTED","Turkish military helicopter crash kills 5","A Turkish military AS-532 helicopter crashed in Eskisehir, killing all five people on board. (Turkish officials · 19:52 UTC)"),("cartagena","10 CARTAGENA · AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","Gunmen held 25 hostages in a Cartagena supermarket; five elderly women were freed. (Colombian officials)"),("aden","11 ADEN · MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden, Yemen, in their latest push south. (Wires · 16:51 UTC)"),("yemen","12 LAHJ · MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes in Wadi Maabaq, Lahj, killed or left missing 25 people and wounded six. (Yemeni officials)"),("space","13 JIUQUAN · SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","Shenzhou-24 crew: Tang Hongbo, Wu Yi, Muhammad Zeeshan Ali — the first foreigner for Tiangong. (CMSA)")]
ALSO=[("Ankara","Haftar visits Turkey for the first time. (13:45 UTC)"),("London","UK sanctions Houthis + 4 officials. (12:55 UTC)"),("Villavicencio","Car bomb injures 23, Monday night. (11:45 UTC)"),("Gaza","Israel kills Hamas security chief + 6. (11:40 UTC)"),("Baghdad","Iraq orders control of Kurdish oilfields. (11:19 UTC)"),("Gaza","Meningitis alert: 272 cases in Oct, 15 dead. (10:10 UTC)"),("DR Congo","Missing Cessna 208; rebels claim shootdown. (08:35 UTC)"),("Hanoi","Hot-pot blast kills at least 6, injures 10. (08:16 UTC)"),("Gulf of Finland","Ukraine hits Sparta II; 16 evacuated. (08:14 UTC)"),("Kuala Lumpur","Malaysia to return migrants to Myanmar. (05:54 UTC)"),("Ulleungdo","S. Korea shelter order as jets enter ADIZ. (04:14 UTC)"),("Dhaka","Hasina plans return on 16 Dec. (03:50 UTC)"),("The Hague","14 nations endorse ICJ Myanmar ruling. (03:00 UTC)"),("Jakarta","Indonesia nominates 2 VP candidates. (02:38 UTC)"),("Beijing","China sentences Ma to death for spying. (02:37 UTC)"),("Brussels","NATO vows defence against space threat. (02:15 UTC)"),("Mexico City","US drone aided El Chapo capture; Mexico to try him."),("San Salvador","Bukele names 3 soldiers killed in Haiti. (01:06 UTC)"),("Ottawa","Pentagon rebukes Canada: only 41.9% of air fleet ready."),("Washington","US adds Megaspeed to trade blacklist. (00:52 UTC)"),("Kyiv","Zelensky urges Ukraine/Russia/US/Europe talks. (00:30 UTC)"),("Ras Al Khaimah","UAE bus-truck crash kills 13; 14 hurt."),("London","England record 5,258 heat deaths, summer 2026. (UKHSA)"),("Kourou","Ariane 6 lofts 36 Amazon satellites. (11:14 UTC)"),("Cikande","Factory-fire toll rises to 26. (Fire began Sat 21 Nov)")]
def main():
    im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,10],fill=RED)
    txt(d,12,16,"THE WORLD ON ONE DAY",f_kick,RED); txt(d,W-12,16,"38 STORIES · 6 REGIONS · 13 FIELDS",f_kick,INK,anchor="ra")
    txt(d,W//2,32,"Tuesday 24 November 2026",f_mast,INK,anchor="ma")
    txt(d,W//2,64,"Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12",f_sub,RED,anchor="ma")
    regs=[("Europe",9,(30,80,160)),("Middle East",8,(178,34,34)),("Asia",8,(200,120,0)),("Africa",2,(34,120,60)),("Americas",7,(90,60,140)),("World/Space",4,(20,90,110))]
    x=12; tot=sum(v for _,v,_ in regs)
    for name,v,c in regs:
        w=int((W-24)*v/tot); d.rectangle([x,82,x+w-2,98],fill=c); txt(d,x+w//2,84,f"{name} {v}",f_reg,"white",anchor="ma"); x+=w
    d.rectangle([12,104,W-12,132],fill=(235,230,215),outline=LGREY)
    txt(d,16,106,"THE DAY IN UTC",f_kick,RED)
    for i,(t,s) in enumerate([("02:15","NATO vows space defence"),("08:16","Hanoi blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]):
        xx=16+i*144; txt(d,xx,118,t,f_utc,RED); txt(d,xx,127,s,f_utc,INK)
    d.rectangle([12,138,W-12,172],fill="white",outline=LGREY)
    txt(d,16,140,"THE DAY IN NUMBERS",f_kick,RED)
    for i,(n,l) in enumerate([("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed/missing in Yemen"),("26","Cikande fire toll")]):
        xx=230+i*132; txt(d,xx,140,n,f_num,INK,anchor="ma"); txt(d,xx,162,l,f_numl,GREY,anchor="ma")
    # heroes
    hw=(W-24-16)//3; hy=176
    for i,(kind,kick,ch,head,deck) in enumerate(HERO):
        x=12+i*(hw+8); scene(im,x,hy,hw,86,kind); txt(d,x,hy+90,kick,f_hk,RED); chip(d,x+hw-62,hy+88,ch)
        for j,ln in enumerate(wrap(d,head,f_hh,hw)): txt(d,x,hy+104+j*15,ln,f_hh,INK)
        for j,ln in enumerate(wrap(d,deck,f_hd,hw)[:4]): txt(d,x,hy+136+j*12,ln,f_hd,GREY)
    # cards 5+5
    cw=(W-24-32)//5; cy=366
    for i,(kind,kick,ch,head,deck) in enumerate(CARDS):
        r,c=i//5,i%5; x=12+c*(cw+8); y=cy+r*112; scene(im,x,y,cw,44,kind); txt(d,x,y+48,kick,f_ck,RED); chip(d,x+cw-52,y+47,ch)
        for j,ln in enumerate(wrap(d,head,f_ch,cw)[:2]): txt(d,x,y+62+j*11,ln,f_ch,INK)
        for j,ln in enumerate(wrap(d,deck,f_cd,cw)[:3]): txt(d,x,y+86+j*11,ln,f_cd,GREY)
    # map
    my=cy+224+6; draw_map(d,12,my,W-24,168)
    txt(d,12,my+172,"Pins 1-13 = stories 1-13. Redmond is on the US west coast; pins 3 and 7 share New York (offset).",f_ft,GREY)
    # ALSO
    ay=my+186; txt(d,12,ay,"ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES",f_kick,RED)
    colw=(W-24-16)//3
    for i,(city,head) in enumerate(ALSO):
        col=i//9; row=i%9; x=12+col*(colw+8); y=ay+18+row*14
        txt(d,x,y,f"{14+i}. {city}: {head}",f_al,INK)
    # DATE CHECK
    dy=ay+18+9*14+6; d.rectangle([12,dy,W-12,dy+66],fill=(255,235,235),outline=RED,width=1)
    txt(d,16,dy+3,"DATE CHECK",f_dc,RED); yy=dy+18
    for ln in wrap(d,"Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.",f_dct,W-40): txt(d,16,yy,ln,f_dct,INK); yy+=12
    for ln in wrap(d,"LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) · Huang returns as Nvidia CEO (Mon 23 Nov) · EU sanctions package 22 (Mon 23 Nov) · COP31 ends no deal (Sun 22 Nov) · Merkury sunk (Sat 22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande fire began (Sat 21 Nov).",f_dct,W-40): txt(d,16,yy,ln,f_dct,INK); yy+=12
    for ln in wrap(d,"NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR VP vote (11 Dec) · Huawei sentencing (Sep 2027) · Hasina return (16 Dec).",f_dct,W-40): txt(d,16,yy,ln,f_dct,INK); yy+=12
    txt(d,12,dy+72,"Sources: dailysummaryof.com/world/2026-11-24 · Reuters · AP · UKMTO · CAS · CMSA · CCDI. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim. Scenes are drawn illustrations, not photographs.",f_ft,GREY)
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out)
if __name__=="__main__": main()
