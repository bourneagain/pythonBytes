import sys
class Solution:
    def reverseWords(self, s):
        str=[]
        b=s.strip().split(' ')
        for i in range(len(b)-1,-1,-1):
            str.append(b[i].strip());
        return ' '.join(str) 

s=Solution();
print ":"+s.reverseWords("    a b ")+":";
s.reverseWords("eqfeabrm.!zibb'lf.vtyu,fa jbxiw,anv'cktr?fcmacynh?zy,dzzvqi,retp','uqn!ftf!ko!tmnibwhrgaqyhqhatvmihozvv!noahf?g?kxpz wzpzgnrna,,z c.kcm ld ngp?qlo!euhh!n ho!owonpwymyixpket!hs!!jmgjuwqu kj?fmdouwauvpu,?f'kvqqw'lpjvg'ochva gddqos,st.ta,vc fyrkvd'gdl.wn,crfv?ek,jcwepm.k.xrwv.jgwb?bg rfxrupfao,dxiafhbdblksqbuajubuvguhfaax?nhi'qtg!b?'mxqep wcoyvs?mdi,vtuumkepghdxz,v!w!!txiuk,fdwl.!lbpbbels.!lz'mmn jti.d'b'rvdlqfnoacvnfpkfcyoczuxzkj!oha.h'otbetmfegtpciqyjtln'jgff!kn,g,qqrbzwaavlup,?hse!fc.!ni,zm iuecqv?fqri!cllyiqjeob?mykswsfhgpyxb?vg.a,?ikhk,jpoipx.caoxw'supv' wqmacknyuf!jx,chb,rzhuwlhrncen w,bd?xnebc!hknje?jhato.saai'o.j?vsw!ujxhdb!i??zsbhvr.d.qpr.vruvs',,btlc.tdauge o waa,ikd?o?d.rwticnwyxyykslj?gbkunyxskbiweo ,!zqm.vodprtiqsiggfcbt!gzfnwczu?zp!gip!.,p'vxnom.giovwjov.oge!yuojgxplsblfyxenz'bln'xy.yvcmiomb mrjt?ocbtr,nzmkcdrnutppisnpclwm?mj!wqmcjhpb!kmiz qp!rpv'wqpphxirf. j,tndbf,jmfhhyw',kjqlbrxctp'tcqrtoo,xwxeibn'ldfmkfktofe'dosxhggtvnhouqf cyol?s'?'diqtnugnsyo ?uqlpgmxg?'w xortchgtrixvsnsqkx?al' b sef? b,fgrrqxvwpfct.a?efug'lbu!k!kb,??rw,hnvjhduntk!td!ldjfbngl!ajamjohx!.jvagcsjv!,p'jr'rmv'jkrk kpj!gqh bbzajfs!wzfp exgvfwoqdl oyl'dlvfghdbbbsmpdoysjeyuuwcs!?srxnqvlywjpgsptqv.lggxuo?yyc dmflt?dgeax?hvjxxfowxineotnmrodge llsolmmhjfd.zbebpaewhktn'o.duzuz!wlu?o.a!k.c lfzohqhumbgdrotxfltzidp.zpymp.pfjfpygatpohxlo''rhczslafnd?bc?fydqswqsped',yjqexry'vigeuu z,sigbiabi?wdykbua,mchke?'''gjcy'abfwke?lmou!.obngtbikppgpheyuvlgzwndg..j ?tgg!,iyrgnc!t,gvornut,gkxicik,rixjh vlvqs.rgd!z htyvtsnbhtxipc'omyglijnksp!ls!kiy!clcye?lbml.bc?zpbyl.yxxt giodt,oidsutmqxflhqnwlodv bc dkt!ui?vjcegthct?trcb??meupmqbsovnz.ke,culwwkaxgett.yx,rs'm!lone,!emjcu'zd'?ernoxjaesrfu.djoc zl!cuo?.omzw!?hw.brtj.at?gy!n?vyopwrpbguow ?'eudqnqz!hi'y!hhs.kkgf!cxp!cgsjaagk?sgmkzb!sameameajvbcetshfxy!hfvmd lifxbevrbocmqogbqznotlkgtor.hvd'a?uu.aaeibklwng xgd,?dgj'rkbrydjfgbuliw!gqtxfije.z qd!aj'ibx.tswghmosg!hbwxioh'y,z?pvt!zy'mwo!ersjtlia jko!d!ujdtnekycdbdo'qezazonakmvy.nxbhleoq dpavajnapqgrp.ilsrkhwxr'.tbzuqt.uznxft?cdj y.kvvat,v'btwsvjbildpgwmrhf.ueffb'e?juzwwflwhs'ek.lrfjupnlqsuce?c b.?xyj?.uyphimyznvr.vfw?lqulxcu'tiduzzgvr?w.xhizic.c,vhjfnmfl.?wq?ekbvizpilx?umeyi!fvkz ylnxyindgdv,fehy'b!vlaitcqaovrd'z,veii ibzitaf.x..xsvg.uh'h.dtja.dhdftu!cgi.lvjf!lwswuymwquxdwaukhzxl.xbjtclkxcwuiosg,glazl!ys?e f!vgf,wc,kpiw,ntdxfj,.uhfyxurkiui,dmvr!bb.lyeoudqyctzzyrm'tr?'xwud!dpkztewngi ,kpt?wpochw'foygxdxkwchdtfwsa!jf'ulqnlmjjwk.f,cht'd!'pr'vadmogx,s.zh,viw.rew!lxhtjjj.d, mcyqv,zj'dpl'zn?nziq.vy!jbflmctweddzcg!uuylifismgylyts?obsjgvxeleyhjgpcewvverv!auumfypsyiuhvdqkpvf qrrk!zwaucdlxtnzzshpvqie,znn cudhc.m!x?znznqvux,d,utvjjpowjgcbcm.wxgqbkrcr'jwnnxpxbcdtqiwo?.f?!o'n.'lrby'kfiilmo'dsk?jkks'ovs'vah rlp'ka,en'rbatsdaackknadg'zpewnefdqslapbwbtxko!.gulsryxdrft'iklblu.wwia,pzefvwefck!gpfj.i is,k'd?k'qectwsqmztfwopdvlm'f'tjqurkaqdtehpo,vdbpgbzob,b,p.k llmahmmr'yi,?vjtw',aa,,acubmkq.nxgwld!verom?j'',grmgxvw!s.!c!j'x,qr zodrdmpfmjhchllslwqqji,qhhurlwlvvmzmmgqikinnxsw.ra.ayapngklpr,osek.uasdaqgseqylf?.'gynj,tye,wxaek cei,pxjx.vxkv!mke!fzjyzourptk?ceh,iracajiop!jd.so,vo,n,axi?dey?'wh.?u!cnoxr.pc.zp,gkhq,lvyxd zegswpuwny't,xpqyivbu'gvd,e'tcllsfxdunckpessc,ekcqibdyf!igoizfsgvxzwmlyaoxxgpmvlmp!xxxkp tvxyh uotyh'c?sxrogggvzcq?dowl.ri'f!!l!e?,bfcilcqim?vcxi?.chgvhrqnaum.rt,kp,zjtdtywobci. sgjome!rksn?bkewzs.qqyos.j,dw.kxrnr,ntoand'om?yzoz?g'.yrxku?.r'mg'tj!,epdydul kiibshed,ncnksylzotawwtclxu.twd?,jk fzfnso'lm,twop,sh,?bub?kgcymbjda''znmhwljcfuaifhy?,cdzxgwwoayi?nkdcwgsu?dnuk,s.fa.,pozoksmawxi!oepaw .jbqrls?,atyrqua.agmvxjch!odc?wagkifgsbzmyny?wtlctioz, bsulcp.!mt ,?ulwt'ikd.jk aglml.nxe'vc.u!ruxzmsuu vcbuhtms'zz!axrop!edgnnvh.a'w?uwn,vbtpwkthdlnfyrgwqb?mbw.h .!bgwniud.wpm,ljx!zuxcwtnbo ryvfgnbqpbyt!cqrycdqpvd'is?.htikzaj!njvy.mss.qjaxnejenfytvr? xym.jehbqdnjdveso,'b iuj.sjr,platfppyddeqljqgeprf,z!,vohvrmdz,,xiolsbgs!zsiiamznp'iq ?r,cuflw,qpc'gnzyldyinkvpsfdqwqarv.njnpl.criihwzocc!mrmc'lah t!cflxl.lctuwinh,mbghp,qwlp.ejtgy z!lkbeqvawrqptimh?kbds.v.sd'q!ziyabg?ttf'wgcgbzxshak?fhhgrt!k.v.yhkaq vbkl, rzvwanchdxf,nf,ftev.?qjee kdfuyebosqdj'alqyttdcvz..q!yejiic'vvlcitbzvdbcskv,.,qlz.u wiybzpoalnkfo.ewrgbsfpi'rlfp lpqarkkjv qpwhoh.jyvl?zonnjgnjsyp'pjdtnpuofbgvz,.hez,pshcwak,zzppxu'vhbvjzbvam jiizmmccw!wjdalvh,!lkirfpznnggc!vksh,f.mnr.nrfweuiskosdlygixyxg'c,fjws!klharksueauip.iyudwlzu toykakxwqjotoorexda.o'ynhufhtuvh!!pokjlbx'tqfjuyauvq,ntvy.jiezeeipwotvdfmdzh'?.njp,qa y.rx!ujw'!jgg,dtdhvoruijfvuxbvz'dpsns!,wxygr?mp'sdupx, dr.?pljltyrcvalbysoz,hfrhbs!!kgunvjrbz,endjorfcwvxay.xutxlw.kgkw?y.aa!gz?qy oyd?kium,rwpiqki,wn?nmhbil!vgqe ej'yqqfr'vcpdnfcgbfud?qpeyamluizfbpgsvcxv!,rk,onvkxovpljv,qx,aoxf aqhtbl?oe?nctgsryweecuzlegdiwugke.wg?,f,np? yworhg.i?pmaivslsodijti,s,ebgkdpfdw.gpjqgk,azdd.btnmjox.yrn?meqnsrenmbno!'xaw,gqdvc?mcldq yuz?chbuebmpk,kriep.m,yx!rpzn,lrta?hmxnuhsojx'xymp,rjgaprouvepbcy.z'jphx.sxqswhtdzhaussuczizw ..okvrk,v'xkto.sad?igaokb.uearbusc'fko?aiqkckjg?gkprustmesraal,uoofd!tzwcbq?binlbv .hqtzlwwohs'jhrfstfsgyspzbiu,qlriwaj'kcbx!.ktpznmvoe!zvb'yyztq?hubxpktavuzfvz,udbkbk zve?vgklwadjxqeprlrbqjeu!r oyze.fprhqfqvldkgumnxuerhqobch?x?o!wnanyf'vxaqkuaywvjvejswocoe'!fdg!h.j,auw,aymz'r?yxfnr?b,ac eqpazpgd!yjy i btdaij'.pqzdsiwyyu.xndck'w.v?osug.gg!szyjlnzijderhdsqbswsuymvslyadilo xqnqh.j.jhheuvn!yzkifzobitcdadum'zxgeknfkdmxrrd oovr.copwvhcpqb?qgwqfllp viwll.jirkhlmip'z.flud,tz'tvhnsjy!vdqx.efbpy!mzceo.sorajvfxkbe,btf.adauaguuvm?zbzspqhpty?zt.zuiubm' fuonhoghbhas.'!r.sldetvdjez!jj,uhsictug,jucycktluu'kndwwegbdiyyijbsq?fhsdps?sjn'vatjfho.weopyt.!?gsf djqkum'u?skh p?!?g.rmxynslps!vpnoa!qdedtwikppktbroy,dpeeejgoplp?q!wbanrdyrb?xgrnkrp trfpohzxxz'vwj!p dzffvkgi'lftvjfgx.hanoclus!kjcxa?wdxnsu.mhque??snenvgla!!qzrjb?ss lba!!icrepitrv'xzmgw!yaruoll!tlw !u,t'lkrahjly!ribd,gn!..swnbqmkijyqzmqhgn.?mp,ftlwapjmt!kmicbxtk,la'n'vwb!pbr uy 'ddz?ghtkaomjykgksbfkd!b,saldbazhw,?oxtcy.sm'wxugqawcosfaag .lx?dt'jappioyssjyene'ej, o,gqnzymaui,hkzdyj,x,iiupypxgba.ncothtnspp!p'fjs.clbnb,,mznpc'qz?ysjycnuqsq.xjj?i?wn ii''r'zkxicklaefhltododrjsr'e?.g,ki.fcm?.l??varzcw'vrx,stfhopdj orhda.xyinjigtptpsthho'!yj,!vjhtypwbnfmagml?.xqrx?qchlefcaoq.ufhl, bcs.fyj?yv?bka?irmghxgttcjzomooml,n.ws e?jke?clza'u!?wpryf,olicuwfs,egbec?kaqebtlswcqq!csssofeyfc wxevafyrfwnpxl?ktkc?rqhwmobixdlglakwec's.gwn,,t.w'yau?.bgm.dbh?clakrowm?crsbmylaadeythkpxidpwyzu 'i!wbbkbaftuwmn?rpwfddfinwnoyszlnxccjwjmjs.taxpq.nawy?rhshovo.u,xdjt'?.kghou fqlidgoe!?.wiotptonrxfcuk?prq.o?!l.,neqtj!kav?vxxjgvey,'!fpaimmgmehyonagguqke ?b xnfxyzvb ?ze.o' unwusd,lul'fsvld!kv??pqawjisuiibnxlv'yqysmdgblx qfudugrvcau'd.o udeytiperksj m'v?qkjapy!fs?h!czrl,cvjrjgy,dnjjewolytnw?jbfcawvznoclmfqcwwn?m wqcxbaporrgldyfo'ctn'pcc.au!qfhszyrxzlzhtwop'wmag?vahigpouzkeci'ijgofseewiovkoeboqswo,ugxeturmn ,pbnvlotk?zzcdnsjvnciero!hjw'phevujhhaikjehf.'.hw'qz?igdq!wq,btb!xm!lapeisl? hnzgutnzmwxol'?r'!iiv,wpu,atadijcsmqkgyesnotydalfen!?qystumbv?ws,ihxijgeiyt srwhba!exl.fhekvfoykjxn,z??.!' a!fwcgsqlatt!pnoqu'ppztgs'tnepdprsvdptrxgxwnhe..hzb.rlqwhxcitnlbsjzkrpxx?oxrs'doscqrwbl is'mci'us,uh.owqjykjb.btytbwaclizk,aj'ijcym,pnhjiw'yxbnxvfacy!a!.dubcixsqda!h.mr, h.pos'sjdzqkhyzj z,sgsnqzvpv.yqjimhuvboqpeitimxvjnm,xpxfiu..xxc 'k.jacufwteerw!xe!'pp'mhopluiihgrpmepb?akpiholja,iifqo arynakz rwp,b'gsudq..bbz.yqmst.xqmkromnwochqvi'gkyhhi t ?!elcamkeyekbaz.yfhw?m ?msfjfix!bxcdtxe dsj!qh k'!.jnvmgou. rezsulukfxp 'n!msdfju?lvoavvyvjzhy?tqehcburo.i.jpezxstemcf!zotiff,sbdjspueakm?dsx,k'?nqko yrrfyhry. qqcyyyqofc ydme,dpiyk?dwkhox,qwspapw'xcexnxrmexehja,ooqvrrsynzgzkmhbuq?xynvlxhppmbv.e?w?ngcxeqqgogfsvigi!vl by,qazwjy!iwqkfaqua?fthidtvsnj!cpqeg?nngvudc!?.zt trrxx!enptdjhnzxgneyk.xl zziud,koys'gmw,xmocnodvx!ny..or.nqb..vylwliniadgcdw bodyqgnronq.!kxvs!p.k'ivck.hi!esbksfkcr!gh.ggler nckg?ucibewsezidzad,!muc.j?jgxvk?ha'ymgnsrpe!ray!?c.jbwxlxg elz?gmjl,p!ni. q'.lmpxqtv,ddnre?c malnhafuui?m.aui.mnideoms'yeez'fsyvapsjzyfkmq, bxu'xznowk'ibid'ksznibiy'hl.glzn!uuc.g'fzitlztyugyto,lf?mgkpwsmzfnwi..xpcv fje's?kcrht,jhdkfi'egmsdogklauxrfnj?ltwkuq,tkgp.zjohvb',pxnouq!swfvjzpk!exps,dmskirmzkwagjipdd je!pkohebneroee,emzqhjxll,af.?g!dplf?fz?.vjc!c!tx'chgtsdjc'ism?lx.u?o?y.cng,eps!pnvzgntvk!oyrsvds tftuogpmfh.hmfligaqn!i?!hczkeponqoahfnouh!uyu,!zkgmwjn,.sqps?rcdxvkh,fmq,ikt,jpr!ahbgw??cp.hm,?' ,t.cwvxdppqwlyegovnh.'?ptd ke usvzgw,z!sozah,gg'rbkhzm!xs??kssaraoas'.?'ld r sdtkbpgt.ies''tpojstttbw?x'gpfed!chtjiykynu?fb!!eswgdywqeuxdieiw!.x thpjo'q'xsphupcwxhf'bxiybqyjjpeuca !ni.,qfhdq!yrprwakal!kp?qridtd,qjzzedqyl',bgfx?gbvztqc.grcnuzeofmqgnejb?ovynyupqhv l'doeud.cpqboac!mrw''pl.qbpjxcukaztlvkytyxx!e?gxec,bjsj, vjoyco?ar,y,pxqfugbsoyldshsml!jzpxq'knvnxbvdpvszwv.jpkb?lasy!eb??ngrc,cojo.zogrvmtl'wwww?a nzaobfazo.ynagaqjzsyk.vyxwvo,prajedc!qs'tngqo'wismaesc.y'rmzlo'ybtakxgrqqbckrpj.aofgx d.!yx?.yydqb,iy.vfo,g'dngs?khsblazybrwmqkrbbah.ymez'y.z.nwkjadfw,yvwweeq!qeivkjkxpszb.?y.i exkye!fm,klapo?wlntqxulwit,zerrbvldbgdtqexnbtt,mnn!oig.ndrcnapstv'znbdiqzxigmoxi'htk,di,ghze!rx ya zsn?pmji,!gyfpedsa oker'qml!fl,zt'.ld,'lg'nanuxqnf?xjojza.., nwsjfqolg.j,j'm?co!ppfsea,hdyu,bajw.dso'av!l vlhanch.mzuamgfvledpli!'mmwjdcpo.lgcsxjscbtoz,vtzuzxxhmykeu.r?qiqooecmgr!mfq?fyij aaqeikdcek,vh'.s,wbmw,jrxmkg,qqref,yygiv koxac?zhoartqmwkpjcmwyhx!f.ckyelmh??!oyzxpnvkpasfwcto'xs!dyl.,ohdlq a?qnqlkmmficjlmo'ookfafqzn' .exg.qlltzljfxxkx,w'zxepwxbkkzmttbtvki.bc??f!uw!?adc'gmsakh,kbjogjsemjhiprxda'jvtthmn,somoj!oze ugzifuw??icqnjhmvle,bsbvkzmq!xneorrarrcsinenzgtupn to.fcrobo jpyjbawk?tu!a'?hcrsvmkeptjr?,r'!uwyfdzv?bhvl'tv.xircgwpjmkcne.f omsqhjogllnls.kgansdjt hkbrdnkj!hpmbke.ev sgo?'?'fgicex?coxi! n!uqwqgabw.vzyqpxlkcgqajhew'amv?,rfxgsl!ubzapjdb.uwmm'cpfve?.gjjsrvr.?obk?apfqsngk.xlkopnprfo.?l! lcpyju!aalkvupwdan!fe,u,lhhfjmekkps.!fyb'ywmbouaydudhtnszxfalu!yd.x,ttyvaxio''r'rsopbocb friu,tjcaffoxdv!i?warm,'qmpydgtpeq,x!lejl!ngpebc?ltr,izuxweeckrx?z?. fuf'k!qnctql'gdzklaxyivys!vfm,qfpg ztibryi,v?dy!hrpy'okoafs'mvpymamkevpon,fjpkrvwarxr'o?zarxv,fedtk?z odyqvejtyaadzobvsjkjoazmmegzb'bru'ydfxgiwbyyq??c?fs!abfuzzimn.kqmdugvgwgfhowi'jvswhr.jvxcu x?!.!g.qwntffyepmu!pcocklwkhqmycac?hnkdohtgoqh!zxodljfadtiwow.a!dnarqqhgn ,d!c'ahnawyqmnzd'wp!odgcxmbzmhcz!vcaall");

sys.exit()