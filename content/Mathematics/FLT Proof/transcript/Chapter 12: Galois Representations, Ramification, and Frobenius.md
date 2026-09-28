Chapter 12: Galois Representations, Ramification, and Frobenius
4:37:334 hours, 37 minutes, 33 secondswas too large and complicated for us to understand directly. It's not like uh G q2
4:37:424 hours, 37 minutes, 42 secondsover Q. It's not like this true and we can just list the elements see what they do. This only had two elements in it. So if we try to stare at the whole group
4:37:514 hours, 37 minutes, 51 secondsdirectly, it's almost impossible to get a clear picture. So instead we do something more practical. We let G act on a more concrete object and we see
4:38:004 hours, 38 minuteswhat happens. You can see of this as taking a shadow of a huge object. The original object is too complicated to see directly. But if it casts a shadow
4:38:084 hours, 38 minutes, 8 secondsonto something more manageable, then we can study the shadow. In this case, the manageable object is usually a module.
4:38:164 hours, 38 minutes, 16 secondsSo let M be a R module. A gala representation is a homorphism that takes one element from the absolute gala
4:38:234 hours, 38 minutes, 23 secondsgroup and sends this to a automorphism group of M. This means that for every element sigma in G, we assign an R
4:38:324 hours, 38 minutes, 32 secondsmodule automorphism. So row is a automorphism. So we send sigma to row.
4:38:394 hours, 38 minutes, 39 secondsSo sigma itself originally acts on algebraic numbers, right? Because sigma was an element of absolute group. But through the representation we have sigma
4:38:484 hours, 38 minutes, 48 secondsact on module m and sigma goes to row and row is a element of this automorphism group. Um that's why this is so useful. We are translating the
4:38:574 hours, 38 minutes, 57 secondsaction of the huge group the absolute group into automorphisms of a more concrete algebraic object. And if m is
4:39:044 hours, 39 minutes, 4 secondsfree of rank two meaning that uh the basis of m equals two then after choosing a basis uh this happens. This
4:39:134 hours, 39 minutes, 13 secondsis because uh if M is free of rank two, this means that M is isomeorphic to R squar, right? So
4:39:224 hours, 39 minutes, 22 secondsGQ goes to automorphism R and this is isomorphic to automorphism R². And what's this?
4:39:324 hours, 39 minutes, 32 secondsThis is isomeorphic to generally new group.
4:39:374 hours, 39 minutes, 37 secondsThis is the point where the absolute galo action becomes useful because this absolute glo group this was so hard and complicated to uh examine. But this g
4:39:464 hours, 39 minutes, 46 secondsrepresentation transform one element from GQ to a matrix that we well know.
4:39:534 hours, 39 minutes, 53 secondsSo that is the basic idea of gal representation.
4:39:574 hours, 39 minutes, 57 secondsFor this slide we do not need to spend much time. I just want you to know that there is a notion of isomeorphic gal representation. We will see this kind of
4:40:064 hours, 40 minutes, 6 secondslanguage later but we're not going to use the definition in any serious way right now. So you can think of a slide as a piece of terminology. Just as
4:40:144 hours, 40 minutes, 14 secondsmatrices representing linear transformations can change when we change the basis glo representation can also be considered the same up to an
4:40:214 hours, 40 minutes, 21 secondsappropriate change of basis. Uh from now I'll just read the definition and we'll move on. So two g representation row and
4:40:284 hours, 40 minutes, 28 secondsrow two are set to be isomorphic. Uh we write like this. if that exists an invertible matrices P such that uh this
4:40:384 hours, 40 minutes, 38 secondsholds. So this is very similar to what we define for a similar matrices. Now I just want to introduce one more word
4:40:454 hours, 40 minutes, 45 secondsthat will appear later and that is irreducible g representation. A g representation is called irreducible if
4:40:524 hours, 40 minutes, 52 secondsit cannot be broken into a smaller representation acting on a proper subspace. More precisely, a
4:40:594 hours, 40 minutes, 59 secondsrepresentation is irreducible if that if the vector space V contains no non-trivial subspaces that are stable
4:41:064 hours, 41 minutes, 6 secondsunder the action of all transformation in the image of V. So the word irreducible here means that the representation cannot be decomposed into
4:41:164 hours, 41 minutes, 16 secondsa smaller stable piece. Um you don't need to digest this perfectly and I do not expect you to just uh you you just need to know that we can define
4:41:244 hours, 41 minutes, 24 secondsirreducibility of a car representation for now that's all we need in later we could when we talked about st conjecture
4:41:314 hours, 41 minutes, 31 secondsand rub theorem the word irreducible will appear as one of the required condition and that's why I'm introducing this right now
4:41:394 hours, 41 minutes, 39 secondsfrom here we need to introduce some slightly different ideas because we want to talk about uh something called a ramification these idea will be used
4:41:484 hours, 41 minutes, 48 secondslater but we will not use them too deeply. So if this part feels hard, do not get stuck on every detail. For now, it's enough to know that the rough
4:41:564 hours, 41 minutes, 56 secondspicture in mind. Um in field extension and go representation, we can ask what happens at each prime. If a prime is
4:42:044 hours, 42 minutes, 4 secondsunrammified, uh it means that uh it's a good case. It behaves cleanly. Uh but if a prime is ramified, then it's a bad
4:42:114 hours, 42 minutes, 11 secondscase. Something more complicated is happening here. And we don't want ramification to be happening. I will only give a very shallow definition. I
4:42:194 hours, 42 minutes, 19 secondswill not go much deeper than that. Just uh just try to keep in mind that ramification is about detecting which primes behaves badly. In the ordinary
4:42:284 hours, 42 minutes, 28 secondsintegers, a prime numbers are the basic building blocks. For example, if you take any number, for example, 12 = 2^ 2 * 3.
4:42:384 hours, 42 minutes, 38 secondsuh but when we move from a Q to a larger field K the ordinary rational primes or
4:42:454 hours, 42 minutes, 45 secondsthe prime that we are familiar of 2357 can behave in new ways. So let K over Q be a field extension and let OK K be its
4:42:544 hours, 42 minutes, 54 secondsring of integers. uh these ring of integers. This is a set of alphas
4:43:024 hours, 43 minutes, 2 secondsthat satisfies a monic polomial uh with
4:43:104 hours, 43 minutes, 10 secondsinteger coefficients. You can think of okay k as the analog of the inside number field k. Now take an rational
4:43:184 hours, 43 minutes, 18 secondsnumber or just just prime number P and inside okay we'll look at the ideal P. This ideal may no longer remain prime.
4:43:274 hours, 43 minutes, 27 secondsInstead effect vectors into prime ideals in okay uh like this here pi to PJ are the prime ideals of okay and the
4:43:354 hours, 43 minutes, 35 secondsexponent EI we call the ramification index. So the rational prime P may split into several prime ideals and some of
4:43:434 hours, 43 minutes, 43 secondsthem may appear with multiplicity. For example, if P factors into something like P1 P2 cub P3
4:43:544 hours, 43 minutes, 54 secondsuh squared blah blah blah, we have multiplicity here. The exponent is greater than one. And that multiplicity
4:44:014 hours, 44 minutes, 1 secondwe call it ramification. If every exponent uh is one, for example, if p is the form of something like uh p1, p2,
4:44:104 hours, 44 minutes, 10 secondsp3, all the exponents one, then p is unrammified in this extension. But if at least one exponent is bigger than one,
4:44:184 hours, 44 minutes, 18 secondslike in this situation, then we say p is ramified in k. Uh let's look at some
4:44:254 hours, 44 minutes, 25 secondsexamples. If we take k as qi, what is the ring of integers? The ring of integer equals zi. And here if we take
4:44:344 hours, 44 minutes, 34 secondsprime number p, what happens at 3 k uh 3
4:44:394 hours, 44 minutes, 39 secondsk is a prime. However, if you take p = 2 k these are collections of the numbers
4:44:484 hours, 44 minutes, 48 secondsof the form 2 a + 2 b i and this actually factors into the square of this
4:44:574 hours, 44 minutes, 57 secondsprime ideal. So we have a index greater than one. So we say 2 is ramified in k.
4:45:064 hours, 45 minutes, 6 secondsIf we take p= 5, five k factors into uh the ideal
4:45:144 hours, 45 minutes, 14 secondsgenerated by 2 plus i and the ideal generated by 2 minus i. So here five is not ramified because the index are all
4:45:224 hours, 45 minutes, 22 secondsone. Uh another example if we take K as uh Q2
4:45:294 hours, 45 minutes, 29 secondsokay will be Z 2 and if we take P = 2
4:45:374 hours, 45 minutes, 37 seconds2 okay factors into the ideal generated by two
4:45:434 hours, 45 minutes, 43 secondsuh a square so P equals 2. So two may be a prime number in rational numbers. But
4:45:494 hours, 45 minutes, 49 secondsif we take two to the field of K, we say that two is ramified in K.
4:45:574 hours, 45 minutes, 57 secondsThese are some concepts we need in order to define ramification. Not only for a field extension we just saw but also for
4:46:034 hours, 46 minutes, 3 secondsG representation. So let K over Q be a G extension and let uh P be a prime ideal
4:46:114 hours, 46 minutes, 11 secondsof OK lying over P. So what does it mean by lying over P? It means that P appears
4:46:194 hours, 46 minutes, 19 secondsin the factorization of P or K. It's equivalent to saying that the intersection of prime ideal and Z equals
4:46:284 hours, 46 minutes, 28 secondsthe multiple of P PZ. Now since K over Q is Glo the Glo group K over Q acts on K
4:46:364 hours, 46 minutes, 36 secondsand in fact it also acts on the prime ideals of OK K. So if we take one element sigma from the scala group, this
4:46:444 hours, 46 minutes, 44 secondssends one prime ideal P to another prime ideal P prime lying over the same P. But
4:46:514 hours, 46 minutes, 51 secondssome automorphisms preserve this particular prime ideal which means that this sends the prime ideal to the exactly same prime ideal and these
4:47:004 hours, 47 minutesautomorphisms form the decomposition groups at P. So we define this decomposition group as the collection of
4:47:064 hours, 47 minutes, 6 secondssigma that preserves P. So this decomposition group DP is a subgroup of the glo group that keeps the chosen
4:47:144 hours, 47 minutes, 14 secondsprime prime ideal fixed. Now why do you care about such subgroup? Because if sigma keeps p fixed then sigma acts
4:47:234 hours, 47 minutes, 23 secondsnaturally on the quotient okay over p okay mod p and since p lies over p the
4:47:314 hours, 47 minutes, 31 secondsresidue field contains the finite field z mod pz. So this field we can see it as a extension field of Z mod PZ. So the
4:47:404 hours, 47 minutes, 40 secondselement in the de composition group gives a natural homorphism that goes to this scholar group. Uh how we send uh
4:47:484 hours, 47 minutes, 48 secondssigma from DP to a sigma prime in this scholar group.
4:47:564 hours, 47 minutes, 56 secondsWe send sigma to sigma. So how do we define sigma prime? We define very naturally sigma prime x + p.
4:48:084 hours, 48 minutes, 8 secondsWe define it as sigma x plus p. And the inertia group at this
4:48:164 hours, 48 minutes, 16 secondsprime ideal we define as the kernel of this homorphism. Meaning that all the
4:48:224 hours, 48 minutes, 22 secondsset of sigma that satisfies sigma x equals x modulo p for all x in k. We
4:48:304 hours, 48 minutes, 30 secondshave just defined the inertia group in the field extension setting. The inertia group measures what happens locally at a prime. Now we transfer that language to
4:48:384 hours, 48 minutes, 38 secondsGrow representation. What does our representation row to the IP? Now since row sends elements of the absolute gar
4:48:464 hours, 48 minutes, 46 secondsgroup to matrices, right? Row was a G representation. Every element sigma in IP, this sigma gets sent to a matrix row
4:48:564 hours, 48 minutes, 56 secondssigma and this is in general linear group three. And here if every element of the inertia group is sent to the
4:49:044 hours, 49 minutes, 4 secondsidentity matrix like this then the representation then the representation does not detect any inertia at P. In
4:49:124 hours, 49 minutes, 12 secondsthat case we call it row is unrammified at P and if not we say that row is ramified at P. So this is definitely the
4:49:214 hours, 49 minutes, 21 secondsmost technical definitions in this lecture. So if you don't get all these decompositions or whatever that's okay.
4:49:274 hours, 49 minutes, 27 secondsUm you can think of ramification as bad behavior and un ramification as good behavior and we don't want ramification to be happen at primes.
4:49:364 hours, 49 minutes, 36 secondsNow we define the arting conductor of a representation. The RT conductor and row of a representation row is a positive
4:49:444 hours, 49 minutes, 44 secondsintegral that precisely measures this ramification. And we define like this uh the product of L all L to the NL row.
4:49:524 hours, 49 minutes, 52 secondsThis NL row depends on the structure of the ramification at L. If row is
4:49:594 hours, 49 minutes, 59 secondsunrammified at L, if row is unrammified at L, NL, row equals zero. So L does not
4:50:094 hours, 50 minutes, 9 secondsdo anything to N row. But if row is ramified at L then L does appears in the conductor. Meaning that if N is
4:50:174 hours, 50 minutes, 17 secondsdivisible by L, it's ramified by L. So N row is the in that packages the ramification data of the representation.
4:50:244 hours, 50 minutes, 24 secondsIt tells us where the representation is ramified and how seriously it's ramified at each time. For examples, um let's say
4:50:324 hours, 50 minutes, 32 secondsthe ramification uh index aring conductor of some G representation is AD
4:50:384 hours, 50 minutes, 38 secondsand AD is 2 to the 4th * 5. So other than 2 and 5, we know that it's fine
4:50:464 hours, 50 minutes, 46 secondsmeaning that it's unrammified. For example, if I take prime 37, 37 is unrammified at row. We know this because
4:50:534 hours, 50 minutes, 53 secondsuh we should only check the prime that divides the RT conductor. And we know that two something very bad is happening
4:51:014 hours, 51 minutes, 1 secondbecause the uh the NL is four right it means that it's very badly ramified and at five uh we know that it's ramified
4:51:094 hours, 51 minutes, 9 secondsbut it's not as bad as uh two now we look at fenuous element for a final field FPDF
4:51:184 hours, 51 minutes, 18 secondsthis map is a field automorphism and this is called the fenous automorphisms uh first of all why is this an
4:51:254 hours, 51 minutes, 25 secondsautomorphism uh Let's see uh before we start this FPF this has characteristic
4:51:354 hours, 51 minutes, 35 secondsuh P let's just take that as given um we want to show that this is also a homorphism right so we want to show that
4:51:444 hours, 51 minutes, 44 secondsthis a + b p equals to modulo a to the p plus b to the p modular p and we also
4:51:524 hours, 51 minutes, 52 secondswant to show that the p power of ab is equal to a to P BTDP modulo P uh right
4:52:014 hours, 52 minutes, 1 secondoff the bat we know that this holds right but this is the problem. So why does this hold?
4:52:084 hours, 52 minutes, 8 secondsIf we extend this what happens? So we have P 0 A P B 0 plus P C1 A P minus one
4:52:194 hours, 52 minutes, 19 secondsB1 plus blah blah blah P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P P - one A1 B P
4:52:274 hours, 52 minutes, 27 secondsminus one plus uh the last time P A 0 B P um notice that these are all multiples
4:52:364 hours, 52 minutes, 36 secondsof B because PC1 PC2 all the way up to through P CP minus A is P C P minus one
4:52:434 hours, 52 minutes, 43 secondsis a multiple of P. So we look at only these two terms which is ATP plus BTP.
4:52:524 hours, 52 minutes, 52 secondsSo this is uh same as ATP plus BTP modulo M modul P. Now knowing this
4:53:004 hours, 53 minutesforous automorphism let K over Q be a GO extension and let P be a prime ideal of
4:53:074 hours, 53 minutes, 7 secondsP. So knowing this let k over q be a go extension at p be b be a prime ideal uh above p. This means that it's lying over
4:53:164 hours, 53 minutes, 16 secondsP. And if P is unromified in this extension, then something very nice happens. The Fenaneous automorphism on
4:53:234 hours, 53 minutes, 23 secondsthe residue field can be lifted to an element of a Galwa group K over Q. And
4:53:304 hours, 53 minutes, 30 secondsthis element, this element is particularly called the froenous elements at the prime ideal P. And we
4:53:374 hours, 53 minutes, 37 secondswrite uh like this P. uh the defining property is that after reducing modular P it acts just like the probenius
4:53:454 hours, 53 minutes, 45 secondsautomorphism. So this probenius element is a glo automorphism upstairs but when we look at downstairs on the residue
4:53:524 hours, 53 minutes, 52 secondsfield it becomes the familiar fraenous automorphism which is uh this for our purpose we will not need to go deeply
4:54:004 hours, 54 minutesinto this uh just remember that there is a special element of the glo which is related to a fraenous automorphism.
