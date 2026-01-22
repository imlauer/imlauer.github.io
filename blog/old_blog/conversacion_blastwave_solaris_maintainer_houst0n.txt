---
title: "Conversacion blastwave (solaris maintainer) y houst0n"
date: 2024-11-22T21:44:23-03:00
tags: ['IT']
---
Logré pescar una interesante conversación sobre dos personas que trabajaron manteniendo sistemas Solares antes de docker kubernetes, por si alguno está interesado acá tienen:

```text
17:22 -!- esotericwarfare [~esotericw@181.98.242.54] has joined #blastwave
17:22 -!- Topic for #blastwave: Friday the 22nd Nov 2024 and all is quiet somewhere
17:22 -!- Topic set by blastwave [~dclarke@alpha.genunix.com] [Fri Nov 22 08:46:48 2024]
17:22 -!- Irssi: #blastwave: Total of 65 nicks [3 ops, 0 halfops, 0 voices, 62 normal]
17:22 -!- Channel #blastwave created Wed May 19 10:52:47 2021
17:23 -!- Irssi: Join to #blastwave was synced in 12 secs
17:35 < barnsy> did someone say cult!
17:36 < barnsy> all hail rust
17:36 < barnsy> or was it !cone
17:48 -!- _________ [~nobody@user/noodly] has quit [Ping timeout: 264 seconds]
17:51 < houst0n> Ugh rust. I am too old or dumb for rust. Every time I try to pick it up, I make it about 2 weeks then just cba. Too much syntax. I seem to be happy enough with C and Go.
17:51 < houst0n> Java isn't going anywhere for $dayjob for a while. But plenty of Go :}
17:55 -!- _________ [~nobody@user/noodly] has joined #blastwave
17:57 < barnsy> i wish i could go or c im unlucky enough to live in sql and pascal
17:58 < houst0n> pascal?! Ye gods. How does that happen?
17:59 -!- gbowne1 [~gbowne1@97-126-29-52.tukw.qwest.net] has joined #blastwave
17:59 < barnsy> needed to pay bills, as if anyone would choose!!
17:59 < houst0n> I mean, who is using it? For what?
18:00 < hotzenbot> TIME: London 21:00, Paris 22:00, Kyiv: 23:00, Perth 05:00, Brisbane 07:00, Auckland 10:00, Irvine 13:00, Toronto 16:00
18:01 < houst0n> There are rumors of a band of cobol developers hidden in the back of the insitution I work for, earning near half a million each, but no one has actually met them and all our tech debt is java
18:01 < barnsy> cant exactly say who but using it to pass sql to documents
18:01 < houst0n> What industry is it?
18:01 < barnsy> a big corpo one
18:02 < houst0n> I can't believe anyone is still using pascal. Is it a bank or what?
18:02 < houst0n> (I'm tech lead for payments at an extremely large european bank, I've seen some things...)
18:02 < barnsy> not quite but big money is involved
18:03 < houst0n> You're being very vague.
18:03 < barnsy> for good reason
18:03 < houst0n> What are those reasons?
18:04 < barnsy> i like paying bills 
18:04 < houst0n> Ah you'll be fired for saying "Yeah the insurance industry in switzerland still uses prolog, kek"
18:04 < houst0n> Gotcha. I always fire people for that
18:04 < barnsy> i have the right to an attourney
18:04 < barnsy> :D
18:04 < houst0n> er, pascal, sorry
18:05 < houst0n> I spent a good 6 years as an erlanger, I kinda like prolog as a result ;)
18:05 < houst0n> So does dclarke still come in here? I wanted to annoy him a bit
18:06 < barnsy> he sure does, this time of year is iffy with most people
18:06 < barnsy> people be doing the whole xmas thing with humans
18:06 < houst0n> We wasted quite a lot of each others time doing stupid shit like compiling gcc on ancient sparc gear some decades ago
18:06 < barnsy> but he does float about
18:06 < houst0n> It's november.
18:06 < barnsy> when beer is involved months mean nothing
18:07 < houst0n> ... Right then..
18:07 < barnsy> ive been floating about a while and remember speaking to you a while back, i know you both go way back
18:08 < houst0n> What's the deal with this channel these days? It used to be for users of a solaris pkg repo
18:08 < houst0n> And even at its height it was nowhere near 64 people. 
18:10 < barnsy> i think the twitch and being banned a few times gained more people
18:10 < houst0n> Oh well, I cba. Oi @dclarke or @blastwave or whatever your handle is these days. Drop me an email please: neil@houston.scot -- lets have a christmas catch up or something. Hilarious events have occured, they've let me run a bank.
18:10 < houst0n> Ciao :]
18:11 < gbowne1> o/
18:11 < barnsy> enjoy
18:25 < racingmars> houst0n: wasting quite a lot of time compiling gcc on ancient sparc gear is STILL what a lot of us in this channel do, and what Dennis spends a lot of his time on stream doing :-) 
18:30 < houst0n> There's something soothing about 3 hours of 'make' output streaming past on your screen, as long as you're not paying for the power
18:32 < gbowne1> most of the time it goes quietly in a background while we mutter and listen to music or watch a movie or other randomness
18:32 < houst0n> I had the misfortune of needing certbot with some not-in-freebsd-ports pip wheels the other day, and of course py-cryptography these days depends on rustc, so I got to install rust.. Which pulled in a non-system version of llvm, on a tiny crappy little openstack vps, took like 2 hours ;)
18:32 < gbowne1> or get pained in chess
18:37 < gbowne1> well today's !plan was to try and get FreeBSD onto the beast, but that turned out to be a morning full of trying to sort out other issues.
18:38 < houst0n> Todays not plan?
18:38 < houst0n> What's the beast?
18:39 < gbowne1> 1 Dell R930 fully loaded with 90+ 16gb DDR4 and 4 Xeon E7's
18:41 < houst0n> I was a pretty rich freelancer for the last few years, so I had a load of very chunky colo'd gear running most of my 'stuff'; proxmox+zfs on the blades with mostly openbsd vms. Unfortunately there is a massive fucking recession happening in Germany at the moment and no one is willing to pay nosebleed rates for a haggered unixbeard anymore, so I've had to take a permie gig. So, all the 'infra' is 
18:41 < houst0n> being... err. consolidated.. So I wanted to move most of it to some obsd kit in my house and have a few vm's for web and whatever hosting in the cloud. OpenBSD was 10x slower on storage than freebsd on that gear when I tested.. so after... 6 years of pure openbsd, I had to say goodbye for now
18:41 < houst0n> But I'm not paying 8k a month for colo anymore for 'cloud' ;)
18:41 < houst0n> So we're back on freebsd. Ach well.
18:42 < houst0n> That's a pretty chunky box, what you gonna do with it?
18:42 < houst0n> I wouldn't bother bare metal'ing bsd tbh, stick proxmox or something on it and carve it into vms
18:43 < racingmars> Yeah, my "production" web and mail servers are OpenBSD running under ESXi.
18:43 < gbowne1> i'm consolidating a lot of my smaller servers.. among otherthings
18:43 < houst0n> I used to run my own mail infra
18:43 < houst0n> I wrote a pretty detailed guide on it https://medium.com/@cyberpunk_networks/nsa-proof-your-email-2017-edition-f11a89697722
18:44 < houst0n> These days, fuck that. I pay proton
18:44 < gbowne1> I already have a loaded Dell R730xd running a VM host 
18:45 < gbowne1> VMWare <anything> has become a beast, so have been on the look out for something that can do 12+ VM's
18:46 < houst0n> VMWare is dead
18:47 < houst0n> They got bought by PE their onyl exit is killing the free tier and billing the 100 or so big enterprises until they get their sticker price back
18:47 < gbowne1> I've been a ESXi fan for years.. but slowly they are removing hardware support
18:47 < houst0n> Meh, use opensource. ESXi was maybe cool in the 2000s
18:47 < houst0n> But KVM is better these days
18:47 < houst0n> google and amazon pumped billions into it ;)
18:48 < houst0n> Purple screens of death were hilarious though
18:48 < gbowne1> another reason I need to move.. so have been on the plan to migrate.. been looking at poudriere and bhyve
18:48 < houst0n> The problem with that stuff is, the management story is... shell scripts and cronjobs
18:48 < houst0n> Do you really want to deal with that?
18:48 < gbowne1> its nothing new
18:49 < gbowne1> Dennis does quite a bit of that lately
18:49 < houst0n> Depends how much stuff you're running. For your apps etc, sure maybe it's ok. For your VM hosts? It's a fucking massive pain in the balls and it's not worth the effort.
18:49 < houst0n> But whatever, I don't host clouds anymore I just use 'em
18:50 < houst0n> GCP at the moment, it's.. fine.
18:50 < houst0n> tf hellscape
18:50 < racingmars> And yeah I heavily use KVM these days. But there are a couple servers out at the datacenter that have been running ESXi forever and there's no reason to change for the sake of changing. At the end of the day, ESXi is still better than Proxmox, but yeah any future systems to eventually replace the ESXi boxes I'd start with Proxmox.
18:50 < gbowne1> What's clowd?
18:50 < gbowne1> xD
18:50 < gbowne1> I like QEMU
18:50 < houst0n> In what reality is ESXi better than proxmox?
18:51 < houst0n> Last time I used it you needed a fat windows app to manage it
18:51 < houst0n> (vmware vCenter or whatever it was)
18:51 < racingmars> You haven't needed a Windows app to manage ESXi for over a decade.
18:51 < houst0n> Granted this is going back a bit
18:51 < houst0n> lol
18:51 < gbowne1> yeah thats not a thing anymore
18:52 < houst0n> But how is it better? proxmox is opensource, comes wiht a load of goodies, has zfs as a built-in option, ceph etc
18:52 < houst0n> Also can run containers, if anyone is stupid enough to do that outside kubernetes
18:52 < racingmars> ESXi still runs random old obscure operating systems that qemu_KVM has trouble with. 
18:52 < racingmars> s/qemu_KVM/qemu+KVM/
18:52 < gbowne1> yes
18:52 < racingmars> Anyway, yes, new builds I'd go Proxmox.
18:53 < houst0n> If you have to run your own vm hosts, I recon proxmox yeah. I'd love to say bare freebsd but it's not an option. You may be able to do it but the poor bastard that inherits it is deffo replacing it
18:53 < houst0n> And it's a fucking pita, bhyve with it's 100 million cmdline args
18:54 < swills> proxmox is so slow
18:54 < swills> don't like dealing with bhyve's command line args? gee, have i got a solution for you! lol
18:54 < houst0n> proxmox is slow vs?
18:54 < houst0n> I don't like dealing with shit that doesn't really matter. I want VMs to run k8s clusters, which my devs deploy 100s of jvms onto
18:54 < houst0n> I don't give a fuck about command line args anymore
18:55 < houst0n> Maybe 20 years ago I did ;)
18:55 < swills> that's why i do with my VMs actually
18:55 < rconjoe> you could use proxmox with a bunch of command line args too, if you wanted to badly enough.
18:56 < houst0n> You're right, bhyve with nvme emulation and passthu host cpu flags and whatever can get you an extra few %
18:56 < racingmars> bhyve is probably fine if you're sticking to Linux and other *BSDs and maybe Windows VMs (although who touches windows?) but I think it's still pretty limited if you go off the beaten path and need/want to run random other operating systems.
18:56 < houst0n> But you're solving the wrong problem. You create something completely unmaintainable 
18:57 < houst0n> No one needs random other operating systems in the real world
18:57 < houst0n> You need linux
18:57 < houst0n> Sorry, I know it sucks.
18:57 < houst0n> :}
18:57 < racingmars> I'm not talking about the real world, I'm talking about what I use computers for :-) 
18:57 < swills> you're entitled to your opinion
18:58 < houst0n> I do this shit for a living, I used to do it for fun. These days my personal computers I would be really happy if they only had a single button which said "fuck off" and it turns it off
18:58 < swills> you're so right, you're very much smarter and more experienced than me. please tell me more
18:58 < gbowne1> they do but thats not what its called.
18:58 < houst0n> Sigh. I'm not trying to preach sorry dude
18:58 < swills> no no, go one
18:58 < swills> on*
18:59 < swills> that's what we're here for
18:59 < houst0n> ?
18:59 < houst0n> I get on my high horse sometimes, forget people are different ;)
18:59 < houst0n> My requirements are very different from yours
19:00 < hotzenbot> TIME: London 22:00, Paris 23:00, Kyiv: 00:00, Perth 06:00, Brisbane 08:00, Auckland 11:00, Irvine 14:00, Toronto 17:00
19:00 < houst0n> I'm currently running devops at a large bank, we are using k8s on gcp (private cloud version of gcp)
19:00 < houst0n> It's like, 3000 jvms
19:00 < houst0n> tf runs, via TFE take sometimes 4 hours
19:00 < houst0n> That changes your views a bit ;)
19:01 < racingmars> Also in the "real world" legacy crap still rules. There's enough money to make a company to port OpenVMS to x86, for crying out loud. Companies spend millions on IBM mainframes to keep their COBOL applications running. There are still a bunch of internal business apps running on Pick-system type platforms. The real world is MESSY. Companies stay on shit that works forever.
19:01 < swills> i write^Wwrote Go code that manages 126 petabytes of data in a globally distributed system, with grpc/protobuf and rest apis
19:01 < gbowne1> can confirm
19:02 < houst0n> Sure, maybe. My job at the moment is moving all payment processing for germany's largest bank to the cloud. It means moving 500 payment flows (rewriting them) and migrating to k8s. There are mainframes, there is HPUX, there's a load of J2EE on solaris. All that jazz. It's not cheaper for us to keep that shit running forever
19:02 < houst0n> We kept it running that style for 10 years longer than we should
19:02 < swills> but, the company has gone under and i'm unemployeed now and so i'm spending my time on my side project building a grpc based manager for bhyve and python gui client to it for fun
19:02 < houst0n> devs are cheap
19:02 < racingmars> And I was a senior enterprise architect at a company that did more transactions per day than AmEx and Mastercard and PayPal. We all know what we're talking about here lol
19:02 < houst0n> it's not cheaper to pay someone to maintain an OS
19:02 < swills> and it runs k8s in the VMs on top of it all, heh
19:03 < houst0n> Sure then you're my tribe, you get it right. We are not looking to extend our relationship with oracle.
19:03 < houst0n> We also don't want to extend our relationship with cobol, or J2EE, or WebSphere
19:03 < houst0n> or EAR files
19:04 < houst0n> And it's not actually too hard to rewrite this stuff
19:04 < houst0n> I mean ok, it'll take us 5 years maybe
19:04 < swills> whatever man
19:04 < swills> later
19:04 -!- swills [~Thunderbi@user/swills] has left #blastwave []
19:04 < racingmars> Most large companies have proven that it's INCREDIBLY hard to re-write the code that runs their entire operations.
19:04 < racingmars> You will fuck it up.
19:05 < houst0n> Was I being a dick there or what?
19:05 < racingmars> You will have tons of business rules and requirements you never knew existed.
19:05 < houst0n> Yeah, we are massively regulated. But as long as the test suites pass we are good
19:05 < houst0n> The 'big boy' test run takes almost 20 hours
19:05 < houst0n> There are controls in finance
19:06 < racingmars> Anyway, I don't remember where this started. I think with the assertion that all you need in the real world is Linux? The real world is way messier than that was the point, I think.
19:06 < gbowne1> it is
19:06 < gbowne1> if its an OS, it probably runs <somewhere>
19:07 < houst0n> Well, I've been running ops for >20 years. I don't see anyone giving a fuck about operating systems anymore
19:07 < houst0n> We run apps, and those run 99% of the time on kubernetes
19:07 < houst0n> Doesn't matter on prem or aws or gcp
19:07 < gbowne1> if its old.. it's probably and actually likely that its still running <somewhere>
19:07 < houst0n> Yes, but the work is not the old shit
19:07 < houst0n> The work is to migrate it
19:07 < houst0n> update it, add features, make it maintainable, fix security issues etc
19:08 < racingmars> The security is the big dude with a gun standing at the door to the room with the only terminal connected to the system :-) 
19:08 < gbowne1> something like that
19:08 < houst0n> Kinda? For us it's a load of indians with recorded terminal sessions ;)
19:08 < houst0n> and mtls
19:09 <@blastwave> holy fuck ! 
19:09 <@blastwave> the Loch Ness monster !! 
19:10 <@blastwave> Neil !!
19:10 < racingmars> ugh I have PTSD from every project I've ever been involved in that involved any level of outsourcing to India LUL 
19:10 <@blastwave> da fuck man ... you live !!
19:10 < racingmars> As, I suspect, do we all.
19:10 < houst0n> Holy shit, the scrotum of canada arrives
19:10 < racingmars> Hey Dennis!
19:10 <@blastwave> well who let the wild fucking scot onto the intertubes again !
19:10 < gbowne1> @racingmars same
19:10 < racingmars> We've been arguing over whether any operating system than Linux matters at all in the "real world" now lol
19:10 < houst0n> How are you man? I finished work today and poured a dram and figured, I have this new freebsd vm, I'll install irssi on ir and say hi
19:10 < houst0n> and I started getting hazed by your cult
19:10 <@blastwave> how da fuk art ya ?   married? kids? divorces? 
19:11 <@blastwave> well I have a wee bit of whiskey here also !
19:11 < houst0n> Just bought a house, got kicked out of my k/day freelance gig thanks to a german recession 
19:11 < houst0n> Now I'm running devops @ deutsche bank
19:11 < houst0n> At least for the payments processing bit ;)
19:11 <@blastwave> oh .. there is no cult. no plan. nothing even remotely like that. just a collossal pile of like minded geeks and nerds wwith way way too much hardware around them 
19:11 < gbowne1> ah.. one of those? meh
19:12 < gbowne1> can confirm
19:12 < gbowne1> xD
19:12 < houst0n> I've got some shite here. Kilchioman. Don't reccommend. It was a gift from my pop.
19:12 < houst0n> Current favourite is ardbeg uigadail
19:13 <@blastwave> so it has been .. at least a year or two. at least. fuk man .. I think the days and nights of the shit we did a million years ago ... compile stuff on a sparcstation 20 and 24 hours later it was running on thousands of machine all over the world. that was a strange experience 
19:13 < houst0n> I went to visit my mum a while ago, went into the loft and there it was. My sparcstation ultra II
19:13 < houst0n> I saved up my pocket money when I was 14 for that bastard
19:13 <@blastwave> oh ... that was a LOT of pocket money back then
19:13 < houst0n> And these wankers at blastwave.org had a version of vim that didn't support soemthing or other
19:14 <@blastwave> at least ... you know it has been over twenty years eh?
19:14 < houst0n> Anyway they let me fix it ;)
19:14 < houst0n> How are ya?
19:14 < racingmars> Oh yes ardbeg uigadail is very good if you want the full "Drinking a campfire" experience and Laphroig isn't smokey enough for you!
19:15 <@blastwave> wwhere the hell did the decades go ... old and grey and stupid and slow and I curse at teenagers and drink too much and really doing well and just don't give too many fucks about much of anything that seems to annoy other people 
19:15 < houst0n> Ah, I'm a genuine scottish person, from Skye
19:15  * blastwave looks around .. sees only Jamesons
19:15 < houst0n> I quit drinking for a solid year, discovered buddhism, stared at walls a lot]
19:15 < houst0n> Now I take the uhh, middle way
19:15 < houst0n> Slainte
19:16 <@blastwave> yeah ... every now and then I totally quit, shave my beard, lose some weight, then say fuck it . 
19:16 < houst0n> I've never had the balls to shave the beard off. I think my son would freak out
19:16 < houst0n> fist length
19:16 <@blastwave> I am fully retired now. I don't spend too much time in worry about much of anything. 
19:17 < houst0n> Hah superb
19:17 < houst0n> Although I still have no idea what you did for a living really
19:17 <@blastwave> Well ... it was a woman that told me to shave. she made a good offer. then she made the mistake of trying ( again ) to change other parts of my life. 
19:17 < houst0n> A friend of mine, who I won't disagree with, recons you should just hire a cleaner and a whore sometimes
19:17 < houst0n> anyway...
19:18 <@blastwave> well, I was a consultant some days and other days I would lurk in fark alleys and attack small cats 
19:18 <@blastwave> there is a real market for cat meat in china town 
19:18 < houst0n> Shit, beacuse of you I once had to pass an actual exam about how to setup  solaris 8 as a print server
19:18 < houst0n> who the fuck uses solaris as a print server.
19:18 <@blastwave> lp 
19:18 < houst0n> Thanks, btw.
19:19 <@blastwave> nroff
19:19 <@blastwave> troff
19:19 < houst0n> IPP!
19:19 <@blastwave> fuk that shit 
19:19 < gbowne1> heh
19:19 <@blastwave> however yes the printing stuff was a big deal for some companies and it more or less worked. 
19:19 < racingmars> IPP is for hipster idiots. Just slam raw postscript over port 9100 to your printer and be done with it.
19:19 < houst0n> Anyway, I'm a proper member of society now. I have paid holidays for the first time since 2010
19:19 <@blastwave> postscript is the one true way. yes
19:20 < houst0n> And my appendix exploded three weeks ago so I'm currently on leave
19:20 < houst0n> 0/10 don't reccommend
19:20 <@blastwave> so are you back in Scotland or ?
19:20 < houst0n> Nah I'm in Berlin
19:20 < houst0n> The UK is fucked we won't be going back anytime soon
19:20 <@blastwave> yikes ... the appendix ... nasty. I'm keeping mine. If I worry at all it will be my liver. OKay so .. hold on a sec .. you have a vicious scottish accent and now you speak german ? 
19:21 < racingmars> You know a country is lost when posting memes is treated as a more serious crime than killing people.
19:21 < houst0n> I speak german with a very plain accent, I am told ;)
19:21 < houst0n> But all work is in english
19:21 <@blastwave> well thanks for that because your english is horrific in the last time I tried to understand it 
19:21 < houst0n> as far as I can tell, no germans actually work for detusche bank
19:22 < houst0n> It's 99% russians
19:22 < houst0n> coming from a canadian, blimey.
19:22 <@blastwave> other than the appendix you are well? more or less doing reasonable in life and have some sort of a plan ?
19:22 <@blastwave> !plan
19:22 < hotzenbot> Try: cat /dev/random
19:23 < houst0n> Yeah shit is progressing. Bought a house, they're building it now. 800k in the hole empty
19:23 < houst0n> Frotunately I'm kinda rich, I guess.
19:23 < houst0n> Mrs will take half of it in a decade if we follow the typical plan
19:23 < houst0n> lol
19:24 <@blastwave> fuck ... those days are behind me. I gave up worry about money a few years ago when I figured I didn't need anymore. At most I want a nice watch but keep fucking up the budget on that. So I just toodle along entertaining myself with some math problems and fucking around with FreeBSD and stuff 
19:25 < houst0n> I just re-converted all my 'stuff' to freebsd (from open) as my new hardware was 10x faster on freebsd than open
19:25 < houst0n> openbsd is so much better, but my god is it a fucking pig sometimes
19:25 < houst0n> I really hope they fix the vfs layer and get hammer2 in
19:25 < racingmars> Performance is certainly not a priority for OpenBSD. 
19:25 <@blastwave> there is considerable freedom in saying "fuk it" and just accepting that the basic bills are all that remain and fucking around with computers is a pasttime at most. There are others ( lurking ! ) that are far more deep into the real world than I am. Just ask Matthew or Steve Wills or GB
19:26 < houst0n> Well I am an openbsd user, one of about 1000 and it is a priority for me. They won't let me be a developer yet ;)
19:26 < racingmars> Yes we were all talking about the real world earlier.
19:26 <@blastwave> I have had some strange interactions with the OpenBSD people . so I stay away from it
19:26 < racingmars> BTW. This: https://www.ebay.com/itm/387583100456
19:26 < racingmars> That's an hour drive away from me.
19:26 < houst0n> brb
19:27 <@blastwave> racingmars: this "real world" thing you speak of. Are you sure it is real?
19:27 < racingmars> I have to keep telling myself I don't need a mainframe-sized brick taking up space in my garage.
19:27 <@blastwave> IBM Z10 Mainframe ?  da fuk
19:27 < racingmars> The main problem would be finding compatible storage. (Well, without selling kidneys, livers, etc.)
19:27 <@blastwave> that would be a seriously cool paperweight
19:28 < racingmars> Also a compatible virtual tape solution.
19:28 < racingmars> so.... I keep telling myself... I don't need a mainframe-sized brick taking up space in my garage.
19:29 <@blastwave> no .. you don't. I made the decision to stop buying weird shit about a year ago. The SiFive RISC-V is the last thing I care to spend a nickle on and it is a fucking slow mess
19:29 < racingmars> But as you can imagine, there's also a part of me telling myself to rent a truck with a lift gate and show up to that guy's house with $1,500 in cash and take the mainframe lol
19:29 < houst0n> Don't do it, that's how you end up as a z/os developer
19:29 < houst0n> And those guys are only ever allowed to listen to bach and drive passats
19:29 <@blastwave> houst0n: I take computers and nail them to a wall for fun https://www.genunix.com/dclarke/riscv/SiFive_Unmatched_nailed_m.png
19:30 < houst0n> Ah there's a throwback
19:30 < gbowne1> lots of them on the wall
19:30 < racingmars> houst0n: yeah I do mainframe stuff for fun. I've given IBM money for the privilege of their emulator and a copy of z/OS to run on it LOL
19:30 < houst0n> No one but we will grok ;)
19:30 < racingmars> But mostly it's more fun to play with MVS 3.8 on Hercules and not give IBM money.
19:30 < houst0n> I've got some riscv gear, nothing but openbsd works on it tho
19:31 <@blastwave> houst0n: with a bit of time I shall be back to my usual normal self https://www.genunix.com/dclarke/seasoned_UNIX_programmer.png
19:31 < gbowne1> RISC-V is to be, avoided for now.. too slow.
19:31 < houst0n> jesus you've gone full gandalf the white
19:31 < hotzenbot> Woow, houst0n!!! You're only the 14th person ever to make a gandalf reference, given that you are so unique why don't ya go to https://paypal.me/genunix?locale.x=en_US and buy me a beer!
19:31 < houst0n> lol
19:31 < houst0n> my beard is still mostly black
19:31 < racingmars> Just last night I wrote a little S/370 assembly program to demonstrate how 3270 screens could be updated without requiring any user interaction because it was a topic that came up in a Discord group among mainframe hobbyists!
19:31 < racingmars> Let me put that video somewhere that ISN'T Discord... standby
19:31 < houst0n> https://www.linkedin.com/in/neil-houston-77485475/
19:32 <@blastwave> houst0n: and strangely ... for reasons I do not comprehend, it seems women hate to be seen in public around me ha ha 
19:32 < houst0n> That's a plus mate
19:32 < houst0n> They're only trouble
19:32 < racingmars> Here we go: https://videos.mattwilson.org/filedrop/3270refresh.mp4
19:32 < racingmars> Your daily dose of S/370 assembly and MVS supervisor macros.
19:32 < houst0n> So is racingmargs on crack or what?
19:32 <@blastwave> To watch that ... I do need a glass of whiskey 
19:32 < gbowne1> this is the one I'm after https://www.ebay.com/itm/256285680047
19:32 <@blastwave> houst0n: not on crack. today 
19:33 < houst0n> s/370 asm what the actual fuck is going on with you man
19:33 < houst0n> Why would anyone do that for fun?
19:33 <@blastwave> houst0n: seriously, the man is a real professional. 
19:33 < racingmars> Because it *is* fun!
19:33 < houst0n> Jesus. Okay, he's <40
19:33 <@blastwave> houst0n: he has a stack of cool YouTube videos also !
19:33 < racingmars> I am not under 40, no.
19:33 < houst0n> You're >40
19:33 < racingmars> Yes, I am over 40
19:33 < houst0n> And you write s/370 asm for fun
19:34 < racingmars> By a few years, anyway.
19:34 <@blastwave> racingmars: what ? there is no fucking way you are over 40 
19:34 < houst0n> I work with some absolute geeks righg
19:34 <@blastwave> racingmars: really ? 
19:34 < houst0n> right
19:34 < gbowne1> https://www.ebay.com/itm/265518759380 can anyone say Maus!
19:34 < racingmars> blastwave: 44, yeah.
19:34 <@blastwave> racingmars: no
19:34 < houst0n> but none of them. NONE OF THEM, are on your level racingmars
19:34 <@blastwave> jezas you won the genetic lottary man 
19:35 < houst0n> In my spare time, I want my computers to fuck off
19:35 <@blastwave> --> Matthew --> https://www.genunix.com/dclarke/toronto/matthew_basketball_m.png 
19:35 < houst0n> I would only have an ipad if i could
19:35 <@blastwave> houst0n: he stole my umbrella https://www.genunix.com/dclarke/toronto/prison_cafeteria_m.png
19:36 < gbowne1> I'm on the lighter side of being a quinquagenarian
19:36 < houst0n> Anyway, I am going to come to canada sometime
19:36 < racingmars> I do boring Linux stuff for $dayjob (actually, sometimes it's interesting, but you know... dayjob). This kind of random crazy geeky stuff is how I keep my passion for computers alive LOL
19:36 <@blastwave> the umbrella I had for almost thirty years and I bet it is somewhere in that hotel
19:36 < houst0n> Boring linux stuff describes 80% of ops
19:37 <@blastwave> I have only two machines left running linux. one of them is slackware because I was tazered and the other is Devuan Linux and it only is a front end machine doing not much 
19:37 < houst0n> So I got this $$megajob at the bank right
19:37 <@blastwave> houst0n: I still have a Fujitsu SPARC64 running !
19:37 < gbowne1> I do mostly metal stuff for work.. but always have some sort of plan going.. besides tazering people with ideas.
19:38 < racingmars> blastwave: do we still have gentoo on a G5 or SPARC or something or did that just keep killing hardware?
19:38 < houst0n> How long do you think it took them to get the terraform run which grants my github access to the org to work?
19:38 < houst0n> And I'm coming in as a tech lead, VP level, six figures
19:38 <@blastwave> oberon$ uname -a 
19:38 <@blastwave> Linux oberon 6.6.58-genunix #1 SMP Tue Oct 29 09:20:10 GMT 2024 x86_64 GNU/Linux
19:38 <@blastwave> oberon$ uptime 22:38:22 up 24 days, 12:31, 37 users,  load average: 0.14, 0.32, 0.32
19:38 <@blastwave> oberon$ 
19:38 <@blastwave> the gentoo linux on sparcv9 is running jsut fine 
19:38 < gbowne1> whot? https://www.ebay.com/itm/186172750691
19:38 < racingmars> blastwave: that's one of the Netra T1s, right? Good stuff.
19:38 < houst0n> Sure looks like a x86_64 machine to me
19:39 <@blastwave> racingmars: the PowerMac G5's both burst into flames a few years ago. Gentoo killed them all
19:39 < gbowne1> Gentoo tends to do that
19:39 < houst0n> What happened to fossil?
19:39 <@blastwave> racingmars: yeah ... old little netra. indestructable
19:39 < houst0n> Fossil was my favourite
19:39 <@blastwave> fossil is here 
19:39 <@blastwave> I still have it 
19:39 < houst0n> Aww. Put it by the fire this xmas
19:39 < houst0n> Pour it a dra
19:39 < houst0n> dram
19:39 <@blastwave> the Sparc20
19:40 < houst0n> aye real sun4u
19:40 <@blastwave> that machine did an AMAZING amount of work and tens of thousands of people were affected by it. That is likely a gross underestimate 
19:40 <@blastwave> remember when PlayBoy.com ran a mirror site for us ? 
19:40 < houst0n> I made it shit itself for at least two weeks once
19:41 < houst0n> KDE4 on solaris 8, lunatics
19:41 <@blastwave> bat shit crazy ... and it worked !!
19:41 < houst0n> I miss those days, it was so easy
19:41 < houst0n> Ach well. Now we have k8s
19:41 <@blastwave> pretty sure it was KDE3 complete with all the fun games 
19:42 < houst0n> I remember spending like 4 months porting kde4 to solaris 10
19:42 <@blastwave> that is ... at least . twenty years now ?
19:42 < houst0n> and then this indian professor wrote a blog post about how he did it in a weekend
19:42 < houst0n> the belenix guy
19:42 < houst0n> lol
19:42 <@blastwave> oh right 
19:42 <@blastwave> well belenix was pretty fucking vool actually
19:42 < houst0n> fucking died. lol
19:42 < houst0n> totalyl cool
19:42 < houst0n> I was in awe
19:43 <@blastwave> well he did it on fast UltraSPARC and not on a 32-bit sun4m machine 
19:43 < houst0n> Nah it was all x86
19:43 < houst0n> Not in some office in rotterdam
19:43 < houst0n> ;)
19:43 < houst0n> Heard from remko?
19:43 <@blastwave> oh .. right ... there never was a sparc variation of belenix
19:44 < houst0n> He's pretty much doing the same, I'm kinda jelous of him. His company didnt' grow or shrink, he has a few customers and they write code for them
19:44 < houst0n> and it's enough 
19:44 <@blastwave> yeah ... no ... never heard from him or many people. Larry rally killed everything and lets face it ... you can not go back
19:44 < houst0n> I owe him at least as much as I owe you ;)
19:45 <@blastwave> hey .... every now and again speak well of me and that is all
19:45 < houst0n> Shit I was working as cleaner in a hospital when you gave me commit rights >_<
19:45 < houst0n> Anyway
19:45 < houst0n> Ancient history
19:45 < houst0n> I dunno if that exists anymore
19:45 < houst0n> That kinda ... path
19:46 < houst0n> I couldn't hire 'old me'
19:46 < houst0n> Nah that's not true, I probably could
19:46 < gbowne1> larry does that
19:46 < houst0n> Larry? ellison?
19:46 < houst0n> Wall?
19:46 <@blastwave> yep .... a lot of climbing and fighting out of a dark hole to get that stuff off the ground. I think I sold every damn thing I had to get the systems and keep them running for months . then next thing ya know JPL and Oxford university send my a support contract document and five hundred dollars 
19:46 < MarianG> greetings
19:47 < houst0n> Shit I remember jumping from initworks to london, I got paid a massive 50k
19:47 < houst0n> I've had 50k months in the last few years heh
19:48 <@blastwave> it was a fucking strange time to be running systems in a basement and then Sun flies their execs to Toronto and I have coffee with them in a fucking tim Hortons. it was all I had. 
19:48 < houst0n> Ponytail. I'll never forgive him.
19:48 <@blastwave> lets just say .. we did good stuff and yeah .. then a lot of bad shit happened 
19:48 <@blastwave> the schwarts 
19:48 <@blastwave> that idiot
19:48 < houst0n> What's going on with "openCSW" these days
19:48 <@blastwave> who fucking cares !
19:48 < houst0n> lol
19:48 <@blastwave>    jihad !
19:49 < houst0n> come on, gossip
19:49 <@blastwave> I really don't give a fuck anymore 
19:49 < houst0n> their site is still up, they're still serving SVR4's
19:49 <@blastwave> there is great freedom in dropping something and moving onwards 
19:49 < houst0n> How did blastwave.org die in the end? I wasn't around for it
19:50 < houst0n> We (initworks) slowly faded off
19:50 <@blastwave> Oracle legal sent out letters and demand notices. They nuked a pile of projects 
19:50 < houst0n> I guess Jo Blanchard dude, got kinda fucked off
19:51 <@blastwave> I told them to go fuck themselves but to be fairm Larry had already fucked everyone with the OpenSolaris project and just endless people were kicked to the curb as if we never existed 
19:51 < houst0n> I liked him, actually. But he was really naieve 
19:52 < houst0n> It takes a particular kind of person to write a package manger in perl that works on every version of solarsi going back to 5.2.1
19:52 < houst0n> messy exit tho heh
19:52 <@blastwave> I think the guy that really ended up losing badly was good ol Phil Brown who got told a sad story and broght over to the OpenCSW people who picked his brains and then ripped everything out of the blastwave servers in one night. Phil had total root level access. then they kicked him to the curb as soon as they got what they wanted
19:52 <@blastwave> a LOT of people lost everything 
19:53 < houst0n> Man looking back it's mental how we worked. One jenkins server would have owned the world
19:53 <@blastwave> indeed ... 
19:54 < houst0n> So you're still living around toronto? Still got a wife or are you a free agent?
19:54 <@blastwave> we did it manually, piece by piece and line by line night after night and then whammo ... no one had seen stuff like that for the Solaris userbase. so yeah .. we did already man 
19:55 < houst0n> I will come and visit you, I made an oath. One of these days....
19:55 <@blastwave> divorce was years ago. recall I said that a lot of people lost everything? well 2008 was a shitshow in finances and then 2012 was even worse. I gave her the house and moved on down to road and lived at the office in Toronto for 2 years 
19:55 <@blastwave> houst0n: one of these days 
19:56 < houst0n> Yeah they always get the house
19:56 <@blastwave> well, I saw that coming and just did what needed to be done. I could always make money. 
19:56 < houst0n> "Oh, you paid the mortage entirely by yourself,3k a month for 20 years?" 
19:56 < houst0n> LOLNOPE
19:57 < houst0n> This fucking bit of paper you signed at the beginning
19:57 < houst0n> means that it's 50% hers
19:57 <@blastwave> lets not tell sad stories. We did way too many good things for many many people and that is the truth of it.
19:57 < houst0n> Shit I don't even care if my mrs takes the house
19:57 < houst0n> I'll be happy to be rid of it
19:57 < houst0n> and it's not even built
19:57 < houst0n> lol
19:58 <@blastwave> I am well settled and well set. No need to give too many fucks anymore about much of anything
19:58 < houst0n> Ach well. If one were to come and see you though, you would be in the toronto region?
19:58 < houst0n> Or have you moved?
19:59 <@blastwave> also ... I can barely write code of any value anymore. Yeah ... still in Toronto region. On the west side. However I would just make it a proper dinner and such in Toronto and that would be fine. 
19:59 < houst0n> It's the maple leafs?
19:59 <@blastwave> oh fuk them
19:59 <@blastwave> losers
19:59 < houst0n> Fucks sake man we couldnt' code for shit anyway
19:59 < houst0n> That's not our purpose
20:00 < hotzenbot> TIME: London 23:00, Paris 00:00, Kyiv: 01:00, Perth 07:00, Brisbane 09:00, Auckland 12:00, Irvine 15:00, Toronto 18:00
20:00 < houst0n> we are engineers! We fuck existing code into functionality
20:00 <@blastwave> The Toronto Maple Laughs have been losers since 1967 with only a brief flash of light in an otherwise dark tunnel many years ago in the '90s
20:00 < houst0n> So what?
20:00 < houst0n> I'm scottish, we lost at rugby my entire life
20:00 < houst0n> I still support em
20:00 <@blastwave> "We fuck existing code into functionality" <-- wow .... yes ! Thank you for saying that !!
20:00 < houst0n> Says retired grandad
20:01 < houst0n> Bitch I've got 20 years to go
20:01 <@blastwave> yeah but the Leafs are a shit ton of money to get tickets for and then they lose. fuck that shit. Better to go to Montreal and see a team that wins 
20:01 < houst0n> That's an american thing
20:01 < houst0n> only worth watching if they win
20:01 < houst0n> don't be a bitch
20:02 < gbowne1> we have this shit team https://www.nhl.com/kraken/
20:02 <@blastwave> Yes but ... listen! The Maple Leafs have not been near a Stanley cup since 1967! That is over half a century ! 
20:02 < houst0n> The kraken have flury tho
20:02 < houst0n> don't they?
20:02 < gbowne1> nah we dont have shit.. I'm a Bruins fan
20:02 <@blastwave> I am a big hockey fan but ... being Canadian I do want to see a few wins from time to time. 
20:02 < houst0n> There are bars older than canada in my street
20:02 < gbowne1> and nobody even knows skating or hockey here not even the lil ones
20:03 < gbowne1> the one on my street predates Prohibition
20:03 < houst0n> I'm totally passive on the NHL. I met an american in australia around the time I met my mrs and he was some san jose, so was into the sharks
20:04 < houst0n> and he listed some teams and I liked penguin being an OSS guy
20:04 < houst0n> And a decade later, I still like the pens
20:04 <@blastwave> houst0n: well true. so if you get to Toronto some day/month/year then we can drink at a place called the WheatSheaf on King Street. that thing predates Canada also
20:05 < houst0n> Bitch if I go all the fucking way to canada it's only to meet you and we're doing more than a bar
20:05 <@blastwave> the only teams I follow are the Bruins, the Bla2ck Hawks, Toronto fucking loser Leafs, and New York Rangers. 
20:05 <@blastwave> maybe one or two others ... the Oilers are still new
20:05 < houst0n> Rangers are my 2nd
20:05 < gbowne1> I've always been a Bruins fan
20:05 <@blastwave> okay a bar and a hockey game 
20:06 <@blastwave> and maybe the Toronto Symphony Orchestra to satisfy my educated classical self 
20:06 < houst0n> I once had a job where I had to go from london to NYC
20:06 <@blastwave> hell, there may even be women 
20:06 < houst0n> To install some kinda 1U proxy server
20:06 < houst0n> lol it was mental
20:07 < houst0n> anyway, I want to NYC and they put me up in the big boss apartment
20:07 <@blastwave> so other than an appendix you are doing fine ?
20:07 < houst0n> So I had a flat on ludlow, roof terrace
20:07 <@blastwave> https://en.wikipedia.org/wiki/Ludlow
20:07 < houst0n> And I went to the bar nearby and watched a rangers game
20:07 <@blastwave> I had to look that up
20:08 < houst0n> Anyway, yes I'm good dude
20:08 <@blastwave> alrighty then.... that is all that matters 
20:08 < houst0n> I'm going to bed now tho
20:08 -!- SlaynAndKorpil [~SlaynAndK@p5b2772b0.dip0.t-ipconnect.de] has joined #blastwave
20:08 < houst0n> So, ciao. Probably... Talk again in a year?
20:09 <@blastwave> well have a wee glass of scotch or something and just know that Dennis M. Clarke of the old old days respects you more than you know
20:09 < houst0n> Pfft, like I give a fuck. Come here and see the sights!
20:10 < houst0n> Berlin would blow your mind. There are bars that don't open til 1am and you need arseless trousers to even imagine getting in
20:10 <@blastwave> between us and maybe a dozen others in the bitter end we did great things. I have been planning a trip to Europe for a long time. However I have to make choices ya know? Also ... this getting old thing, it really kicks in 
20:10 < houst0n> Well, I have a line to remko and martijn 
20:11 < houst0n> They don't hate me at least
20:11 <@blastwave> so to be really honest I move slow and think slow and drink slow and all very very steady and this is well with me 
20:11 <@blastwave> They were good people. Never had a problem with remko and his ego !! ha ha 
20:11 <@blastwave> that was long ago
20:11 < houst0n> remko is a dickhead
20:11 < houst0n> but a smart one
20:11 <@blastwave> ^ yep
20:11 < houst0n> and I owe him
20:12 < houst0n> he paid me to do bastwave shit
20:12 <@blastwave> that too ... as I say ... in the bitter end it was a few people doing crazy good stuff
20:12 < houst0n> so you owe him too
20:12 < houst0n> anyway
20:12 <@blastwave> well holy fuck ... now you tell me ? 
20:12 <@blastwave> you wait twenty years to drop that on me !! ha ha 
20:12 < houst0n> I'm sorry to pollute your twitch fanclub with nonsense
20:12 < houst0n> I'll fuck off for a few months
20:12 < houst0n> :P
20:13 <@blastwave> twitch fanclub. it is a drinking club lately 
20:13 <@blastwave> drop an email fer fucks sake
20:13 <@blastwave> it isn't like my email addr changes much ya know 
20:13 < houst0n> I swear there was a guy here earlier who said he's a paid prolog dev
20:14 < houst0n> and refused to even mention industry 
20:14 <@blastwave> I have no idea what that is .. or means. 
20:14 < houst0n> prolog?
20:14 <@blastwave> however Matthew does the really cool stuff
20:14 < houst0n> IT's a truely awful programming language
20:14 < racingmars> ha no I'm not the prolog guy
20:14 < houst0n> Butit's make believe
20:14 <@blastwave> I barely recall anything about it 
20:15 < racingmars> Someone was saying they work where Pascal is in use.
20:15 <@blastwave> FORTRAN77 man !
20:15 < houst0n> fortran is in use in CERN
20:15 <@blastwave> Pascal is awesome. Niclous Wirth for the win !
20:15 < houst0n> it's great for math
20:15 < houst0n> and intel's f compiler is insane balls fast
20:15 < racingmars> Yeah Fortran is still a thing for sure.
20:15 < houst0n> prolog tho? nah
20:15 <@blastwave> will likely be .... for a very very long time 
20:16 < houst0n> I work with legacy. Super legacy. Finance legacy. Z/Os. ibm MQ
20:16 < houst0n> No one uses prolog
20:16 < gbowne1> wasnt me.. I however still do F77 on the occasion
20:16 < racingmars> Oh, blastwave, my latest video series is complete:
20:16 < racingmars> https://www.youtube.com/watch?v=3mJLbJPn3t0
20:16 < racingmars> https://www.youtube.com/watch?v=6n0pZGwhMrY
20:16 < racingmars> https://www.youtube.com/watch?v=KrtD-hlXPOc
20:16 <@blastwave> okay Neil .... get some sleep. stay in touch. don't wait for a fucking year to say hello and saend a fucking email fer fucks sake !
20:17 < houst0n> I randomly find ADA, KSH, Eiffel.. Even fucking C
20:17 <@blastwave> oh ... ha ... my fireFox just blew up
20:17 < gbowne1> here we do not fuck C at all do we? xD
20:17 < racingmars> I'm glad you run nightly so we don't have to!
20:17 <@blastwave> yeah ... it just vanished in a puff of bits
20:17 < gbowne1> heh
20:18 < houst0n> I have a love hate with C that anyone born after 1990 won't understand]
20:18 <@blastwave> you just reminded me ... I want a Z80.
20:18 < houst0n> My orig copy of k&r's 2nd is n my mums house
20:18 < houst0n> I remember writing my own printf()
20:19 <@blastwave> the last computer I plan to buy will be something similar to the first machine I ever programmed. I do not think there are 8080 kits around 
20:19 < gbowne1> I mean I want a https://www.ebay.com/itm/395340937984 but that might not happen
20:19 <@blastwave> well ... what is that ? FireFox starts up ... go to the YouTube link from Matthew and then dies 
20:19 <@blastwave> I need to flush out my $HOME/.mozilla
20:20 < gbowne1> quick, Dennis, Fire zillas at it xD
20:20 < houst0n> Shit, these days? Focus on fonts
20:20 <@blastwave> speaking of fonts 
20:20 < houst0n> Berkeley mono or nothing
20:20 <@blastwave> anyone have the link to termingus ??
20:20 < houst0n> I paid $200 for the term font I use
20:21 < houst0n> And I regret nothing
20:21 <@blastwave> github.com:neutaaaaan/termingus
20:21 <@blastwave> ^ that 
20:21 <@blastwave> I use that everywhere I can 
20:21 < houst0n> https://berkeleygraphics.com/typefaces/berkeley-mono/
20:21 < houst0n> I have a 5k monitor
20:21 <@blastwave> I would not be able to see it
20:22 <@blastwave> what the fuck is a 5k monitor ?
20:22 <@blastwave> 4096x4096 ??
20:22 < houst0n> Nah
20:22 < racingmars> 5120 × 2880
20:22 <@blastwave> just gimme a line printer and a teletype.
20:22 < houst0n> Its what you get when you give apple like 2.5k
20:22 < houst0n> I dunno what the x*y is
20:23 < houst0n> But it's pretty
20:23 <@blastwave> if I can get Firefox to start up ... I will have to look at what the hell that is. but whyt would I want that? nope ....
20:23 <@blastwave> anything more than 1920x1080 is a waste with me 
20:23 < racingmars> 3 x 4k monitors on monitor arms does the trick for me here at my desk.
20:23 < houst0n> Ah shit I'm a clarity bitch. I like crisp text.... Fuck you 1080 is not usable
20:24 < racingmars> And yeah even after taking into account making all the font sizes bigger so they're readable on the 4k monitors, 1080p just doesn't have the real estate I've gotten used to.
20:24 < gbowne1> Give me a ADM-3a https://www.oetec.com/pastebin/plain/bvx9TUYQ xD
20:25 < houst0n> https://houst0n.net/retina.png
20:26 < houst0n> Okay, I have to get up at 5am to get brootchen
20:26 < houst0n> so, toodles
20:26 <@blastwave> well... I am in the dark ages here. One step away from a serial terminal and I have a yellow warning light on this machine also. so 
20:26 <@blastwave> houst0n: good stuff!
20:27  * blastwave ponders the whiskey
20:27 < houst0n> Aight bruv. You'l be here when I seek you out next?
20:27 < houst0n> Otherwise, dclarke@genunix.com ?
20:27 <@blastwave>  at blastwave.org  fer fucks sake
20:28 <@blastwave> or dc at genunix.com
20:28 < houst0n> or motherfucker@blastwave.org ?
20:28 <@blastwave> that works too !
20:28 < houst0n> What happened to purplecow?
20:28 <@blastwave> oh fuck man ... there is a story
20:28 <@blastwave> some other night ... go sleep. 
20:28 < houst0n> I've got a wee bit of whisky left
20:29 <@blastwave> suffice it to say that the purplecow was awesome and got slammed by Oracle also 
20:29 < houst0n> The purplecow dude ran a really enterpise mail stack
20:29 < houst0n> Stupidly so
20:29 <@blastwave> remember WeSunSolve.org ?
20:29 < houst0n> yep
20:29 <@blastwave> nuked by Oracle 
20:29 < houst0n> How could purplecow be nuked tho
20:30 <@blastwave> also yeah ... purplecow was on really big ass software. sadly all of it Oracle 
20:30 < houst0n> It was like an experiment how much enterprise shit you could run for free
20:30 <@blastwave> license costs and then other problems. support on the servers etc 
20:30 < houst0n> Oh? 10 users? HEREIS OPENDJ
20:31 < houst0n> I worked at a place who once had a massive incident and hired the australian who wrote opendj
20:31 <@blastwave> Oracle went after everyone everywhere to fucking scortch earth radiation nuke everyone 
20:31 < houst0n> fuck larry
20:31 < houst0n> I still like him more than elon
20:31 <@blastwave> when is the last time you tried to get a patch for a Sun server? Or an Oracle server?
20:32 < houst0n> Never, we don't use that stuff anymore
20:32 <@blastwave> we don't have enough whiskey for this topic 
20:32 < houst0n> What was that mental .pl script for patching solaris
20:32 < houst0n> some random dude maintained it for like 10 years
20:33 <@blastwave> yeah .. I recall that thing. that totally stopped working a long time ago. k ... I am going to rescue my firefox config here and 
20:33 < houst0n> Okay, I'm off. Closing IRC. Mabe I'll open it next year
20:33 < houst0n> Have a good new year dude
20:34 <@blastwave> right on ya wild scot !!
20:34 < houst0n> Shit
20:34 <@blastwave> watch out for Nessie
20:34 < houst0n> I'm tamed bitch
20:34 <@blastwave> I'm old
20:34 < houst0n> Me too
20:34 <@blastwave> shit happens
20:34 < houst0n> 38
20:34 < houst0n> :P
20:34 <@blastwave> y old fart
20:35 < houst0n> But at least I can write helloworld.c without #include <stdio.h> :P
20:35 < houst0n> night
20:36 -!- houst0n [~nh@dynamic-077-188-086-095.77.188.pool.telefonica.de] has quit [Quit: 42]
20:48 < MarianG> @houst0n you rock :D
20:52 < gbowne1> kernadian airspace.. somewhere https://www.twitch.tv/smellyspice
21:00 < hotzenbot> TIME: London 00:00, Paris 01:00, Kyiv: 02:00, Perth 08:00, Brisbane 10:00, Auckland 13:00, Irvine 16:00, Toronto 19:00
21:06 -!- merkuro [~merkuro@ip-037-201-213-211.um10.pools.vodafone-ip.de] has joined #blastwave
21:34 < rconjoe> @gbowne1 i watch LA airspace far too much. so entertaining
21:36 < gbowne1> yeah
21:37 < gbowne1> KSEA isnt that much fun these days
21:39 < gbowne1> much better during May-Aug
```
