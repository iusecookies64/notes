Chapter 16: Reduction Modulo p, Point Counting, and Frobenius
5:38:455 hours, 38 minutes, 45 secondsNow we want to look at elliptic curves through the lens of prime number p.
5:38:495 hours, 38 minutes, 49 secondsSuppose we have an elliptic curve over Q by an equation with integral coefficients. For example, if we take an
5:38:565 hours, 38 minutes, 56 secondselliptic curve Y^2 = XQ + 6 X + 11. Now choose a prime number say um P = 5.
5:39:095 hours, 39 minutes, 9 secondsFrom now on we want to look at this equations over the finite field f5 or uh it's isomeorphic to z mod 5z.
5:39:205 hours, 39 minutes, 20 secondsNow here's the important point. Over z mod 5z or z5 there are only five possible values right 0 1 2 3 4. So
5:39:285 hours, 39 minutes, 28 secondsunlike an elliptic curve defined over q this is not a continuous curve in the plane. It's a finite sets of points where we can literally plug in values of
5:39:365 hours, 39 minutes, 36 secondsx and check whether there exists a value of y satisfies the equation. So if we look at elliptic curves over the finite field 5 which is equivalent to saying
5:39:445 hours, 39 minutes, 44 secondslooking at this elliptic curve a modulo 5 y^2 = x² + 6 x + 11
5:39:545 hours, 39 minutes, 54 secondsmodulo 5 only infinitely many points are possible. So the points on this curve
5:40:005 hours, 40 minutesmodulo fpi is 01 04 2 1
5:40:085 hours, 40 minutes, 8 seconds2 2 4 3 1 3 4 4 4 2 4 3 for example 4a 3. If you
5:40:185 hours, 40 minutes, 18 secondsplug this in, y 2 3 2 = uh 4 cub + 24 +
5:40:265 hours, 40 minutes, 26 seconds11 uh this is 9. If you compute this, this is 64 + 24 which is 88 + 11 99 and
5:40:345 hours, 40 minutes, 34 secondsthis is equal modul 5. So 4a 3 or in this is in this curve. So reduction module P turns the curve into a object.
5:40:445 hours, 40 minutes, 44 secondsInstead of drawing a continuous curve, we can count actual points on FP. That's why reduction modul P is so useful. It lets us take an elliptic curve of a Q and studied through infinite arithmetic.
5:40:565 hours, 40 minutes, 56 secondsNow this is the important point.
5:40:585 hours, 40 minutes, 58 secondsReduction module P is not just copying the same curve into a smaller world.
5:41:025 hours, 41 minutes, 2 secondsSome geometric properties may change after the reduction. For example, u remember how we define a singular point.
5:41:095 hours, 41 minutes, 9 secondsA point is singular when all the reent partial derivatives vanish at that point. Now suppose one of those partial derivatives gives the number five uh
5:41:185 hours, 41 minutes, 18 secondsover Q that's not zero. So the partial derivative disadvantage but if we reduce modul five uh we're looking at Z5. So in
5:41:265 hours, 41 minutes, 26 secondsthe reduced world the same value becomes zero. This means that a curve that was smooth over Q can be become singular
5:41:335 hours, 41 minutes, 33 secondsafter reduction modul P. In other words, singular points that did not exist before can appear after reduction.
5:41:425 hours, 41 minutes, 42 secondsSo let E be an elliptic curve over Q given by a minimum various charge equation P. We will learn what this minimum var equation means after. And
5:41:515 hours, 41 minutes, 51 secondslet E bar be a curve reduced modul P. If E bar is still smooth, we say that E has
5:41:585 hours, 41 minutes, 58 secondsgood reduction at P. And if E bar has a singular point with distant tangent, we say that E has multiplicative reduction
5:42:065 hours, 42 minutes, 6 secondsat P. And if E bar has singular points with a repeated tangent, we say E has addictive reduction. So the first
5:42:135 hours, 42 minutes, 13 secondsscenario where E bar is smooth. This is the best uh you do the reduction and still smooth.
5:42:195 hours, 42 minutes, 19 secondsAnd if E bar has singular points, meaning that E bar has bad reduction uh these two to give you the feeling of it,
5:42:265 hours, 42 minutes, 26 secondsmultiplicate reduction is uh still bad but it's better than addictive reduction. And addictive reduction is the last thing you want to happen. this
5:42:345 hours, 42 minutes, 34 secondsis um uh bad. Okay. And uh these features here are only for visual references. They're not literally what
5:42:425 hours, 42 minutes, 42 secondsthe reduced curves looks like over uh FP because after reduction module P we are working on a finite field and there are only many points. So the curve is not a
5:42:515 hours, 42 minutes, 51 secondscontinuous curve that we can draw smoothly on a plane like this. Now we working over field. Suppose our elliptic
5:42:595 hours, 42 minutes, 59 secondscurve is defined over FQ. So we are looking at elliptic curve reduction modulo uh Q. Uh this curve has only
5:43:075 hours, 43 minutes, 7 secondsinfinitely many elements. So it makes sense to ask how many points does this elliptic cover have over the field FQ.
5:43:165 hours, 43 minutes, 16 secondsWe write this numbers like this. The number of points over EQ.
5:43:225 hours, 43 minutes, 22 secondsUm let's think about this very naively.
5:43:255 hours, 43 minutes, 25 secondsSuppose the curve is given by the short fire equation y^2 = xq + ax plus b and
5:43:345 hours, 43 minutes, 34 secondsthere are exactly q possible values for x because we are looking at uh fq. There are exactly q possible values of x
5:43:425 hours, 43 minutes, 42 secondsbecause x has to be an element of fq. So in principle we can plug in every uh q values of uh x one by one for each x the
5:43:525 hours, 43 minutes, 52 secondsright hand side xq plus a xb is again a element of fq.
5:43:585 hours, 43 minutes, 58 secondsThen we ask how many y's satisfies this once we have this value. Um sometimes that can be no solution for y and
5:44:055 hours, 44 minutes, 5 secondssometimes that exactly one solution where the right hand side is zero and sometimes there are two solutions where the right hand side is a non-zero
5:44:145 hours, 44 minutes, 14 secondssquare. So for each x the number of possible y value are zero, one or two.
5:44:225 hours, 44 minutes, 22 secondsNow without proving anything let's make a very rough guess. Maybe on average each x values gives about one point. So
5:44:315 hours, 44 minutes, 31 secondsif each of the q possible x values gives one point in average we expect about q * 1 equals q of fine points. But an
5:44:405 hours, 44 minutes, 40 secondselliptic curve is projective. That means we have to also consider the points at infinity. So after considering the uh points of infinity we might expect this
5:44:495 hours, 44 minutes, 49 secondsnumber of points to be somewhere around Q + one.
5:44:555 hours, 44 minutes, 55 secondsAnd surprisingly this rough guess is actually not that far from the truth.
5:44:595 hours, 44 minutes, 59 secondsHass theorem says that the number of point field FQ is not too far away from
5:45:055 hours, 45 minutes, 5 secondsQ + one. More precisely the difference between this is bounded by two root Q.
5:45:135 hours, 45 minutes, 13 secondsSo the difference is at most two root Q.
5:45:165 hours, 45 minutes, 16 secondsAnd right after this theorem let's give a name to the quantity that appears there. uh let e over q be an elliptic
5:45:235 hours, 45 minutes, 23 secondscurve and suppose p is a prime of good reduction meaning that uh if we reduce module p no singular points uh occurs
5:45:315 hours, 45 minutes, 31 secondsthen we can reduce e modul p and get a new curve which is defined over a field fp and count its point over fp and we
5:45:405 hours, 45 minutes, 40 secondswill define a as p + one minus uh the number of uh the number of reduced
5:45:475 hours, 45 minutes, 47 secondspoints this is exactly the error term from H's theorem. H's theorem says that this error
5:45:565 hours, 45 minutes, 56 secondsabsolute value is no greater than two roo p and from now on we call this
5:46:035 hours, 46 minutes, 3 secondsnumber a the trace of probenus and for good primes this definitions comes from point counting p + 1 minus the number of
5:46:115 hours, 46 minutes, 11 secondspoints and for bad primes um the curve does not reduce nicely so we have to use this convention instead a is defined as
5:46:205 hours, 46 minutes, 20 secondsone when you a split multiplicative reduction and minus one when non-split multiplicative reduction and zero when addictive reduction.
5:46:285 hours, 46 minutes, 28 secondsSo you do not have to memorize all of these values in bad reduction in case for now it's enough to remember that at a good prime we define the trace of
5:46:365 hours, 46 minutes, 36 secondsfenius AP as p + one minus the number of reduced points.
