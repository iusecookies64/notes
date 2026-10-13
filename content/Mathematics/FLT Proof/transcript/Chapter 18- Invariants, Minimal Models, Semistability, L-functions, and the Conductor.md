Chapter 18: Invariants, Minimal Models, Semistability, L-functions, and the Conductor
6:18:226 hours, 18 minutes, 22 secondsNow we move on to a slightly different topic. We are going to introduce a few basic invariants of an elliptic curve.
6:18:296 hours, 18 minutes, 29 secondsSo let's look at E as a shortf equation. So y² = xq + ax + b.
6:18:386 hours, 18 minutes, 38 secondsFirst the determinant is defined as -6
6:18:446 hours, 18 minutes, 44 seconds4 a cub + 27 b 2. This determines whether if the curve is smooth or not.
6:18:516 hours, 18 minutes, 51 secondsSo if this value is zero, it means that the curve is singular. And if this is non zero, it means that the curve is smooth. And J invariant J invariant is
6:19:006 hours, 19 minutesdefined as C4 cube over the discriminant. And C4 here is uh minus 48
6:19:096 hours, 19 minutes, 9 secondsA. So if you compute this it looks like something like 1728
6:19:156 hours, 19 minutes, 15 seconds4 a 4 a cube and the denominator
6:19:206 hours, 19 minutes, 20 seconds4 a cub + 27 b² and over the algebraic closure two elliptic curves are
6:19:286 hours, 19 minutes, 28 secondsisomorphic if and only if they have the same j invariant. So the j invariant is like an ID number for an elliptic curve.
6:19:366 hours, 19 minutes, 36 secondsThere is one more useful thing that we can do with the discriminant. The discriminant does not only tells us whether the original curve is smooth. It
6:19:446 hours, 19 minutes, 44 secondsalso helps us understand what happens after reducing the curve modul prime P.
6:19:506 hours, 19 minutes, 50 secondsSo let E be an elliptic curve defined over Q. And we choose P greater or equal to five prime number. And to determine
6:19:596 hours, 19 minutes, 59 secondsthe reduction type of E, we consider a minimum vi equation. And we will learn this later. So uh if the periodic
6:20:066 hours, 20 minutes, 6 secondsvaluation of the discriminant equals zero, it means that E has good reduction at P. And if the periodic valuation is
6:20:146 hours, 20 minutes, 14 secondsgreater than zero, it means that uh it's a bad reduction. And bad reduction, we had two bit bad reductions, right?
6:20:216 hours, 20 minutes, 21 secondsMultiplicative reduction and addictive reduction. And addictive reduction was uh the worst thing. And if the period valuation of the discriminant is
6:20:296 hours, 20 minutes, 29 secondspositive and the period valuation of C4 equals zero uh it's a multiplicative reduction and if the period valuation of
6:20:376 hours, 20 minutes, 37 secondsdiscrim is is positive and the periodic valuation of C4 is greater than zero it means addictive reduction. So with this
6:20:456 hours, 20 minutes, 45 secondscriterion we do not have to reduce the curve find the points and compute partial derivatives directly every time to detect singular points. Instead we
6:20:536 hours, 20 minutes, 53 secondscan just look at uh valuations of the delta and C4 and that already tells us the reduction type. Now even if two
6:21:026 hours, 21 minutes, 2 secondselliptic curves are isomorphic over Q, they can look quite different as equations. In other words, the same elliptic curves can have many different
6:21:106 hours, 21 minutes, 10 secondsvar equation depending on the coordinate system we use. For example, consider the elliptic curve that looks like this. y^2
6:21:206 hours, 21 minutes, 20 seconds= x cub + 16 x + 64. Now make the change of variables.
6:21:316 hours, 21 minutes, 31 secondsx = 4x prime and y = 8 y prime. So let's
6:21:366 hours, 21 minutes, 36 secondsplug this in. uh 64 y prime squar is equal to 64x prime
6:21:456 hours, 21 minutes, 45 secondscub + 64x prime + 64. Oh, so what do we
6:21:516 hours, 21 minutes, 51 secondsget? We have uh y prime 2 = x prime cub + x prime + 1. So these two equations
6:22:006 hours, 22 minuteslook different but they are describing essentially the same over q. uh because the isomeorphism is just a rational change of coordinates. But now this
6:22:096 hours, 22 minutes, 9 secondscreates a small problem because if the same relative curve can be written many different ways uh then which equation
6:22:166 hours, 22 minutes, 16 secondsshould we use? This matters because quantity like discriminant depends on the equation. If we choose a bad equation, the discriminant may look
6:22:246 hours, 22 minutes, 24 secondscomplicated and the reduction behavior may look worse than it really should be.
6:22:296 hours, 22 minutes, 29 secondsSo we need a way to choose the best equation among all these possible via stress equation and what should the
6:22:376 hours, 22 minutes, 37 secondscriterion be and we find the answer by looking at one prime p at a time for a fixed prime p among all integral via shi
6:22:466 hours, 22 minutes, 46 secondsequation for the same elliptic curve. We decide that a better equations uh are the ones with the smaller periodic valuation of the discriminant. Why?
6:22:566 hours, 22 minutes, 56 secondsBecause the periodic valuation of the discriminant measures how many powers of P appears in the discriminant and discriminant is what we use to detect
6:23:046 hours, 23 minutes, 4 secondsbad reduction. So if VP discriminant is large just because we chose a bad coordinate system then the equation is making the curve looks worse at P than
6:23:136 hours, 23 minutes, 13 secondsit really is. So at the prime P we try to remove all necessary powers of prime for the discriminant and that leads to
6:23:216 hours, 23 minutes, 21 secondsdefinition. A minimal equation is P is a various equation whose discriminant has the smallest possible PI valuation among
6:23:306 hours, 23 minutes, 30 secondsall other various shar equation for the same curve. So from the point of view of P smaller VP discriminant means a better
6:23:386 hours, 23 minutes, 38 secondsequation. So there is one small problem um there infinitely many primes. So maybe one equation is good at P= 3 but
6:23:466 hours, 23 minutes, 46 secondsanother equation is better at P= 5. Then which prime should be prioritized? The nice fact is that over the set of
6:23:546 hours, 23 minutes, 54 secondsrational numbers, we do not have to choose one prime over other because there exists a various trans equation that is minimal at every prime p at the
6:24:026 hours, 24 minutes, 2 secondssame time and that is called the globally minimal via trans equation. So locally at each prime P we try to
6:24:096 hours, 24 minutes, 9 secondsminimize VP discriminant and a globally minimal equation is an equation that does this simultaneously for all primes.
6:24:186 hours, 24 minutes, 18 secondsIf you have made it this far, you may have heard the phrase before semi-stable elliptic curves. Whilst first prove the modularity theorem for semi-stable
6:24:276 hours, 24 minutes, 27 secondselliptic curves and this is exactly the word semi-stable.
6:24:306 hours, 24 minutes, 30 secondsSo an elliptic curve defined over Q is called semi-stable if it's globally minimal model has either good reduction
6:24:386 hours, 24 minutes, 38 secondsor multiplicative reduction at every prime number. So you can think of semi-stable curve as an elliptic curves
6:24:456 hours, 24 minutes, 45 secondswhose reduction is never too bad at each prime. It's allowed to have good reduction and it's even allowed to have multiplicative reduction which is uh not
6:24:546 hours, 24 minutes, 54 secondsa good reduction. Right? But addictive reduction is never allowed on a semi-stable elliptic curve. Here I want to briefly introduce one of the most
6:25:026 hours, 25 minutes, 2 secondsfamous functions in number theory. The reman zeta function. It's defined as the infinite series like this. So you take
6:25:096 hours, 25 minutes, 9 secondsevery positive number n take it to this power s and take the reciprocals and and add everything up. And this function can
6:25:176 hours, 25 minutes, 17 secondsbe also written like this. The product of all factors 1 / 1 - b to the minus s for all prime. And this particular term
6:25:266 hours, 25 minutes, 26 secondsin product for primes is defined as the local zeta function. Now why does this equation holds? Let's see. So we want to
6:25:346 hours, 25 minutes, 34 secondsshow that 1 + 1 / 2 s + 1 over 3 s + 1 4 s + blah blah blah is equal to the
6:25:436 hours, 25 minutes, 43 secondsproduct of 1 / 1 - p to the minus s. But we know that this is equal to the sum of
6:25:496 hours, 25 minutes, 49 secondsgeometric series p to the s + 1 2 s + blah blah right. So if we write this for
6:25:576 hours, 25 minutes, 57 secondsall p uh this becomes 1 + 1 / 2 s + 1 over 2 2s
6:26:066 hours, 26 minutes, 6 secondsto 3s and we have uh p = 3
6:26:186 hours, 26 minutes, 18 secondsand p = 5 and so on and so on for all primes. Now
6:26:276 hours, 26 minutes, 27 secondsthink about expanding the factors on the right side. Uh from p= 2 factor we choose one of uh these. So let's say we
6:26:356 hours, 26 minutes, 35 secondschoose this one over 2s and for p = 3 uh so we choose uh this factor and p = 5 we
6:26:446 hours, 26 minutes, 44 secondschoose one. So if we multiply these together we have one over 2s 1 over 3 2s
6:26:536 hours, 26 minutes, 53 secondswell I don't know we can have 1 over 11 uh and we can also have 1 over 11 7s
6:27:016 hours, 27 minutes, 1 secondblah blah blah so every term we get on the right hand side looks like this but
6:27:076 hours, 27 minutes, 7 secondsactually this is equal to 1 over 2 3^ 2 uh 117
6:27:156 hours, 27 minutes, 15 secondsuh to the power fs like this and by unique factorization domain every positive integral n appears exactly once
6:27:246 hours, 27 minutes, 24 secondsin this way. So when we expand the product over primes we found every one of one over n ds and that's how this
6:27:326 hours, 27 minutes, 32 secondsformula uh works. This part is a little bit technical so if you don't want to follow every details uh that's completely fine. The main point here is
6:27:406 hours, 27 minutes, 40 secondsthat we are trying to imitate what we did for remman functions on the elliptic curve side. To do that we first attach a ring to the defined part of the curve
6:27:496 hours, 27 minutes, 49 secondsand this ring is defined as a quotient like this. So fpx comma y uh this is basically a polomial uh ring and this e
6:27:596 hours, 27 minutes, 59 secondsthis is a ideal generated by reduced kef and this is a dedicant domain. Um what is a dedicant domain? uh it's an
6:28:076 hours, 28 minutes, 7 secondsintegral domain in which every nonzero proper ideals factors into a product of prime ideals and for any non-zero ideals
6:28:166 hours, 28 minutes, 16 secondsalpha of a um its norm I would define as the cardality of the quotient a mod a um
6:28:246 hours, 28 minutes, 24 secondsand the important property is that the norm is multiplicative meaning that n a b equals n a nb this is the important
6:28:336 hours, 28 minutes, 33 secondspart and because I use factors uniquely into prime ideals of the static in domain settings and because the norm has
6:28:416 hours, 28 minutes, 41 secondsmulticative property. Uh this one over n a s would be written as something like uh n a is factorized into a prime ideal.
6:28:526 hours, 28 minutes, 52 secondsSo it look like P1 uh E1 P2 E2 blah blah blah P K E K and since the norm function
6:29:026 hours, 29 minutes, 2 secondsis multiplicative uh like this this is equal to N P1 E1 N P2 E2
6:29:136 hours, 29 minutes, 13 secondsN PK EK So because this ring is a dedicating domain and this norm is multiplicative we can do the exact same
6:29:226 hours, 29 minutes, 22 secondsthing one we did for the remmanetta function. So the sum of these can be described by the product of these vectors and this only describes the
6:29:316 hours, 29 minutes, 31 secondsained part of the curve. But the projective elliptic curve also has the point at infinity O. And to account for that extra point, we will also
6:29:406 hours, 29 minutes, 40 secondsuh multiply this uh additional term and we will define this as the local zeta function of an elliptic curve. And the
6:29:486 hours, 29 minutes, 48 secondssame zeta function can be built in a more geometric way. Instead of talking about ideals and primary groups here and
6:29:566 hours, 29 minutes, 56 secondsthe same zeta functions can be built in a more geometric way. Instead of talking about ideals and prime ideals, we can count points. Uh so let Ebar be an
6:30:056 hours, 30 minutes, 5 secondselliptic curve over FP and we can count points of points over FP. But we can also count points on larger infinite fields like FP squ or FP cub and so on.
6:30:166 hours, 30 minutes, 16 secondsAnd the local zeta function packages all of these point counting into one generated function. And that looks like this. So it's uh defined as the
6:30:246 hours, 30 minutes, 24 secondsexponents of uh this sum where t equals p to the minus s. And the remarkable thing is that these two perspectives are
6:30:336 hours, 30 minutes, 33 secondsdescribing the same zeta function. On one side uh we have the algebra perspective. We built the zeta functions using ideals, prime ideals and norms in
6:30:426 hours, 30 minutes, 42 secondsa way that looks very similar to the reman zeta function. On the other side we have the geometric perspective. Uh we built by counting points over the
6:30:516 hours, 30 minutes, 51 secondsfinfield field FP FP squ and FP cub and so on. These are very completely different two constructions. One is
6:30:586 hours, 30 minutes, 58 secondsabout ideals in a ring and others is is about counting points and a curve. But the surprising point is that they meet.
6:31:056 hours, 31 minutes, 5 secondsThere are two ways of seeing the same arithmetic object. And this is one reason why zeta functions are so important. They let us see the same
6:31:136 hours, 31 minutes, 13 secondsarithmetic object from two completely different angles. And one really surprising thing is that that the complicated looking infinite object uh
6:31:226 hours, 31 minutes, 22 secondsthe zeta functions can actually be written in a very uh closed form uh like this. So uh let's show how this works.
6:31:306 hours, 31 minutes, 30 secondsSo the zeta function on the geometric side was defined defined like this. So Z
6:31:396 hours, 31 minutes, 39 secondsdt equals exponential of
6:31:496 hours, 31 minutes, 49 secondstn / n. And we know that t is p to the minus s.
6:31:556 hours, 31 minutes, 55 secondsAnd about the number of points over the finished field uh e fn.
6:32:046 hours, 32 minutes, 4 secondsSo we made a whole big deal out of house theorem getting bounds and stuff. So um this might feel a little bit funny but actually we do have an explicit formula
6:32:136 hours, 32 minutes, 13 secondsfor this number and this is p to the n + 1 minus alpha to the n minus beta to the
6:32:206 hours, 32 minutes, 20 secondsn where alpha and beta are um roots of x^ 2 minus apx
6:32:286 hours, 32 minutes, 28 secondsplus p equals zero. So the roots are alpha and beta. And before we uh expand this and simplify this, we would first
6:32:366 hours, 32 minutes, 36 secondswant to look at a tailaylor series of 1 / 1 - x. And this is uh sum of x to the^
6:32:446 hours, 32 minutes, 44 secondsof n to infinity. And we will integrate both sides. So minus ln 1 - x equals uh
6:32:536 hours, 32 minutes, 53 secondsthe sum of n + 1 x cn + one. But uh I'll change the index to make it simple. also
6:33:016 hours, 33 minutes, 1 secondx to the power of n and where n starts from one to infinity. So uh using this
6:33:086 hours, 33 minutes, 8 secondsand using the fact that this can be described as uh this expression let's
6:33:146 hours, 33 minutes, 14 secondslook at this this is exponential uh sigma denominator we have n and we
6:33:246 hours, 33 minutes, 24 secondshave p n + 1 minus alpha n minus beta n
6:33:306 hours, 33 minutes, 30 secondsuh tn right this is equals to
6:33:376 hours, 33 minutes, 37 secondsuh pt / n
6:33:446 hours, 33 minutes, 44 secondsplus t n / n minus alpha t / n minus beta t / n.
6:33:546 hours, 33 minutes, 54 secondsAnd so if we use this we can simplify this as denominator we have uh
6:34:026 hours, 34 minutes, 2 secondsas a denominator we have 1 minus pt 1 minus t and numerator we have 1 minus
6:34:106 hours, 34 minutes, 10 secondsalpha t 1 minus beta t but we know that alpha plus beta equals a p and alpha beta
6:34:196 hours, 34 minutes, 19 secondsequals p. So uh the numerator is 1 minus alphos beta= a p a pt
6:34:286 hours, 34 minutes, 28 secondsplus uh alpha beta= p right so p t t²
6:34:356 hours, 34 minutes, 35 secondsand the denominator stays the same
6:34:406 hours, 34 minutes, 40 secondsand if we put uh t = p to the minus s we finally get this formula.
6:34:506 hours, 34 minutes, 50 secondsNow you just saw that the zeta functions of a reduced elliptic curves has the form and here the denominator is kind of like
6:34:596 hours, 34 minutes, 59 secondsthe standard background part. The elliptic curve itself is really showing up in the numerator because a has the point counter thetas right. So I will
6:35:086 hours, 35 minutes, 8 secondstake the numerator and take the reciprocals and we will define that as the local L factors of an elliptic
6:35:166 hours, 35 minutes, 16 secondscurve. So this local L factor is like the concentrated extract of the elliptic curves at the prime P. It packs a lot of
6:35:246 hours, 35 minutes, 24 secondsinformations about how the curve behaves at P into one small factor.
6:35:306 hours, 35 minutes, 30 secondsNow we already define the L functions of an elliptic curve. For each prime P, we had a local factor LPS. And for good
6:35:386 hours, 35 minutes, 38 secondsreduction, it look like this. We just defined it.
6:35:426 hours, 35 minutes, 42 secondsAnd when we have a bad reduction, the factor slightly differs and it looks like this. Then we multiply all these local factors together for all prime ps
6:35:516 hours, 35 minutes, 51 secondsand this gives us the h vile l functions of the elliptic curve. So what does this mean? Each prime p gives us a small
6:35:596 hours, 35 minutes, 59 secondspiece of informations about the elliptic curve the lps local z local l functions.
6:36:046 hours, 36 minutes, 4 secondsAt good primes that informations comes from counting points on the reduced uh finite field. At bad primes the curve
6:36:126 hours, 36 minutes, 12 secondsdegenerates. So the factor changes depending on the type of battery reduction.
6:36:176 hours, 36 minutes, 17 secondsThe L functions takes all these local informations prime by prime and packages into the one global analytic object. And
6:36:256 hours, 36 minutes, 25 secondsthis is why the L function is such a big deal because it's take the data from every primes and put it into a one small function. So instead of studying
6:36:336 hours, 36 minutes, 33 secondsinfinitely many primes separately, we can study this one object. We have already seen a conductor on the GO representation side. There the conductor
6:36:416 hours, 36 minutes, 41 secondsmeasured how the representation behaves at each primes especially where it is ramified and how badly it is ramified.
6:36:486 hours, 36 minutes, 48 secondsFor elliptic curves we define a similar kinds of invariant. The conductor of an elliptic curve is uh ne that records the
6:36:566 hours, 36 minutes, 56 secondsbad primes of the curve and also how bad the reduction it has those primes.
6:37:026 hours, 37 minutes, 2 secondsHere uh ne is defined as the product of ptfp for all primes p. If E has good
6:37:116 hours, 37 minutes, 11 secondsreductions at P then FP equals zero meaning that P does not appear in the conductor and if E has multiplicative
6:37:206 hours, 37 minutes, 20 secondsreduction at P then FP is defined as one. So multiplicative bad reduction contributes one power of P and if E has
6:37:286 hours, 37 minutes, 28 secondsaddictive reduction which is uh the worst then FP is greater or equal to two. So it contributes a higher power of
6:37:366 hours, 37 minutes, 36 secondsP. You can think of it as the elliptic curve version of the conductor we saw regular representation. On both sides
6:37:436 hours, 37 minutes, 43 secondsthe conductors measures bad behaviors prime by prime. Chapter five is modular forms. Now the word modular uh may
6:37:516 hours, 37 minutes, 51 secondssounds familiar. You might think it has something to do with modular like number theory. But modular forms are something completely different. They are complex
6:38:006 hours, 38 minutesfunctions. And if you have watched pop science videos about famous theorem, you have probably heard people say something like a modular form is about symmetry.
6:38:086 hours, 38 minutes, 8 secondsBut what does that actually mean? What kind of function has that much symmetry?
6:38:126 hours, 38 minutes, 12 secondsWhy would such a function appear in number theory? And does it anything to do with elliptic curves? Uh and that we're going to find out in this chapter.
