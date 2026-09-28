Chapter 7: Vector Spaces, Basis, and Dimension
1:40:321 hour, 40 minutes, 32 secondsabout numbers. A lot of mathematics is about structures. A vector space is one of the most important examples of such a
1:40:401 hour, 40 minutes, 40 secondsstructure. Um so vector space at first when you hear the word vector you might
1:40:461 hour, 40 minutes, 46 secondsthink of arrows in the plane right you might heard in a physics class. So uh
1:40:531 hour, 40 minutes, 53 secondslike 2 comma 1 this we call a vector or a arrows in third dimensional plane. So
1:41:001 hour, 41 minutes1 comma 2 comma 4 these kind of things we used to call them a vector but here um we want to sort of generalize the terms of vector here mathematically.
1:41:131 hour, 41 minutes, 13 secondsOkay so here we go. A vector space V over field F is a set with addiction and
1:41:201 hour, 41 minutes, 20 secondsscalar multiplication satisfying these eight rules. Um first of all what is this addiction and scholar
1:41:281 hour, 41 minutes, 28 secondsmultiplication? Um it's an operation right? Addiction here is a function from
1:41:361 hour, 41 minutes, 36 secondsV product V to V. It takes two vectors in V uh and add them and the result
1:41:431 hour, 41 minutes, 43 secondsshould again be an element of V. And scalar multiplication it takes one value of V and one number
1:41:531 hour, 41 minutes, 53 secondsand it gives a result in V. Okay.
1:41:591 hour, 41 minutes, 59 secondsSo if you take a scalar from field F number and a vector from V then multiplying them should again gives us
1:42:061 hour, 42 minutes, 6 secondsvector in V. Um so let's look at these eight rules that the vector space should satisfy. Uh first one and second one is
1:42:151 hour, 42 minutes, 15 secondsabout addiction. Uh the addiction defined in vector space has to satisfy uh commutativity and associivity.
1:42:241 hour, 42 minutes, 24 secondsBut wait wasn't addiction always commitive and associative? Uh who doesn't know that a plus b equals b plus
1:42:311 hour, 42 minutes, 31 secondsa right? But actually the addiction here may not be the addiction that we already
1:42:381 hour, 42 minutes, 38 secondsfamiliar of. It's just a given operation whose name happens to be an addiction.
1:42:431 hour, 42 minutes, 43 secondsRight? I've earlier said that addiction takes two vectors in V and uh gives one vectors in V. Right? So uh if v is a set
1:42:541 hour, 42 minutes, 54 secondsof real numbers and if I define a plus b as some sort of weird crazy way like a
1:43:021 hour, 43 minutes, 2 secondsto the power of b plus uh e a b 72 uh
1:43:081 hour, 43 minutes, 8 secondspower. This is again in a real number set right. So this addiction I define
1:43:161 hour, 43 minutes, 16 secondsuh is actually can be an addiction right because it takes two uh real numbers and it gives one real number back. So of
1:43:251 hour, 43 minutes, 25 secondscourse this addiction does not satisfy these two right. So the addiction that
1:43:321 hour, 43 minutes, 32 secondsis defined on a vector space should define these two uh commutivity and associivity. That's that's uh what these
1:43:411 hour, 43 minutes, 41 secondstwo rules are telling here. Okay. And the third one is about there should be a zero in v. We call this a zero vector.
1:43:511 hour, 43 minutes, 51 secondsAnd uh it has to satisfy x plus0 vector equals x for all x no matter what x you
1:43:581 hour, 43 minutes, 58 secondspick in v. Okay. And rule number four says for every vector every element in v
1:44:051 hour, 44 minutes, 5 secondsminus x should exist in v such that x plus minus x should be zero and zero here is the zero from the third rule.
1:44:151 hour, 44 minutes, 15 secondsAnd number five and six is about scalar multiplication. 1* X should be X and A *
1:44:211 hour, 44 minutes, 21 secondsX should be same as A uh scalar multiplication B scalar multiplication X and number seven and eight is about
1:44:301 hour, 44 minutes, 30 secondsdistributive law. So what are some examples of vector spaces?
1:44:371 hour, 44 minutes, 37 secondsUm first of all R is a vector space.
1:44:421 hour, 44 minutes, 42 secondsIt's so obvious that it's a vector space, right? Because rule number one through rule number eight uh satisfies,
1:44:481 hour, 44 minutes, 48 secondsright? C is also a vector space and u uh r to the power of n is actually
1:44:581 hour, 44 minutes, 58 secondsa vector space. Remember this was a cartisian product. And how do we define addiction multiplication here? Of course
1:45:051 hour, 45 minutes, 5 secondsRN the addiction multiplication is the operation that we are familiar of. And here rn the addiction is multiplication
1:45:141 hour, 45 minutes, 14 secondsdefined like this. So if you add x1 x2 blah blah blah xn plus y1 y2 blah blah
1:45:231 hour, 45 minutes, 23 secondsyn uh you add corresponding entries x+ + y1 x2 + y2 blah blah blah x n + yn.
1:45:341 hour, 45 minutes, 34 secondsUh scalar multiplication. If you scar multiplication a with any uh vector or
1:45:411 hour, 45 minutes, 41 secondselements in Rn uh this is defined as ax1 ax2
1:45:481 hour, 45 minutes, 48 secondsax3 blah blah blah axn. So when we call arrows in the plane or arrows in
1:45:561 hour, 45 minutes, 56 secondsthreedimensional space vectors, we were actually looking at very special examples of vector spaces because r²
1:46:051 hour, 46 minutes, 5 secondsand r cube is a vector space. So element of these two sets like one comma 2. We call this a vector because this is a vector space. Okay.
1:46:171 hour, 46 minutes, 17 secondsUm some another examples of vector spaces. RX is a vector space. So what is
1:46:241 hour, 46 minutes, 24 secondsRX? This is a set of all polomials
1:46:321 hour, 46 minutes, 32 secondswith a real coefficient.
1:46:371 hour, 46 minutes, 37 secondsSo how do you know that this set is a vector space? You check if this set satisfies rule number one through rule number eight. Uh for example, rule
1:46:461 hour, 46 minutes, 46 secondsnumber one asks if uh if you add two polomials and change the order, do you get the same result back? Yes, we do.
1:46:551 hour, 46 minutes, 55 secondsLike uh 1 + x + 3 + x^2
1:47:011 hour, 47 minutes, 1 second= 3 + x^2 + 1 + x. It's so obvious, right? So like this you check all the
1:47:091 hour, 47 minutes, 9 secondseight rules and this uh we can call this a vector space. Okay. Uh and uh set of
1:47:161 hour, 47 minutes, 16 secondsall continuous functions we write it as C 0 uh R. This is the set of all
1:47:231 hour, 47 minutes, 23 secondscontinuous functions. This is also a vector space.
1:47:271 hour, 47 minutes, 27 secondsAnd um also this is also a vector space, right? Um
1:47:361 hour, 47 minutes, 36 secondsfor example, rule number four, you pick any X. Is there a minus X in this set?
1:47:421 hour, 47 minutes, 42 secondsYes. because you pick like any matrix 3 4 5 8 and uh - x - 3 -4 -5 - 8 are also
1:47:531 hour, 47 minutes, 53 secondson this set. So rule number four satisfies uh but uh the set of natural numbers
1:48:011 hour, 48 minutes, 1 secondthis is not a vector space because uh while rule number one and rule number two might satisfy
1:48:081 hour, 48 minutes, 8 secondsum zero is not in the zed right and also if you pick any x minus x is not in natural numbers you pick three and minus
1:48:171 hour, 48 minutes, 17 secondsthree is not in n right so n is not a vector space.
1:48:241 hour, 48 minutes, 24 secondsNow that we have defined vector spaces, we can learn about subspace. A subspace is basically a small vector space
1:48:311 hour, 48 minutes, 31 secondssitting inside a bigger vector space. Um so for examples um R is a subspace of C
1:48:391 hour, 48 minutes, 39 secondsbecause R is a subspace of C and both is a vector space. So we call R a subspace
1:48:461 hour, 48 minutes, 46 secondsof C. Okay. And uh if I define w as all pairs of x comm y where y = 2x.
1:48:571 hour, 48 minutes, 57 secondsIf you test this, we know that uh w is a vector space and w is also a subspace of r².
1:49:051 hour, 49 minutes, 5 secondsSo w is a subspace of r².
1:49:101 hour, 49 minutes, 10 secondsBut if I define uh w prime as uh the collection of x comm y where y = x + one
1:49:201 hour, 49 minutes, 20 secondsis it a subspace of r²?
1:49:251 hour, 49 minutes, 25 secondsUh first of all this is obviously a subset of r square. Uh but is this a
1:49:321 hour, 49 minutes, 32 secondsvector space? No it's not a vector space because it does not have a zero vector in it. Right? 0 comma 0 is not in the Z.
1:49:421 hour, 49 minutes, 42 secondsUh so this is not a vector space which means that we can't call this a subspace of R squ this because this is not even a
1:49:491 hour, 49 minutes, 49 secondsvector space. Um some examples of subspaces are
1:49:551 hour, 49 minutes, 55 secondsP to R.
1:50:021 hour, 50 minutes, 2 secondsThis is the set of all uh real coefficient polomial
1:50:131 hour, 50 minutes, 13 secondswith maximum degree 2. Degree at most two. So like 1 + x uh 3 + 3x +
1:50:241 hour, 50 minutes, 24 seconds5x^2 is in the set. But um anything more than that degree is not in this set. And
1:50:311 hour, 50 minutes, 31 secondsuh uh this is also a vector space. So this is a subspace of uh p
1:50:391 hour, 50 minutes, 39 secondsr this was the set of all real coefficient polomial. Right now we are slowly moving towards the idea of a basis. Um so what is a basis?
1:50:511 hour, 50 minutes, 51 secondsA basis is one of the most important ideas in linear algebra. Roughly speaking, a basis is a minimal set of
1:50:581 hour, 50 minutes, 58 secondsbuilding blocks for a vector space. For example, if we look at um R squar, uh
1:51:061 hour, 51 minutes, 6 secondsone of bases for R squ is 1 comma 0 and 0 comma 1 because uh you
1:51:161 hour, 51 minutes, 16 secondscan pick any element in R squ and uh you can make this a comma b using these two
1:51:231 hour, 51 minutes, 23 secondselements like this. So uh we can build every elements
1:51:311 hour, 51 minutes, 31 secondsin R squ using these only uh two elements. So we call this a basis. Uh so if you know the basis then you can build
1:51:401 hour, 51 minutes, 40 secondsevery vectors in the space from those spaces vectors and you can do it in a unique way. But before we can define basis properly we need a few smaller
1:51:491 hour, 51 minutes, 49 secondsconcept and the first one is linear combination.
1:51:531 hour, 51 minutes, 53 secondsSo a linear combination of vectors in a set s v1 through vk is any vector u of
1:52:001 hour, 52 minutesthe form a1 v1 plus a to v2 plus blah blah a k vk where a1 through a ks are
1:52:071 hour, 52 minutes, 7 secondsnumbers. Okay. So for examples um in R2
1:52:131 hour, 52 minutes, 13 secondsI'll pick uh any subset of vectors. If I take S as 1 comma 2 and 3 comma 4,
1:52:231 hour, 52 minutes, 23 secondsthe linear combinations of S would be something like A 1 2 + B 3A 4. Okay. So
1:52:341 hour, 52 minutes, 34 secondsis is 5 comma 8 linear combination of S?
1:52:401 hour, 52 minutes, 40 secondsWe check if there exists A and B such that this equation holds. Um and actually there is because if we take a =
1:52:501 hour, 52 minutes, 50 seconds2 and b = 1 this is 5 comma 8. So 5a 8 is a linear combination of these two vectors.
1:53:011 hour, 53 minutes, 1 secondHowever, um if you look at another example, if we look at vector space R squar and if we take S as um one two
1:53:111 hour, 53 minutes, 11 secondsthree one to zero 4 7 0
1:53:181 hour, 53 minutes, 18 secondsum is 3 4 5 a linear combination of S?
1:53:261 hour, 53 minutes, 26 secondsUm, no we can't. Uh, we can't because no matter how you combine these two vectors
1:53:351 hour, 53 minutes, 35 secondsplus B 470, the third coordinate will always be zero, right? It cannot be five, right?
1:53:441 hour, 53 minutes, 44 secondsUm, so 345 is not a linear combination of S. So we know what a linear combination is.
1:53:531 hour, 53 minutes, 53 secondsWe can now define what is a span. Um suppose we have a set of vectors uh s uh
1:54:001 hour, 54 minuteswe will write s as v1 v2 through vn. So in total of n vectors. Um the span of s
1:54:101 hour, 54 minutes, 10 secondsdenoted by this span s is the smallest subspace of v containing s.
1:54:191 hour, 54 minutes, 19 secondsum smallest subspace of V containing S. Uh but what does it actually looks like?
1:54:271 hour, 54 minutes, 27 secondsWell, uh if a subspace contains um S, V1 through VN,
1:54:331 hour, 54 minutes, 33 secondsthen it must also contains things like 2 V1 plus V2 or something like V1 minus 7
1:54:431 hour, 54 minutes, 43 secondsV2 + 5 V3, right? uh because a subspace has to be closed under scala
1:54:501 hour, 54 minutes, 50 secondsmultiplication and addiction. Uh that's because subspace is also a vector space right. So once this contain the original
1:54:591 hour, 54 minutes, 59 secondsvectors v1 through vk uh it is forced to contain every possible linear combinations of them. Right?
1:55:081 hour, 55 minutes, 8 secondsThat means any subspace containing s must contain all vectors of the form a1
1:55:151 hour, 55 minutes, 15 secondsv1 plus a2 v2 plus blah blah blah a n vn
1:55:221 hour, 55 minutes, 22 secondswhere a 1 through a n is uh numbers or scalas. Now the nice thing is that if
1:55:291 hour, 55 minutes, 29 secondsyou collect all these linear combinations uh this forms a vector space. Uh so while the definition of
1:55:371 hour, 55 minutes, 37 secondsspan is the smallest subspace of v containing s blah blah blah you can just think of span of s as the collection of
1:55:451 hour, 55 minutes, 45 secondsall the linear combinations of s. So we will now going to learn about linear independence and dependence. A set of
1:55:531 hour, 55 minutes, 53 secondsvectors uh s containing v3 vk we call it linearly dependent if the only solution
1:56:011 hour, 56 minutes, 1 secondto the equation a1 v1 plus a2 v2 plus follow a vk equals z is the trivial
1:56:081 hour, 56 minutes, 8 secondssolution a1 through a k equals zero and if a set is not linearly dependent we call them linearly dependent
1:56:171 hour, 56 minutes, 17 secondsum so uh let's look at some examples in r square is 1 comma 2
1:56:261 hour, 56 minutes, 26 seconds1 comma 0 linearly dependent. Um to know this we make an equation. So a1 1 comma
1:56:341 hour, 56 minutes, 34 seconds2 + a2 1 comma 0 and this is equal to a1 + a2
1:56:431 hour, 56 minutes, 43 seconds2 a1 right and in order for this vector to be a zero vector a2 should be zero
1:56:501 hour, 56 minutes, 50 secondsand a1 should be zero. So the only solution to this equation is a1 a2 being
1:56:571 hour, 56 minutes, 57 secondsboth being zero. So these two vectors are linear dependent. Okay. How about uh
1:57:061 hour, 57 minutes, 6 secondsin R cube uh 1 2 3 1 135
1:57:141 hour, 57 minutes, 14 seconds2 5 A. These vectors are not linearly dependent meaning that they are linearly
1:57:221 hour, 57 minutes, 22 secondsdependent because this equation has another solution that a1 through a k uh being all zero because because there's a
1:57:321 hour, 57 minutes, 32 secondssolution other than all a's being zero right in this case we call that these vectors are linearly dependent another
1:57:401 hour, 57 minutes, 40 secondsexample um in rx again rx was the collection of All real
1:57:471 hour, 57 minutes, 47 secondscoefficients of polomial, right? Uh ifs 1 + x x 2 + x 2 + 3x + x² linearly
1:57:591 hour, 57 minutes, 59 secondsdependent or linear dependent. Uh it's linearly dependent because
1:58:051 hour, 58 minutes, 5 secondsthere's a solution that looks
1:58:101 hour, 58 minutes, 10 secondslike this. + -1 2 + 3x + x² = z. Since that is a solution, then all
1:58:201 hour, 58 minutes, 20 secondsthe a's being zero, we call these vectors linearly dependent.
1:58:271 hour, 58 minutes, 27 secondsSo we finally define what is basis and what is dimension. So we finally define basis and dimension. So we want a set of
1:58:361 hour, 58 minutes, 36 secondsvectors that can build the entire vector space by taking linear combinations. For examples uh we saw this before R squ the
1:58:451 hour, 58 minutes, 45 secondsbasis of R² uh so one of many basis of R square was 1 comma 0 comma 1. Uh this
1:58:531 hour, 58 minutes, 53 secondscould make the entire vector space R square by taking linear combinations. For example,
1:59:001 hour, 59 minutesyou take any vector from R square and this could be represented by a linear combination of these two vectors like this.
1:59:101 hour, 59 minutes, 10 secondsUh but we don't want this set to be unnecessarily large, right? Because we can put like any other vector 34, 55 in
1:59:191 hour, 59 minutes, 19 secondsthis set and we can still generate a comma b using uh the three vectors but this is redundant. We don't need these
1:59:271 hour, 59 minutes, 27 secondsunnecessary vector. Right? So what we really want is a set that is large enough to generate the whole space but small enough to contain only the
1:59:361 hour, 59 minutes, 36 secondsnecessary information and that is the idea of a basis. So a basis for a vector space V should satisfies two conditions.
1:59:461 hour, 59 minutes, 46 secondsFirst it should be linear dependent uh and second it has to span V. It has to make free and it has to be small enough uh compact and small enough. Okay.
2:00:002 hoursAnd the dimension of V we define as the number of vector in a basis. Uh so so
2:00:072 hours, 7 secondssome examples uh what are basis and dimension of R cube.
2:00:142 hours, 14 secondsUh the most common one would be one 0 0 1 0 0 1.
2:00:242 hours, 24 secondsThis is one basis of R cube. And since the number of elements in the set is three, the dimension of this vector space is three. But basis is not unique.
2:00:362 hours, 36 secondsMeaning that there could be other bases.
2:00:382 hours, 38 secondsUm for example 0 1 0 1
2:00:462 hours, 46 seconds0 1 1 0 1. This is also basis of RQ. Uh this
2:00:532 hours, 53 secondsis linear dependent. And this also spans V.
2:00:582 hours, 58 secondsSo this is also a basis for R cube. Um some other examples P2R
2:01:072 hours, 1 minute, 7 secondsthis was a vector space of collections of all polomials with real coefficients with degree at most two. Right? The
2:01:142 hours, 1 minute, 14 secondsbasis of this vector space would be something like 1 x x^2 or maybe uh 7 x +
2:01:242 hours, 1 minute, 24 secondsx^2 uh minus x. This is also basis for p2r.
2:01:312 hours, 1 minute, 31 secondsSo the basis so the dimension of this vector space is three.
2:01:362 hours, 1 minute, 36 secondsUm what about the basis and dimension of this vector space? uh the most easy
2:01:442 hours, 1 minute, 44 secondsbasis would be this right. So the dimension of this vector space is four.
2:01:562 hours, 1 minute, 56 secondsBut you also have to know that dimension is well defined. In other words, a basis might be not unique but the number of
2:02:032 hours, 2 minutes, 3 secondselements in a basis is always fixed for a given vector space. So it cannot happen like one basis of the same vector
2:02:112 hours, 2 minutes, 11 secondsspace has three elements and the another vector space has four elements then we can't define dimension of a vector space right that kind of things cannot happen
2:02:212 hours, 2 minutes, 21 secondswhich means that bases and dimension we can well define the two concepts so far we have mostly talked about a
