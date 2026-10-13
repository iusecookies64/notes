Chapter 21: Hecke Operators and Hecke Forms
7:15:007 hours, 15 minutesdifferent. So far, modular forms were functions on the upper half plane. But once we write them as Q expansions uh
7:15:087 hours, 15 minutes, 8 secondslike this f to equals the sum of a and q to the n we got a sequence of numbers a
7:15:167 hours, 15 minutes, 16 secondsz a1 a2 the coefficients of uh the q the
7:15:237 hours, 15 minutes, 23 secondscoefficients of the powers of q in the q expansions of the modular form and mathematicians not there's something
7:15:307 hours, 15 minutes, 30 secondsinteresting for some very important modular forms these These coefficients are multiplicative. So multiplicative
7:15:397 hours, 15 minutes, 39 secondsmeans that uh to mn can be split up to to m to n for some co-prime m andn. For
7:15:467 hours, 15 minutes, 46 secondsexample, we have the mod discriminant here. Here uh the coefficients of q ^2=
7:15:537 hours, 15 minutes, 53 secondsminus4. I'll just write it as like the function like this. And the coefficients of q cq is 252.
7:16:037 hours, 16 minutes, 3 secondsSo if I multiply this together a2 a3 um
7:16:097 hours, 16 minutes, 9 secondstake out your calculator. So minus -4 * 252
7:16:167 hours, 16 minutes, 16 seconds= minus uh 6,048 - 648 is here. So it's a6.
7:16:257 hours, 16 minutes, 25 secondsUh maybe we try another one. So a3 time a4 a3 is 252
7:16:337 hours, 16 minutes, 33 secondsa4 is -472 and this is equals to 252
7:16:427 hours, 16 minutes, 42 seconds* 1472 this is equal to uh 370944
7:16:527 hours, 16 minutes, 52 seconds37944 we we found it here this is exactly a12 12. So why does this happen? Uh we don't
7:17:007 hours, 17 minutesknow. Uh we just assume that something very systematic is going on here. And on the other hand, uh modular forms, the
7:17:077 hours, 17 minutes, 7 secondsspace of modular forms and cost forms there were dimensional vector spaces. So we want to actually find good basis
7:17:157 hours, 17 minutes, 15 secondselements of those spaces explicitly. So we need some kind of tool to solve these problem I just mentioned and that is
7:17:227 hours, 17 minutes, 22 secondswhere hacker operator enters. Now let's pause for a moment and talk about multiplicative functions because this language will keep appearing when you
7:17:307 hours, 17 minutes, 30 secondstalk about for coefficients. So what is a multiplicative function? A function f that goes from natural numbers to
7:17:377 hours, 17 minutes, 37 secondscomplex numbers is multiplicative if f1= 1 and for any two co-prime integers m andn fn equals fm fn. So if f is a
7:17:477 hours, 17 minutes, 47 secondsmultiplicative function if you take like 12 this is equals to f_sub_3 f4 you can split like this.
7:17:567 hours, 17 minutes, 56 secondsSome examples of multiplicative functions are here. So sigma n sigma n is just a sum of divisors of n. So of
7:18:057 hours, 18 minutes, 5 secondscourse positive divisors of n. So for example sigma 6 equals to 1 + 2 + 3 + 6
7:18:137 hours, 18 minutes, 13 secondsto n is the number of divisors of n. So to six would be four because six has
7:18:197 hours, 18 minutes, 19 secondsfour divisors. And this fian this is called the orderer five function. It means the number of integers one to n
7:18:287 hours, 18 minutes, 28 secondsthat are relatively prime to n. So for example 5 12 the number between 1 to 12
7:18:367 hours, 18 minutes, 36 secondsthat are relatively prime to 12. So 1 2 3 now 4 5 6 7 8 9 10 11. So uh 52 = 4
7:18:487 hours, 18 minutes, 48 secondsand sigma kn is the sum of kth power of the positive divisor of n. So um 5k for
7:18:567 hours, 18 minutes, 56 secondsexample 6 would be 1 + 2 to the k + 3 to the k + 6k these are all multiplicative
7:19:047 hours, 19 minutes, 4 secondsfunctions and one nice property is that if f is multiplicative then gn defined using fn like this is also
7:19:127 hours, 19 minutes, 12 secondsmultiplicative so let's prove this so we want to prove that for any co-prime integers m andn n
7:19:237 hours, 19 minutes, 23 secondswe want to show that g mn is equals to gm gn. So let's look at g mn.
7:19:347 hours, 19 minutes, 34 secondsThis is the sum of fd where d is a positive divisor of mn. But if d is a
7:19:417 hours, 19 minutes, 41 secondspositive divisor of mn, we can write d equals d1 d2. for d1 is dividing m and
7:19:497 hours, 19 minutes, 49 secondsd2 dividing n because m and n are co-prime. So we can write uh d1 dividing
7:19:577 hours, 19 minutes, 57 secondsm d2 dividing n f d1 d2 but fd1 d2 equals fd1 fd2 because we know that d1
7:20:067 hours, 20 minutes, 6 secondsand d2 are co-prime since m and m are co-prime right and we will change the order of the sum
7:20:137 hours, 20 minutes, 13 secondslike this d2 dividing in fd1 fd2 and this is equals to we can take this
7:20:217 hours, 20 minutes, 21 secondsout right So d1 dividing m f d1 d2 dividing n f d2. See what we've got.
7:20:327 hours, 20 minutes, 32 secondsThis is fn.
7:20:367 hours, 20 minutes, 36 secondsSo we prove this formula. Now we can immediately use this to prove some of the examples above for multiplicative.
7:20:437 hours, 20 minutes, 43 secondsFor example, sigma n. We can write sigma n as the sum of these. Right? But
7:20:517 hours, 20 minutes, 51 secondsf_sub_x = x is obviously this is multiplicative right. Uh since this d is a multiplicative function automatically
7:20:597 hours, 20 minutes, 59 secondssigma n becomes multiplicative because of this formula. Uh same as to n to n we can write it like this. The sum
7:21:097 hours, 21 minutes, 9 secondsof one when you have a divisor. Uh since the constant function f_sub_1= 1 fnals 1 is obviously multiplicative to n is also
7:21:187 hours, 21 minutes, 18 secondsmultiplicative. And same with sigma n d to the power of k is multiplicative.
7:21:247 hours, 21 minutes, 24 secondsRight? If I define fn= n to the power of k of course mn equals f m fn. So uh sigma kn this is multiplicative.
7:21:357 hours, 21 minutes, 35 secondsSo finally we look at hack operators.
7:21:387 hours, 21 minutes, 38 secondsLet n be an integrated grad equal to one and let mn be the set of integral matrices abcd with determinant n. So a d
7:21:467 hours, 21 minutes, 46 secondsminus bc equals 1. The hacker operator of index n tn um the definition looks
7:21:537 hours, 21 minutes, 53 secondslike this. So tn applied to f equals n to the k / 2 - one sum and we sum all
7:22:017 hours, 22 minutes, 1 secondthese uh slash operators and uh now we look at this gamma 01/ mn. So what is this?
7:22:097 hours, 22 minutes, 9 secondsWe know that gamma 01 this is just equal to the full modular group specialar two group right. This means that we let this
7:22:177 hours, 22 minutes, 17 secondsgamma 01 aka special two group act on mn by left multiplication and then we look
7:22:247 hours, 22 minutes, 24 secondsat its orbits of this action in the sum we choose one representatives from each orbit and we add the sums. The important
7:22:337 hours, 22 minutes, 33 secondsfact about hacker operators is that if m is a modular form. So let f be a element of mk.
7:22:417 hours, 22 minutes, 41 secondsThen after applying the hacker operators this tnm is also in mk meaning that this
7:22:487 hours, 22 minutes, 48 secondsis also a modular form. So tn is a linear operator that goes from the space of modular forms to the space of modular
7:22:587 hours, 22 minutes, 58 secondsforms. So let's show this. So we pick one gamma from special linear group
7:23:057 hours, 23 minutes, 5 secondsand we want to show that TNF is again a modular form right. So we compute the
7:23:137 hours, 23 minutes, 13 secondsslash operator and we want to show that this is again equals to TNF.
7:23:197 hours, 23 minutes, 19 secondsSo TNF bar k gamma this is equals to by the
7:23:267 hours, 23 minutes, 26 secondsdefinition n k / 2 minus one and we uh look at each representatives of the
7:23:337 hours, 23 minutes, 33 secondsorbit gamma 01 such amn k mu
7:23:407 hours, 23 minutes, 40 secondsk gamma right but we know that this is equals to f k mu gamma right we prove
7:23:477 hours, 23 minutes, 47 secondsthis so n k with 2 - one sum f k mu gamma. But here uh look at
7:23:577 hours, 23 minutes, 57 secondswhat gamma is doing. Gamma is just reindexing the sum. Right?
7:24:017 hours, 24 minutes, 1 secondMultiplication by gamma sends mn to itself because gamma is determinant one.
7:24:067 hours, 24 minutes, 6 secondsSo the term fk mu gamma run through the same collection of f k mu.
7:24:167 hours, 24 minutes, 16 secondsTherefore uh we can write this like this and this is uh the definition of TNF
7:24:247 hours, 24 minutes, 24 secondsright so we prove that TNN is again a modular form of weight k so let's
7:24:307 hours, 24 minutes, 30 secondsrewrite the definitions of he operators so tnf
7:24:367 hours, 24 minutes, 36 secondsto this was equal to n k / 2 minus one sum
7:24:427 hours, 24 minutes, 42 secondsgamma 01 acting on Mn and we add far k gamma to.
7:24:527 hours, 24 minutes, 52 secondsNow this definition we just wrote down is correct. But if we actually want to compute this this is kind of uh painful and complicated because what are we
7:25:007 hours, 25 minutessupposed to do for every n find representatives in gamma zn acting on mn then apply the slash operate to each one and then add everything up. uh that's
7:25:097 hours, 25 minutes, 9 secondstechnically fine but it's not the way we want to calculate because usually when we use a modular form we look at its Q
7:25:167 hours, 25 minutes, 16 secondsexpansion right so instead of staring at these matrices we want to add more concrete questions what does TN do to
7:25:237 hours, 25 minutes, 23 secondsthe coefficients of the Q expansions and this is exactly what this formula tells us the new f coefficients of q to the h
7:25:327 hours, 25 minutes, 32 secondsis computed like this when he operatives is applied to f so Let's prove this formula. Before we do this, uh for this
7:25:417 hours, 25 minutes, 41 secondscomputation, we will use a standard set of representatives for the left gamma orbits in MN. So we will pick gamma from
7:25:497 hours, 25 minutes, 49 secondsthe set a b 0 d where a d equals n and b ranges from zero to uh t minus one.
7:26:027 hours, 26 minutes, 2 secondsOkay, so let's go. TNF towel this is equals to uh by the
7:26:127 hours, 26 minutes, 12 secondsdefinition of facialis and k / 2 minus one and a d should uh equal to n a d= n
7:26:217 hours, 26 minutes, 21 secondsand b ranges from 0 to d minus one and we are adding uh remember the slash operator notation so we had first
7:26:307 hours, 26 minutes, 30 secondsdeterminant determinant of the matrix equals a b and a D equals N. So N K / 2 and we had C to plus D, right? But C
7:26:397 hours, 26 minutes, 39 secondshere is zero. So we only have D to the power of minus K. And we have uh F gamma
7:26:477 hours, 26 minutes, 47 secondsto which is A to + B over C to plus B but C equals zero here. So it's D. And
7:26:547 hours, 26 minutes, 54 secondssince we know the Q expansions of F to let's use it to this calculation. So we
7:27:007 hours, 27 minuteshave n uh k minus one using this and we add 4 a d minus n and b ranges from 0 to
7:27:107 hours, 27 minutes, 10 secondsd minus one and we have d to the minus k
7:27:157 hours, 27 minutes, 15 secondsand we let m ranges from 0 to infinity
7:27:227 hours, 27 minutes, 22 secondsand we have a m q to the h but q was equal to e to the 2 pi I to right 2 pi
7:27:327 hours, 27 minutes, 32 secondsand this big thing acts as toao. So a toao + b over d and we also have m here.
7:27:407 hours, 27 minutes, 40 secondsAnd I want to um simplify this a bit. So we have n dk k minus one
7:27:487 hours, 27 minutes, 48 secondsuh a d = n b ranges from 0 to d minus one and you
7:27:557 hours, 27 minutes, 55 secondshave d to the minus k and we will take this out and we will change the order of the sum a little bit. So n k minus one a
7:28:057 hours, 28 minutes, 5 secondsd = n and we will take the sigma out. So m ranges from 0 to infinity
7:28:137 hours, 28 minutes, 13 secondsand we have d to the minus k and since we move to sigma here we can take this out. So a m uh q = to e to the 2 pi i
7:28:237 hours, 28 minutes, 23 secondsright. So this this thing is q to the
7:28:297 hours, 28 minutes, 29 secondspower of a over d m and we have b range from 0 to d minus one and we have e to
7:28:387 hours, 28 minutes, 38 secondsthe 2 pi i m over d b and now we want to focus on this. So we'll take this out.
7:28:507 hours, 28 minutes, 50 secondsSo we are summing when b ranges from 0 to d minus one e to
7:28:557 hours, 28 minutes, 55 secondsthe 2 pi i m over db and let's go case by case if d divides m what happens this
7:29:067 hours, 29 minutes, 6 secondsvalue uh this value is just one right so the the uh total sum equals d and how
7:29:127 hours, 29 minutes, 12 secondsabout d does not dividing m here we can put e to the 2 pi i m / d as z and what
7:29:217 hours, 29 minutes, 21 secondswe get this is a geometric sequence. So the sum will be just summing up the power the b
7:29:307 hours, 29 minutes, 30 secondspower of d which is uh using the formula z minus one first term first terms
7:29:367 hours, 29 minutes, 36 secondsequals zero so d 2 uh z to the d minus one but z to the d equals one right so
7:29:457 hours, 29 minutes, 45 secondsthis is zero so this means that we only have to consider the case where D divides M.
7:29:567 hours, 29 minutes, 56 secondsRight?
7:29:577 hours, 29 minutes, 57 secondsSo we will put M as J D for some integral J. So this becomes N to the K minus one.
7:30:077 hours, 30 minutes, 7 secondsA D = N. When M ranges from 0 to infinity, J also ranges from 0 to infinity. Right? So J ranges from 0 to
7:30:157 hours, 30 minutes, 15 secondsinfinity. D to the minus K A M but M equals J D
7:30:227 hours, 30 minutes, 22 secondsQ A over D M but A over D no M / D equals J right so this becomes AJ and
7:30:307 hours, 30 minutes, 30 secondsthis since we only consider the case where M is a multiple of D this becomes D so we uh uh we plus one here and we
7:30:407 hours, 30 minutes, 40 secondsalso will make a substitution we will put AJ equals H. So this becomes
7:30:487 hours, 30 minutes, 48 secondsuh when j r ranges from 0 to infinity h ranges from 0 to infinity. So h ranges from 0 to infinity and for j and d to
7:30:587 hours, 30 minutes, 58 secondsexist a should divide h and since a d here was n a should divide also n that means that
7:31:067 hours, 31 minutes, 6 secondsa should divide the gcd of n and h and we have uh d / n to the power of k
7:31:147 hours, 31 minutes, 14 secondsminus one and d over n is equals to one right so we have a to the k minus one
7:31:227 hours, 31 minutes, 22 secondsand we have A uh J D J J J J J J J J J J J J J J J J J J J J J equals A to the H uh A over H and D over A over N and we
7:31:317 hours, 31 minutes, 31 secondshave uh finally Q to the H. So we done this is the new full coefficients and if
7:31:407 hours, 31 minutes, 40 secondsI just uh change A to D, this becomes this formula. So we have proved this formula.
7:31:467 hours, 31 minutes, 46 secondsSo here are some main properties of the hack operators. The first and most general one is this multiplication
7:31:527 hours, 31 minutes, 52 secondsformula right here. So, TMTN equals um like this. Okay. Uh this formula can be
7:32:007 hours, 32 minutesproved from the Q expansion formula we just derived. There's not a clever trick in this proof. We know the formula for the coefficients of QTH in TNF, right?
7:32:107 hours, 32 minutes, 10 secondsSo, you apply that coefficients twice here. But like the proof cannot be that messy. So, I personally don't like it.
7:32:177 hours, 32 minutes, 17 secondsuh it's mostly bookkeeping with divisions. So for our purpose, it's not really the part we need to spend time on. So we will take this multiplication
7:32:257 hours, 32 minutes, 25 secondsformula as given. And from this formula, we will prove these three properties below. The first one says that TMTN
7:32:327 hours, 32 minutes, 32 secondsequals TNTM. What do we call this? We call this uh that the objects commute. And this is obvious from this formula.
7:32:427 hours, 32 minutes, 42 secondsTMTN equals TNTM. uh we change m and n and uh it stays the same. And about the
7:32:497 hours, 32 minutes, 49 secondssecond one, if gcd m and n equals 1, what is tmtn?
7:32:567 hours, 32 minutes, 56 secondsSo only possible values of c equals 1, right? So we put c equals 1 and we have tmn right from the formula. So tmtn
7:33:057 hours, 33 minutes, 5 secondsequals tmn if m&n or co-prime. And the third one, it's like a recurrence formula.
7:33:127 hours, 33 minutes, 12 secondsSo uh we will put m equals p to the r and n s p. So what do we get? T p to the
7:33:227 hours, 33 minutes, 22 secondsr tp equals the gcd of the two equals p.
7:33:277 hours, 33 minutes, 27 secondsSo the possible values of c will be one or either p. So let's put c equals 1 and
7:33:347 hours, 33 minutes, 34 secondsit becomes t p to the mn which is p to the r + one. uh plus when we put C uh S
7:33:427 hours, 33 minutes, 42 secondst P to the K minus one uh T MN / C ^ 2 =
7:33:497 hours, 33 minutes, 49 secondsP to the R -1 uh so we prove this formula and the last one we will not going to prove this but
7:33:587 hours, 33 minutes, 58 secondshe put it self join with respect to the Peterson inner product meaning that the Peterson inner product of T and F and G
7:34:057 hours, 34 minutes, 5 secondsis equal to F and TNG and spora a lot. A bit later we'll use this uh compativity
7:34:137 hours, 34 minutes, 13 secondsproperty together with the self adjoiners to show something really cool.
7:34:177 hours, 34 minutes, 17 secondsAnd those two words should sound familiar from linear algebra.
7:34:227 hours, 34 minutes, 22 secondsRemember each hacker operatives TN was a linear operators on the space of modular forms. So once we have these operators
7:34:307 hours, 34 minutes, 30 secondsthe natural thing we can ask is can we find igen vectors of these operators and that's exactly what hack form is and he
7:34:387 hours, 34 minutes, 38 secondsform is a modular form that is an igen vector for every hacky operators tn all at once and this is the surprising part
7:34:467 hours, 34 minutes, 46 secondswe are not saying that f is an igen vector for just one operators like t2 or for a few selected operators we asking
7:34:547 hours, 34 minutes, 54 secondsfor something much stronger for every n greater or equal to on uh the operator tns sends f back to the scalar
7:35:027 hours, 35 minutes, 2 secondsmultiplication by itself and that is a very rigid and strong condition because a random modular form will not usually behave this nicely under all hacker
7:35:107 hours, 35 minutes, 10 secondsoperators at the same time and that is a very rigid and strong condition because a random modular form will not usually
7:35:187 hours, 35 minutes, 18 secondsbehave this nicely under all hacker operators at the same time. But the forms that do satisfies this condition are exactly the ones we want to focus on
7:35:277 hours, 35 minutes, 27 secondsand they are called hacker operators or hacky forms. And hacker form is that to be normalized if its first coefficients
7:35:347 hours, 35 minutes, 34 secondsequals one. And for a normalized hacker form the value is the nth coefficients.
7:35:407 hours, 35 minutes, 40 secondsUh so a n uh this is because if f to
7:35:477 hours, 35 minutes, 47 secondslooks something like this a to the h q to the h then the q1 coefficients of uh
7:35:577 hours, 35 minutes, 57 secondstnf will be how do we compute this we have the formula so d dividing n h and d
7:36:057 hours, 36 minutes, 5 secondsto k minus one a nh over d². So, so if
7:36:127 hours, 36 minutes, 12 secondswe put h here, the only possible values of d = 1. So, this becomes uh 1 to the k
7:36:207 hours, 36 minutes, 20 secondsminus one a n and 1 / d². So, this is just a1.
7:36:277 hours, 36 minutes, 27 secondsBut since f is a heck form, we also have uh tnf equals lambda f. And comparing
7:36:347 hours, 36 minutes, 34 secondsthe QT1 coefficients of each side, we have lambda equals A1. And comparing the
7:36:417 hours, 36 minutes, 41 secondsQ coefficients on each side, this gives a N equals lambda A1. But since F is
7:36:487 hours, 36 minutes, 48 secondsnormalized, if A1= N, uh, lambda becomes a N. So from now on, we will usually be looking at only normalized HK forms. Now
7:36:587 hours, 36 minutes, 58 secondswe can finally see why Hackey forms are so useful. From the properties of hacker operators, we can prove that the fier coefficients of a normalized hacker form satisfy multiplicative relations.
7:37:107 hours, 37 minutes, 10 secondsBecause if f is a normalized hack form, we have t mn equals tmtn
7:37:187 hours, 37 minutes, 18 secondsfor the co-prime integers mn. Right? And we applied these to
7:37:237 hours, 37 minutes, 23 secondsF which becomes TM TNF. And TMNF equals
7:37:297 hours, 37 minutes, 29 secondsA MNF. And this TMTNF equals TM
7:37:367 hours, 37 minutes, 36 secondsANF. And we can take the AN out. So this becomes a N TMF. And this is equals to AMF.
7:37:467 hours, 37 minutes, 46 secondsUh so AMN equals AM. So we prove that the fur coefficients of heer operators are multiplicative.
7:37:557 hours, 37 minutes, 55 secondsSo earlier we said that the coefficients of many modular forms are multiplicative. But now we see what's going on. Those modular forms we looked
7:38:037 hours, 38 minutes, 3 secondsat are actually special one called the heck forms. And there's also a second relation for prime powers. Earlier we
7:38:107 hours, 38 minutes, 10 secondssaw that the heck operators uh had this recurrence P TTR + one equals TP
7:38:197 hours, 38 minutes, 19 secondsTPK TPT R minus P DK minus one TP to the R
7:38:297 hours, 38 minutes, 29 secondsminus one and and similarly if we apply this to F on both sides we easily get this
7:38:367 hours, 38 minutes, 36 secondsrecurrence formula for for coefficients of HF forms. So far we have talked about hecker forms and honestly the condition
7:38:447 hours, 38 minutes, 44 secondsfor being a hecker form was pretty strong. A hecker form has to be an igen vectors for all hacker operators tn at the same time and simultaneous
7:38:537 hours, 38 minutes, 53 secondsdiagonalization is not something that happens for easily. So at this point we might wonder do we actually have examples of hacker forms and the answer
7:39:027 hours, 39 minutes, 2 secondsis yes. The eisenstein series which we already know quite well by now turns out to be a hacker form. So let's show that
7:39:097 hours, 39 minutes, 9 secondsthe Eenstein series is a hecker form. So we want to show that for any end key EK
7:39:177 hours, 39 minutes, 17 secondsequals lambda EK and if you see and if you see the Eisenstein series there's a constant one
7:39:267 hours, 39 minutes, 26 secondsin this uh multiplied factors on the front but that constant uh we can just think that it will be carried along. So
7:39:347 hours, 39 minutes, 34 secondsit's not the main part here. It's not the main issue. you can think that it will match correctly. So we want to show
7:39:417 hours, 39 minutes, 41 secondsthat so we will show that these part of the Eenstein series is a heck form
7:39:487 hours, 39 minutes, 48 secondsthat's enough. So we have the formula TNF this was equals to
7:39:577 hours, 39 minutes, 57 secondsso we have this coefficients formula and here I will define f to
7:40:037 hours, 40 minutes, 3 secondsas the sum of uh sigma k minus one h q to the h when h ranges
7:40:127 hours, 40 minutes, 12 secondsfrom one to infinity and we will show that this f is a heer form and here let's look get the coefficients of Q to
7:40:227 hours, 40 minutes, 22 secondsthe H of uh TNF and by the formula this
7:40:277 hours, 40 minutes, 27 secondsis equals to D / N H D to the K minus
7:40:357 hours, 40 minutes, 35 secondsone sigma K minus one NH over D² and remember this was the coefficients
7:40:427 hours, 40 minutes, 42 secondsof QTH of TNF right so we want this to be some lambda multiple of sigma k minus
7:40:507 hours, 40 minutes, 50 secondsone h and actually we will show something stronger we will show that um
7:41:027 hours, 41 minutes, 2 secondsuh this is much stronger than this one and if we show this one this one is automatically proved so it's enough to
7:41:097 hours, 41 minutes, 9 secondsshow that this equation holds so we want to show that this holds for all n and h and from this expression
7:41:187 hours, 41 minutes, 18 secondsdiscussion we can see that both sides are multiplicative in the pair and h so both sides are multiplicative in pair n
7:41:277 hours, 41 minutes, 27 secondscomma h and so I will explain the term pair multiplicative here briefly um if f is a
7:41:367 hours, 41 minutes, 36 secondstwo variable functions for n and h and if f n1 n2 h1 h2 can speak to f n1 h1 f
7:41:467 hours, 41 minutes, 46 secondsn2 N2 H2 whenever N on H1 and N to H2 or co-prime we call that F is pair
7:41:557 hours, 41 minutes, 55 secondsmultiplicative and here the right hand side and left hand side is both pair multiplicative because for the right side this is clear
7:42:037 hours, 42 minutes, 3 secondsbecause the sigma K we know that it's already multiplicative and for the left side um remember the basic fact we saw
7:42:127 hours, 42 minutes, 12 secondsearlier if F is multiplicative uh D dividing NFD is also multip duplicated for n. And this is basically the same
7:42:197 hours, 42 minutes, 19 secondsidea but now with two variables. So this means that it's enough to check the identity for n= pda and h= ptdb because
7:42:307 hours, 42 minutes, 30 secondsif we look at any paramult k function fn comma h uh n and h can be factorized
7:42:377 hours, 42 minutes, 37 secondsinto the product of prime. So P1 alpha 1 P2 alpha 2 BA P and alpha N H can be
7:42:457 hours, 42 minutes, 45 secondsalso factorized P1 beta 1 P2 beta 2 P N beta N and since F is pair
7:42:537 hours, 42 minutes, 53 secondsmultiplicative this is equal to the product of F u P I alpha I F pi beta I.
7:43:027 hours, 43 minutes, 2 secondsSo we can only show that uh the two are the same for n being the power of prime p and h also
7:43:117 hours, 43 minutes, 11 secondsbeing the power of prime. This means that it's enough to check the identity when n equals p to the and h equals p to
7:43:187 hours, 43 minutes, 18 secondsb. And without loss of generality we'll put b greater or equal than a. So
7:43:267 hours, 43 minutes, 26 secondsif we look at the left hand side we have d dividing the gcd of n and h
7:43:337 hours, 43 minutes, 33 secondsright the gcd is p to the a uh so I'll put d equals p to the j so j r ranges
7:43:417 hours, 43 minutes, 41 secondsfrom zero to a and we have d to the k right d to the k equals p to the j k and
7:43:497 hours, 43 minutes, 49 secondsI'll just change this uh to uh j r bring r from zero to a and we have sigma k
7:43:597 hours, 43 minutes, 59 secondsa + b minus 2j okay and if we uh compute
7:44:077 hours, 44 minutes, 7 secondsthis explicitly so j r ranges from 0 to a p to the j k
7:44:157 hours, 44 minutes, 15 secondsand this is the geometric series and the denominator uh the common ratio will be p to the k and the first term will be
7:44:237 hours, 44 minutes, 23 secondsone and for the numerator we will have p a + b minus 2 j + 1 because we have a +
7:44:327 hours, 44 minutes, 32 secondsb - 2 j + 1 number of terms and multiply k and minus one
7:44:417 hours, 44 minutes, 41 secondsand this will be something like uh first of all we'll put this out so one over p to the k minus one sum
7:44:517 hours, 44 minutes, 51 secondsp to the a + b minus j + 1 k minus p to
7:44:587 hours, 44 minutes, 58 secondsthe j k and j r ranges from zero to a and this is equal to
7:45:087 hours, 45 minutes, 8 secondsuh we'll first compute this sum and this is a geometric series and the common ratio will be ptk
7:45:157 hours, 45 minutes, 15 secondsand um I will so I'm adding up this reversely meaning that uh if we have 27 931 this kind of geometric series we will uh add in this direction. Okay.
7:45:267 hours, 45 minutes, 26 secondsSo the first term here will be if we put a this will become p to the b + one k
7:45:347 hours, 45 minutes, 34 secondsand we have a total of a + one terms right so we have p to the a + 1 k minus
7:45:417 hours, 45 minutes, 41 secondsone and how about this uh this is easy the common ratio p to the k and the first term we have one and the last term
7:45:507 hours, 45 minutes, 50 secondsoh no the number of term equals a + 1 so a + 1 k minus one and this is equals to
7:45:587 hours, 45 minutes, 58 secondsum so these two are common right so if we take this out this becomes uh p to the a
7:46:067 hours, 46 minutes, 6 seconds+ 1 k -1 uh k minus one p to the b + 1 k minus
7:46:147 hours, 46 minutes, 14 secondsone b + 1 k minus one and this is sigma k
7:46:237 hours, 46 minutes, 23 secondsp to the a which is sigma K N and this is sigma K
7:46:317 hours, 46 minutes, 31 secondsto the H. So we prove that the Einstein series is a heck form. And the really nice thing about hek form is that the
7:46:397 hours, 46 minutes, 39 secondsspace of modular forms has a basis consisting of normalized heek forms. So why is this? Let's let's prove this. Um
7:46:477 hours, 46 minutes, 47 secondswe know that modular form can be decomposed into eenstein series and the space of cost form. So C k uh O plus
7:46:577 hours, 46 minutes, 57 secondsthe space of cus forms and we just proved that the Einstein series is a heck form. So it's enough to prove that
7:47:047 hours, 47 minutes, 4 secondsthe basis of cusp forms are heck forms and this is where the Peterson inner product becomes useful. Uh we showed
7:47:127 hours, 47 minutes, 12 secondsthat TNT is equal to TMTN.
7:47:187 hours, 47 minutes, 18 secondsSo they commute each other and we also saw that the heck operators uh was self
7:47:267 hours, 47 minutes, 26 secondsfor join with respect to the Peterson inner product meaning that these two are the same. So from these two we can use
7:47:347 hours, 47 minutes, 34 secondsthe spectral theorem we saw in linear algebra. So that means that there is a basis of sk consisting of vectors that
7:47:427 hours, 47 minutes, 42 secondsare igen vectors for every hack of purchase tn at the same time. But that's exactly what hack form is. So we got a
7:47:497 hours, 47 minutes, 49 secondsbasis of SK made of hack forms. And since this EKenstein series is also a he form putting the st series part together
7:47:577 hours, 47 minutes, 57 secondswith the cost form gives a basis of MK consisting of he forms. So at this point it feels like he forms contains a lot of
7:48:067 hours, 48 minutes, 6 secondsinformations about modular forms. It forms a basis for modular forms. So can we do something more with these hacker
7:48:137 hours, 48 minutes, 13 secondsforms? Can we take these hacker forms uh play with them a little bit process them somehow and build a new mathematical object out of them? If we do that maybe
7:48:227 hours, 48 minutes, 22 secondswe can get something that captures the core of modular forms.
