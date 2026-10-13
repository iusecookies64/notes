Chapter 10: Rings, Fields, Ideals, and Unique Factorization
3:36:073 hours, 36 minutes, 7 secondsNow let's learn another algebraic structure. So far we have talked about groups. A group is a set of one operation that had identity and inverse
3:36:163 hours, 36 minutes, 16 secondsfor all the elements. But now we want to define a structure with two binary operation and that is called a ring. So
3:36:253 hours, 36 minutes, 25 secondsa ring is a set with two binary operations. So addiction and multiplication satisfying first uh R has
3:36:333 hours, 36 minutes, 33 secondsto be an aellion group under addiction and the second one is about the associivity of the multiplication and
3:36:413 hours, 36 minutes, 41 secondslastly the distributive law should hold like I've said in the vector space this addiction and multiplication might not be the one that we are familiar of
3:36:493 hours, 36 minutes, 49 secondsalthough the name is addiction and multiplication they can be defined in a weird way. So some examples of ring the
3:36:573 hours, 36 minutes, 57 secondsmost easiest one would be Z. Uh Z is obviously ring right because Z and addiction is an a billion group and we
3:37:053 hours, 37 minutes, 5 secondsknow that multiplication Z is is associative and distributive law of course holds. Uh Q is a ring.
3:37:143 hours, 37 minutes, 14 secondsR is a ring. C is also a ring. uh some nonobvious examples
3:37:263 hours, 37 minutes, 26 secondsuh the collection of n byn real entries matrices is a ring um because uh yes
3:37:353 hours, 37 minutes, 35 secondsit's an addictive aellion group and in this uh group uh matrix multiplication is associative and the distributive law
3:37:433 hours, 37 minutes, 43 secondsalso holds so this we can call this a ring uh and Of course, ZN is also a
3:37:503 hours, 37 minutes, 50 secondsring. This was a addictive group we saw, right? Um, here we define multiplication
3:37:583 hours, 37 minutes, 58 secondsby multiplying and then remainder modulo n. So for example, Z5 3 * 4 uh is two
3:38:073 hours, 38 minutes, 7 secondsbecause this is 2 modulo 5 12 is 2 modulo 5. So defining the multiplication like this ZN forms a ring uh because the
3:38:163 hours, 38 minutes, 16 secondsmultiplication is associative and uh the distributive law holds uh RX
3:38:263 hours, 38 minutes, 26 secondsthis was a set of polomials with real coefficients and this is also a ring because we know that it's an addictive
3:38:333 hours, 38 minutes, 33 secondsaellion group and um the associivity of multiplication holds
3:38:403 hours, 38 minutes, 40 secondsand the distributive laws. Uh you can check uh however uh n the set of natural numbers this is
3:38:503 hours, 38 minutes, 50 secondsnot a ring. This is not even an addictive abilion group. So this is not a ring.
3:38:573 hours, 38 minutes, 57 secondsIn a ring we can add elements. So take any element for example a and we will
3:39:043 hours, 39 minutes, 4 secondsadd uh a to itself again and again. So a + a + a + a and it goes along. So what
3:39:133 hours, 39 minutes, 13 secondswe want to know is that is there some positive integral n uh that adding any element a to itself n times always end
3:39:213 hours, 39 minutes, 21 secondsup in zero. So the characteristic of r is the smallest positive integral n such that adding a n times equals zero. And
3:39:313 hours, 39 minutes, 31 secondsif such a positive integral exist exist then we say that characteristic R equals N. And if no such positive integral
3:39:393 hours, 39 minutes, 39 secondsexist the characteristic is defined to be zero. So for example in Q or R or Z
3:39:493 hours, 39 minutes, 49 secondsor C here we can add elements again and again it never end up in zero right you pick one and you add one and it kept uh
3:39:573 hours, 39 minutes, 57 secondsgetting bigger and bigger. Uh so in this case the characteristic of these kind of ring is zero. But uh on the other hand
3:40:053 hours, 40 minutes, 5 secondsZN the characteristic of ZN uh is
3:40:123 hours, 40 minutes, 12 secondsN because uh let's say for example in Z5 you pick any number and you add that five times and it becomes zero. Uh for
3:40:213 hours, 40 minutes, 21 secondsexample, you pick three and you add three five times and this is zero modulo 5. Uh this is
3:40:313 hours, 40 minutes, 31 secondsbecause three multiplied by five equals 0 modulo 5. So the characteristic of
3:40:383 hours, 40 minutes, 38 secondsring ZN equals zero. Uh how about the characteristic of Z2
3:40:473 hours, 40 minutes, 47 secondsproduct Z3? Uh this one is tricky.
3:40:543 hours, 40 minutes, 54 secondsIf you take any element um let's take uh one comma one. Uh let's add one comma
3:41:023 hours, 41 minutes, 2 secondsone uh by itself. So uh if you add them two times it becomes 2 comma 2 right uh
3:41:083 hours, 41 minutes, 8 secondsit's 0 comma 2 and you add that three times I just write this way. If you add
3:41:163 hours, 41 minutes, 16 secondsit three times, it becomes 3 comma 3 which is 1 comma 0.
3:41:233 hours, 41 minutes, 23 secondsIf you add that four times, this is uh 0 comma 1. Right?
3:41:323 hours, 41 minutes, 32 secondsIf you add that five times, uh it's five comma 5 and we have to take the remainder. So it's three no one comma
3:41:423 hours, 41 minutes, 42 secondstwo. And if you add this six times 1 comma 1 and this is uh 0 comma 0. So
3:41:503 hours, 41 minutes, 50 secondsfinally we got zero. So the characteristic of uh Z2 product Z3 is six because if we take any element from
3:41:583 hours, 41 minutes, 58 secondsZ2 product Z3 for example A comma B and if we um add this six times uh this is 6
3:42:063 hours, 42 minutes, 6 secondsA modulo 2 times 6 B modulo 3 right but 6 A modulo 2 uh of course it's zero
3:42:143 hours, 42 minutes, 14 secondsright and 6 B modulo 3 because 6 B is divisible by three this is zero so the
3:42:203 hours, 42 minutes, 20 secondscharacteristic of Z2 product of Z3. We know that it's six.
3:42:273 hours, 42 minutes, 27 secondsBefore moving on, let's quickly check three words in ring theory, which is commutative, unity, and unit. First, a ring is commutative if its multiplication is commutative.
3:42:383 hours, 42 minutes, 38 secondsAnd a unity or identity is a multiplicative identity element which is denoted by one. So, some rings may not
3:42:483 hours, 42 minutes, 48 secondshave a unity. So technically the existence of one is not always automatic from the definition of a ring but in
3:42:553 hours, 42 minutes, 55 secondsmost examples we deal with uh the ring does have a unity. So you don't have to uh care much about the existence of the
3:43:023 hours, 43 minutes, 2 secondsunity in a ring and a unit is an element in a ring with unity that has a multiplicative inverse.
3:43:133 hours, 43 minutes, 13 secondsSo if a is an r a is called unit unit if there exist b
3:43:213 hours, 43 minutes, 21 secondssuch that ab equals ba equals 1. One here is the unity. Uh in this case b is
3:43:293 hours, 43 minutes, 29 secondsthe inverse of a. Not every element in ring is a unit. Uh for example z the only units are one and minus one. Right?
3:43:393 hours, 43 minutes, 39 secondsSeven for example seven is not a unique unit because that does not exist um integrate such that 7 A equals one right
3:43:493 hours, 43 minutes, 49 secondsin Q every number is a unit except for zero zero does not have a multiplicative
3:43:563 hours, 43 minutes, 56 secondsinverse right uh how about Z9
3:44:033 hours, 44 minutes, 3 secondsis five is a unit it's equivalent to asking is there a multiplicative inverse to five. Yes, there is uh if you pick
3:44:123 hours, 44 minutes, 12 secondstwo, 5 * 2 equals 1 modulo 9. So five is a unit. But on the other hand, three is
3:44:203 hours, 44 minutes, 20 secondsnot a unit of Z9 because there does not exist any integers such that 3 A equals 1 modulo 9. This cannot be happening.
3:44:333 hours, 44 minutes, 33 secondsAnd before we move on, unit and unity has similar names and concepts. So they're uh easy to mix up. So make sure you distinguish between the two.
3:44:453 hours, 44 minutes, 45 secondsHere's where things get a little bit complicated. The terms on the slides are closely related, so it's easy for them to get tangled up in your head, but if
3:44:543 hours, 44 minutes, 54 secondswe separate them carefully, it's not that bad. And in fact, it's pretty important. Um so this slide is mainly here to understand two special kinds of
3:45:033 hours, 45 minutes, 3 secondsring which is um integral domain and a field. Um we are adding extra conditions to make more refined structures. Before
3:45:123 hours, 45 minutes, 12 secondsthat we need to know what a zero divisor is. A zero divisor is a nonzero element a for which there exists a nonzero b
3:45:213 hours, 45 minutes, 21 secondssuch that a b equals zero in a ring. Um for example in Z6
3:45:283 hours, 45 minutes, 28 secondstwo is one of the zero divisors because 2 * uh three equals zero here right so
3:45:363 hours, 45 minutes, 36 secondstwo is a zero divisor three is a zero divisor um six in Z8
3:45:433 hours, 45 minutes, 43 secondsis also a zero divisor because uh six multiplied by 4 equals zero in Z8.
3:45:513 hours, 45 minutes, 51 secondsuh but however uh in Z6 if you pick uh something like five five is not a zero divisor because
3:46:003 hours, 46 minutesuh for an element to satisfy uh 5 a equals zero in z6 a has to be uh divided by six
3:46:093 hours, 46 minutes, 9 secondswhich means that a should be zero. So five is not a zero divisor in the ring Z6.
3:46:163 hours, 46 minutes, 16 secondsAnd an integral domain is a commutative ring with unity that has no zero divisors.
3:46:243 hours, 46 minutes, 24 secondsAnd an integral domain is a commutative ring with unity that has no zero [clears throat] divisor. So what are some examples of integral domain? The
3:46:323 hours, 46 minutes, 32 secondsmost common one would be Z. Z is obviously a commutive ring and has no zero divisions, right? uh for a integral
3:46:413 hours, 46 minutes, 41 secondsto satisfy a b equals zero either a is zero or b is zero. Right? So z has no zero divises which means that z uh is an integral domain.
3:46:523 hours, 46 minutes, 52 secondsAnd a field is one of the most restrictive structures we will see. A field is a commutative ring with unity where every nonzero element is a unit.
3:47:033 hours, 47 minutes, 3 secondsYou can think of a field as a number system where addiction, subtraction, multiplication and divisions are all possible except of course division by
3:47:123 hours, 47 minutes, 12 secondszero. You can't do that. So what are some examples of a field? Q is a field,
3:47:183 hours, 47 minutes, 18 secondsright? Because Q is a commutative ring uh with every nonzero element is a unit, right? Zero is the only element that
3:47:263 hours, 47 minutes, 26 secondsdoes not have a multiplative inverse in Q. Um
3:47:323 hours, 47 minutes, 32 secondssimilarly R is also a ring and C is also a ring and Z7
3:47:403 hours, 47 minutes, 40 secondsis also a ring. Uh this one is kind of uh tricky. Why is Z7 a ring? We have to show that every nonzero element is a unit. For example, uh is one a unit?
3:47:523 hours, 47 minutes, 52 secondsMeaning that uh it's equivalent to asking this one has a multiplicative inverse. Yes, because uh one itself is a multiplicative inverse. How about two?
3:48:033 hours, 48 minutes, 3 secondsTwo has a multiplicative inverse of four because if we product these two, this becomes one modulo 7.
3:48:123 hours, 48 minutes, 12 secondsHow about three? Uh is there an element such that 3x = 1 modulo 7? Uh yes
3:48:213 hours, 48 minutes, 21 secondsbecause if we take five 3 * 5 = 15 and 15 is 1 modulo 7 this is one
3:48:303 hours, 48 minutes, 30 secondsand how about uh six itself is inverse because 6 * 6 is 36
3:48:383 hours, 48 minutes, 38 secondsand 36 is one modulo 7. Okay, so every non-zero element in Z7 has a multiplicative inverse which means that
3:48:463 hours, 48 minutes, 46 secondsevery non-zero element is a unit and that's why we can call Z7 a field.
3:48:533 hours, 48 minutes, 53 secondsA finite field is exactly what the name means a field withinitely many elements.
3:48:583 hours, 48 minutes, 58 secondsSo unlike Q or R or C which have infinitely many elements, a finite field has only many elements. For example, uh the field we just saw Z7.
3:49:103 hours, 49 minutes, 10 secondsZ7 is a favorite field because it has only seven elements. Uh it's coming to the ring with every non-zero element as a multiplicative inverse. Um the good
3:49:203 hours, 49 minutes, 20 secondsthing is that the ring theory says that if a field has infinitely many elements then the number of elements should be
3:49:273 hours, 49 minutes, 27 secondssome power of prime p uh where p is prime and the field with p to the n
3:49:343 hours, 49 minutes, 34 secondselements is unique up to isomorphism. So structurally there are only one fields that have uh p to the n elements.
3:49:433 hours, 49 minutes, 43 secondsSo u that can be fields with I don't know two three
3:49:483 hours, 49 minutes, 48 seconds5 8 uh 9 11 16 elements because nine is
3:49:563 hours, 49 minutes, 56 secondsa product of prime. 16 is also a a power of prime but there's no infinite field with say like six elements or 10
3:50:053 hours, 50 minutes, 5 secondselements because this is not a product of a prime. So uh finite field with this many element cannot exist.
3:50:153 hours, 50 minutes, 15 secondsNow we look at ideals. We defined coion groups earlier. Remember that the idea was this. We started with a group. We
3:50:233 hours, 50 minutes, 23 secondsdivided into coetses and we treat those cosettes as elements of a new group.
3:50:293 hours, 50 minutes, 29 secondsRight? Now we want to do the same thing uh similar for rings. But to make that work on the group side we needed a
3:50:373 hours, 50 minutes, 37 secondsspecial conditions on the subgroup. Um that condition was called normality. We did not go deeply into normal subgroups
3:50:433 hours, 50 minutes, 43 secondsbut but anyway uh we want to define a quotient like objects for ring which will be later be called as a factor ring
3:50:513 hours, 50 minutes, 51 secondsor a quotient ring but again we cannot just take any random subset we need a special kind of subset that is compatible with ring operations
3:51:013 hours, 51 minutes, 1 secondand that special kind of object is called an ideal here uh so an addictive subgroup n of a ring
3:51:083 hours, 51 minutes, 8 secondsr satisfying uh these these properties saying that a n is again a subset of n
3:51:163 hours, 51 minutes, 16 secondsand nb is also a subset of n for any a b and r uh this is called an ideal
3:51:243 hours, 51 minutes, 24 secondsand an ideal is called prime if a and n means either a in n or b an element of
3:51:323 hours, 51 minutes, 32 secondsn. So these kind of ideals are called prime ideals. Let's look at some examples of ideals.
3:51:423 hours, 51 minutes, 42 secondsUh first, if I take ring R as Z and
3:51:483 hours, 51 minutes, 48 secondsthe addictive subgroup 6Z, 6Z is an ideal of Z. uh because if we take any
3:51:563 hours, 51 minutes, 56 secondselement from Z, so A is any integer and if we multiply A to the left side or the
3:52:053 hours, 52 minutes, 5 secondsright side of 60 C, this set is a subset of 60 C. This is
3:52:143 hours, 52 minutes, 14 secondsbecause if we take any multiple of six and you multiply it by any integral and that result is also a multiple of six.
3:52:223 hours, 52 minutes, 22 secondsThis is obvious. So 6 Z can be called as a ring of Z.
3:52:283 hours, 52 minutes, 28 secondsAnd uh another example would be I will take ring R as RX
3:52:353 hours, 52 minutes, 35 secondsand N will be the ideal generated by X2 + 1. So the multiples of factor x^2 + 1
3:52:453 hours, 52 minutes, 45 secondsis in the set. For example um x^2 + 1 x cub + 4x + 1. These kinds of polomials are in this set.
3:52:553 hours, 52 minutes, 55 secondsSo is this an ideal? Yes. Because if you take any polomial and you multiply to the multiple of x2 + 1 and it's still a
3:53:043 hours, 53 minutes, 4 secondsmultiple of x2 + 1. So this is a ideal ideal of rx.
3:53:113 hours, 53 minutes, 11 secondsHowever, if you take r
3:53:173 hours, 53 minutes, 17 secondsas z squ and if I take n as a comma a where a is c um this is an addictive
3:53:263 hours, 53 minutes, 26 secondssubgroup of uh r right but this is not an ideal because um
3:53:343 hours, 53 minutes, 34 secondsa plus a plus um any element of r for example 1 comma 2 this becomes A + 1 A +
3:53:433 hours, 53 minutes, 43 seconds2 right this is not a element of N right so this is not an ideal of R and now
3:53:513 hours, 53 minutes, 51 secondssome examples of prime ideal 5Z is
3:53:593 hours, 53 minutes, 59 secondsan ideal of Z right is it a prime ideal
3:54:063 hours, 54 minutes, 6 secondsyes because if AB is in 5Z Z
3:54:123 hours, 54 minutes, 12 secondsA is either in 5Z or B is either in 5Z because if A B is a multiple of five
3:54:203 hours, 54 minutes, 20 secondseither A is multiple of five or B is multiple of five right but um if you
3:54:273 hours, 54 minutes, 27 secondschange this five to six Z is an idea of Z right but 6 Z is not a
3:54:333 hours, 54 minutes, 33 secondsprime idea of Z because uh for example 12 is a multiple of six right and 12 is
3:54:423 hours, 54 minutes, 42 seconds12 is 3 * 4 but three is not a multiple of six and four is not a multiple of six
3:54:493 hours, 54 minutes, 49 secondsbut 12 is a multiple of six so 6 Z is not a prime ideal of Z. Now we can
3:54:563 hours, 54 minutes, 56 secondsfinally define a factor ring or also called as a quotient ring. The idea is very similar to what we did with quotient groups. For coion groups, we
3:55:053 hours, 55 minutes, 5 secondstook cassettes and we treated those cassettes as an element of a new group.
3:55:093 hours, 55 minutes, 9 secondsHere we do the same thing but now uh in different settings of a ring. So if I is an ideal of a ring R, we can form the
3:55:183 hours, 55 minutes, 18 secondsfactor ring R mod I. And its elements are of course the addictive coats A plus I for I, A and R. And the operations are
3:55:283 hours, 55 minutes, 28 secondsdefined as this. So we add the representatives a plus b when we add two cosetses here and when we uh multiply
3:55:363 hours, 55 minutes, 36 secondstwo coetses it's defined as the new coets made by uh the multiplying the representatives for quotient groups we
3:55:453 hours, 55 minutes, 45 secondsonly needed to define one group operations for quotient rings we need both addiction and multiplication and this is why I had to be an ideal the
3:55:543 hours, 55 minutes, 54 secondsideal condition is what makes multiplication between cassettes well defined some examples the factor rings
3:56:013 hours, 56 minutes, 1 seconduh for prime number p Z mod PZ is a ring. So for example Z mod 7 Z here uh 1
3:56:093 hours, 56 minutes, 9 seconds+ 6 Z uh plus 5 + 6 Z is equal to 1 + 5 = 6.
3:56:183 hours, 56 minutes, 18 secondsOh it's 7 Z. So 1 + 5 = 6, right? So this is 6 + 7 z.
3:56:293 hours, 56 minutes, 29 secondsAnd the multiplication for example 2 + 7 z ult*lied by uh 4 + 7 z is you multiply
3:56:393 hours, 56 minutes, 39 secondsthe representatives 2 * 4 = 8 and 8 modulo 7 = 1. So it's 1 + 7 z.
3:56:493 hours, 56 minutes, 49 secondsAnd um if we take rx and take a quotient by the idle generated by x^2 + 1 this is also a ring
3:56:583 hours, 56 minutes, 58 secondsand the element would look something like uh x + 7 plus i= x^2 + 1 and
3:57:073 hours, 57 minutes, 7 secondsactually uh it is isomeorphic to c which is isomeorphic to r squ. uh we will not
3:57:143 hours, 57 minutes, 14 secondsprove this but uh fun fact we've already seen polomial rings a few times for examples
3:57:203 hours, 57 minutes, 20 secondsrx is a ring qx is also a ring and even cx can be a
3:57:283 hours, 57 minutes, 28 secondsring um in cx um the elements are like 1 + i x cub + x^2 - 7 I it looks like this
3:57:383 hours, 57 minutes, 38 secondsokay so now we are just making the idea explicit So the element in f(x) when f
3:57:463 hours, 57 minutes, 46 secondsis a field looks like polomials a 0 + a1
3:57:513 hours, 57 minutes, 51 secondsx plus a2x 2 uh plus a n x to the n
3:57:583 hours, 57 minutes, 58 secondswhere the a's uh here the coefficients of x is a element of x. So for example
3:58:053 hours, 58 minutes, 5 secondsthis example here this is a element of cx and uh if I take this polinomial
3:58:123 hours, 58 minutes, 12 secondssquare 7 + 5 x cub + 11 x to the 17
3:58:203 hours, 58 minutes, 20 secondsthis is a element of r x but this is not a element of qx because you have uh square 7 here.
3:58:293 hours, 58 minutes, 29 secondsSo we can add polomials, subtract polomials and multiply polomials and we can still get polomials with coefficients in half. That's why this is
3:58:383 hours, 58 minutes, 38 secondsa ring and we can define the irreducibility of a polomial. A polomial is said to be
3:58:473 hours, 58 minutes, 47 secondsirreducible over f if it cannot be factored into two lower degree non-constant polomial in fx and it's
3:58:553 hours, 58 minutes, 55 secondsreducible if it's otherwise. So for example x^2 - 4x + 3
3:59:033 hours, 59 minutes, 3 secondsuh fx is this polomial reducible or irreducible.
3:59:103 hours, 59 minutes, 10 secondsuh this can be factored into lower degree const non-constant polomial right x -1 x - 3 and this polomial is also a
3:59:193 hours, 59 minutes, 19 secondsmember of rx so this is irreducible over the field r
3:59:273 hours, 59 minutes, 27 secondshowever if I take gx x x^2 + 1 is it irreducible or reducible
3:59:363 hours, 59 minutes, 36 secondsum this is first of all this is irreducible overall Right because it cannot be factored into lower degree
3:59:433 hours, 59 minutes, 43 secondspolomials. However, in C it's reducible because this can be factored into X plus I
3:59:513 hours, 59 minutes, 51 secondsX minus I. So it depends on what field we are looking at. So we already know what divisibility means in integers,
3:59:593 hours, 59 minutes, 59 secondsright? For example, 4 divides 24 and 51 divides 133 something like this. So now
4:00:084 hours, 8 secondswe want to extend this idea from integers to more general rings. So let R be a commutative ring and for A elements
4:00:174 hours, 17 secondsin R we write B bar A if that exists C in R such that A equals B C. So it's
4:00:254 hours, 25 secondskind of like a generalization of the divisibility. Okay. So for examples
4:00:314 hours, 31 secondsum x -1 divides x^2 minus one in rx
4:00:384 hours, 38 secondsbecause there exist x + one such that the product of x + one and x - one
4:00:454 hours, 45 secondsequals [clears throat] x^2 - 1. Okay. So divisibility is not only of an integers.
4:00:514 hours, 51 secondsuh and then Z 7 surprisingly three divides four
4:01:004 hours, 1 minutebecause 3 * 6 = 4 modulo 7 that exits six such
4:01:084 hours, 1 minute, 8 secondsthat uh the product of three and six is equal to four modulo 7 and let's now let's define another related word which
4:01:164 hours, 1 minute, 16 secondsis associates two element a b and r associates if a equals B U for some unit
4:01:234 hours, 1 minute, 23 secondsU. Uh remember unit was the element that had multiplicative inverse right and AB here if they associates they're
4:01:314 hours, 1 minute, 31 secondsconsidered equivalent in terms of divisibility.
4:01:344 hours, 1 minute, 34 secondsUh so for example in Z three and minus3 associates because three equals minus1 *
4:01:424 hours, 1 minute, 42 seconds-3 and minus1 was a unit on Z right and in RX
4:01:524 hours, 1 minute, 52 secondsthe nonzero real constants are unit right so x^2 minus one associates with I
4:01:594 hours, 1 minute, 59 secondsdon't know minus uh 1 7 x^2 + 1 / 7 and
4:02:064 hours, 2 minutes, 6 secondsalso x^2 + x + 1 associates with 2x^2 + 2x + 1. These two associates.
4:02:154 hours, 2 minutes, 15 secondsSo we are still trying to generalize family divisibility ideas from integrates to more general rings. In the integers we know what prime numbers are.
4:02:244 hours, 2 minutes, 24 secondsFor example like 2 3 5 7 11 there.
4:02:274 hours, 2 minutes, 27 secondsThey're prime numbers. But now we working in a more general array or uh in an integral domain. So we need to define
4:02:354 hours, 2 minutes, 35 secondscarefully what it means for an element of D to behave like prime numbers. And there are two related notions here. Um
4:02:434 hours, 2 minutes, 43 secondsnumber one uh first of all we're looking at D which is an integral domain. A nonzero non-unit element P is
4:02:514 hours, 2 minutes, 51 secondsirreducible if any factorization P= AB implies that either A or B is a unit.
4:02:584 hours, 2 minutes, 58 secondsThis definition is very similar to what we've seen at uh the definition of prime ideal.
4:03:044 hours, 3 minutes, 4 secondsAnd second, a nonzero non-unit P is prime if P dividing AB implies P dividing A or P dividing B.
4:03:174 hours, 3 minutes, 17 secondsSo four examples in RX.
4:03:214 hours, 3 minutes, 21 secondsLet's look at polomial x^2 + 1. Is x2 1 uh irreducible? Yes, it's irreducible
4:03:304 hours, 3 minutes, 30 secondsbecause if you find a factorization x^2 + 1 and rx um it's uh it's it's
4:03:384 hours, 3 minutes, 38 secondsyou can only find um these kind of factorizations with unit. This is a unit, right? And also um this is a unit.
4:03:484 hours, 3 minutes, 48 secondsSo we can say that f(x) = x^2 + 1 is irreducible in rx. Uh and is x2
4:03:564 hours, 3 minutes, 56 secondsand is x^2 + 1 prime? Um yes it's prime because if x2 + 1 divides some polomial
4:04:074 hours, 4 minutes, 7 secondsgx hx this means that x2 + 1 either divides
4:04:144 hours, 4 minutes, 14 secondsgx or x2 + 1 divides hx because x2 + 1 cannot be uh divided into parts. Right?
4:04:244 hours, 4 minutes, 24 secondsAnother examples uh ordinary prime numbers 2 3 5 7 blah blah are these
4:04:324 hours, 4 minutes, 32 secondsnumbers irreducible in Z yes because uh let's say you pick seven and try to factoriize seven you can
4:04:404 hours, 4 minutes, 40 secondsfactoriize like this is the only way and one and minus one is a unit uh that's
4:04:464 hours, 4 minutes, 46 secondswhy seven is irreducible and is seven prime yes because if 7
4:04:544 hours, 4 minutes, 54 secondsdivides uh some product of an integer uh either seven divides a or seven divides b. So we can call seven prime here.
4:05:054 hours, 5 minutes, 5 secondsBut these two concepts are not always the same. Let's take a look at this ring z roo 5i. And the definition of
4:05:144 hours, 5 minutes, 14 secondsthis ring is the linear combination of 1 and roo 5 i which is a + b square 5 i where a and b are
4:05:244 hours, 5 minutes, 24 secondsintegers. Okay. And we will look at element two from this ring. First of all two is irreducible in this ring. Um
4:05:334 hours, 5 minutes, 33 secondsbecause if you factor if you try to factoriize two the only way is 2 * 1 or minus one times minus 2 and 2 and minus
4:05:424 hours, 5 minutes, 42 secondsone is a unit here but but is two prime here? Uh it's actually
4:05:514 hours, 5 minutes, 51 secondsnot because 2 / 6, right? And 6 is factorized into 1 + 5 I 1 - 5
4:06:014 hours, 6 minutes, 1 secondI and two divides neither of them. So two is not a prime in this ring.
4:06:094 hours, 6 minutes, 9 secondsSo UFDs an integral domain. Now we're going to be looking at UFDs.
4:06:164 hours, 6 minutes, 16 secondsAn integral domain D is a unique factorization domain or UFD if every nonzero non-unit element has a unique
4:06:254 hours, 6 minutes, 25 secondsfactorization into reducible elements up to orders and unit. Um first of all what does it mean by up to order and units
4:06:344 hours, 6 minutes, 34 secondshere? Um for example uh let's say we factoriize [clears throat] 24 uh we could write two two
4:06:434 hours, 6 minutes, 43 secondsthree and we can even write um I don't know three minus three minus two two and
4:06:504 hours, 6 minutes, 50 secondstwo so up to orders in unit means that in this kind of situations we treat these
4:06:574 hours, 6 minutes, 57 secondstwo factorizations the same because 2 and minus two are associates and the factors only differs by units and by
4:07:044 hours, 7 minutes, 4 secondsorders. So we uh treat this the same. So anyways uh what are some examples of
4:07:114 hours, 7 minutes, 11 secondsunique factorization domain? The most uh famous one is Z. Z you can factoriize any integers and you have a unique
4:07:204 hours, 7 minutes, 20 secondsfactorization. For example, uh 1207 is factorized by 17 * 21. And this
4:07:284 hours, 7 minutes, 28 secondsis the only way, right? So Z is a unique factorization domain. And qx
4:07:364 hours, 7 minutes, 36 secondsqx is a unaccization domain. rx is also a unit factorization domain. Uh as well
4:07:444 hours, 7 minutes, 44 secondsas cx. However, um Z
4:07:514 hours, 7 minutes, 51 secondssquare 5 I. This is not a unique factorization domain because here 6 is 2
4:07:584 hours, 7 minutes, 58 seconds* 3. But this is also 1 + square I 1 minus square I. These two are
4:08:064 hours, 8 minutes, 6 secondsdifferent uh factorizations method. So uh this is we can't call this a unique factorization domain. Now we finally
4:08:144 hours, 8 minutes, 14 secondsgoing to prove the lema we used when we prove the case n= 3 of fair theorem. We are going to look at the set z
4:08:244 hours, 8 minutes, 24 secondsomega. This is defined as the set of a + b omega where a and b are integers. And
4:08:324 hours, 8 minutes, 32 secondsomega here is min -1 + 3 i / 2. So omega^ 2 + omega + 1 = z.
4:08:424 hours, 8 minutes, 42 secondsSo this special set is called the Eisenstein integrals and the important fact is that is this is a unique
4:08:494 hours, 8 minutes, 49 secondsfactorization domain. So here the factorization is unique. Um now I want to introduce a function called the norm.
4:08:584 hours, 8 minutes, 58 secondsYou can think of it as a way to measure the size of an element in the string or very roughly you can think of it as a generalized version of an absolute value. So how do I define norm here?
4:09:094 hours, 9 minutes, 9 secondsNorm of a + b omega is defined as I will define as a squ minus a b + b squ. And
4:09:194 hours, 9 minutes, 19 secondsone good thing about uh norm is that norm alpha beta is norm alpha
4:09:274 hours, 9 minutes, 27 secondsand beta. U it means that if a divides b it means that b equals some a t for some
4:09:354 hours, 9 minutes, 35 secondst right. So norm b equals norm a norm t.
4:09:424 hours, 9 minutes, 42 secondsThis means that if a divides b, norm a divides norm b. And since this is an
4:09:514 hours, 9 minutes, 51 secondsinteger, uh this is a divisibility uh in normal integers, right? So um
4:09:594 hours, 9 minutes, 59 secondswe have the property that if a divides b norm a integer divides norm b. So knowing these let's prove this lema.
4:10:094 hours, 10 minutes, 9 secondsFirst we are going to factoriize this. We have s cub = p ^ 2 + 3 q ^ 2 right
4:10:184 hours, 10 minutes, 18 secondsthis is p + square iq p - 3 IQ.
4:10:274 hours, 10 minutes, 27 secondsNow our goal here is to show that these two factors are co-prime. So I will put uh D I will denote D as the common divisor of these two.
4:10:414 hours, 10 minutes, 41 secondsUh it's not uh note that keep in mind that it's not the greatest common divisor. It's just a common divisor of
4:10:484 hours, 10 minutes, 48 secondsthese two. So if D divides both these two factors, D also divides 2 P and D
4:10:564 hours, 10 minutes, 56 secondsalso divides the difference which is 2 square 3 IQ. Right? And notice that any common divisor that does not come
4:11:044 hours, 11 minutes, 4 secondsfrom 23 I would have to divide both P and Q which is impossible by the primitive
4:11:124 hours, 11 minutes, 12 secondscondition. Therefore, the only possible obstructions comes from the factor 2 3 I. So, in order for us to show
4:11:214 hours, 11 minutes, 21 secondsthat these two factors are co-prime, we just have to show that D is impossible at uh 2 3 I. And actually, we will
4:11:304 hours, 11 minutes, 30 secondssplit this problem and we will show that d= 2 is impossible and d= uh square
4:11:374 hours, 11 minutes, 37 seconds3 i is impossible. Okay. And uh particularly uh this square 3 I
4:11:444 hours, 11 minutes, 44 secondsequ= 2 omega + 1 right and 2 omega + 1 equals omega minus omega
4:11:524 hours, 11 minutes, 52 secondssquar because here omega square + omega + 1 equals zero right and this is equal to omega 1 minus omega but omega here
4:12:004 hours, 12 minutesthis is a unit because if you u compute the norm here uh this is one so we can just show that d= 1 minus w is
4:12:094 hours, 12 minutes, 9 secondsimpossible. So in conclusion for order for us to show that these two factors are co-prime we show that d = 2 is
4:12:174 hours, 12 minutes, 17 secondsimpossible and d = 1 - omega is impossible. So first if d = 2 2 divides
4:12:264 hours, 12 minutes, 26 secondsp + square 3 iq right and uh square root i is equal to uh 2 omega + 1 so 2
4:12:354 hours, 12 minutes, 35 secondsomega + 1 q and this is equals to p + q + 2 q omega and since 2 q omega is
4:12:444 hours, 12 minutes, 44 secondsdivisible by two p + q is divided by q so p and q has the same parody but since
4:12:514 hours, 12 minutes, 51 secondsp and q is co-prime we know that p and q is odd so um p ^ 2 + 3 square = s cub
4:13:014 hours, 13 minutes, 1 secondand here we'll examine both sides by modulo 8 and since the square of odd number is one modulo 8 the left hand
4:13:104 hours, 13 minutes, 10 secondsside we know that it's 4 modulo 8 uh however uh no cube is four modulo 8
4:13:184 hours, 13 minutes, 18 secondsright because four modulo 8 means that there that cube number is even uh and if you take a cube of every even number uh
4:13:264 hours, 13 minutes, 26 secondsit's a multiple of eight so uh this is impossible which is a contradiction so d being 2 is impossible
4:13:344 hours, 13 minutes, 34 secondsand second case we look at the case where d= 1 minus omega so 1 minus omega
4:13:414 hours, 13 minutes, 41 secondsmust divide p + square iq and this is equals to 2q omega plus p + q and
4:13:514 hours, 13 minutes, 51 secondshere we will use these properties and you will uh look at the uh norm value norm of 1 minus omega is uh three right
4:14:014 hours, 14 minutes, 1 secondso three divides the norm of this is 2 q
4:14:074 hours, 14 minutes, 7 seconds^ 2 + p + q squar minus 2 q uh * p + q
4:14:154 hours, 14 minutes, 15 secondsand this is uh p ^ 2 and Uh uh
4:14:234 hours, 14 minutes, 23 secondsis it is it p + 3^ 2? Yes, I think it's right. Uh since this is p + 3^ 2, p ^ 2
4:14:304 hours, 14 minutes, 30 secondsis divisible by 3. So p uh can be written in 3 p prime by some integral p
4:14:374 hours, 14 minutes, 37 secondsprime. Uh so we put this to this equation. Uh since p is a multiple of
4:14:444 hours, 14 minutes, 44 secondsthree, the right hand side is a multiple of three. So s is a multiple of three.
4:14:494 hours, 14 minutes, 49 secondsSo we put s as uh uh 3 s prime. So we get 27 s prime
4:14:584 hours, 14 minutes, 58 secondscub equals uh 9 p uh prime squar + 3 q ^ 2.
4:15:074 hours, 15 minutes, 7 secondsUh and if we divide both sides by three, we have 9 s prime cub = 3 p prime
4:15:154 hours, 15 minutes, 15 secondssquar + q ^ 2. So Q is a multiple of three but that's is a contradiction because P and Q has to be co-prime
4:15:254 hours, 15 minutes, 25 secondsright. So D being 1 minus omega is also impossible which means that these two are co-prime and since the product of
4:15:334 hours, 15 minutes, 33 secondsco-prime factor is a perfect cube and this is a unique factorization domain uh these two factors should itself be a perfect cube.
4:15:444 hours, 15 minutes, 44 secondsSo I can put P + roo3 IQ as some U
4:15:514 hours, 15 minutes, 51 secondsplus uh square I V cube for some co-prime U and V. And if you uh expand
4:16:004 hours, 16 minutesthis you have uh u cub plus 3 u 2 3
4:16:084 hours, 16 minutes, 8 secondsi v minus
4:16:134 hours, 16 minutes, 13 seconds9 u v ^ 2 - 3 3 I v ^ 2 and this is
4:16:224 hours, 16 minutes, 22 secondsu uh u ^ 2 - 9 v ^ 2 + uh 3 square
4:16:294 hours, 16 minutes, 29 seconds3 I v u ^ 2 minus v ^ 2 and uh if you
4:16:364 hours, 16 minutes, 36 secondscompare both sides uh you should know that uh p equals this and q equals if
4:16:454 hours, 16 minutes, 45 secondsyou divide root3 i uh q equals this. So we prove the lema.
