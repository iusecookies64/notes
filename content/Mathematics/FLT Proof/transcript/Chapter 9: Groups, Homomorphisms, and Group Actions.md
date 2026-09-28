Chapter 9: Groups, Homomorphisms, and Group Actions
2:44:502 hours, 44 minutes, 50 secondsEarlier when we talked about vector spaces, we defined a mathematical structure specifying what kinds of object we have and what kinds of
2:44:582 hours, 44 minutes, 58 secondsoperations we can do with them. Now we are going to define another important structure which is called a group. But before defining a group we need to
2:45:062 hours, 45 minutes, 6 secondsclarify one basic idea first and that is binary operation. So binary operation star um on a set is a function that
2:45:162 hours, 45 minutes, 16 secondsassigns to each ordered pair a comma b of elements of s to some elements of s.
2:45:222 hours, 45 minutes, 22 secondsSo binary operation you can just basically view it as a function that goes from s product s to s when s is a set
2:45:312 hours, 45 minutes, 31 secondsand we call a binary operation associative if the regrouping of the elements uh does not change the result
2:45:392 hours, 45 minutes, 39 secondsof the operation and we call them commutative if a star b equals b star a.
2:45:462 hours, 45 minutes, 46 secondsThe most common binary operations that we know would definitely be addiction and multiplication, right? 3 + 4 = 7.
2:45:562 hours, 45 minutes, 56 secondsThis can be viewed as a function that assigns 3 comma 4 to 7. Same with the multiplication 4 * 5 = 20. And this is
2:46:052 hours, 46 minutes, 5 secondssame as uh we assign two order one ordered pair four comma 5 into the number 20. Okay.
2:46:142 hours, 46 minutes, 14 secondsUm we can define any uh weird binary operations. For example, I can define binary operation star that goes from r²
2:46:232 hours, 46 minutes, 23 secondsto r such that a* b equals a to the power v uh plus
2:46:332 hours, 46 minutes, 33 secondssin a e to the power of b something like this. Um and since this is still a real number we can call this a binary operation.
2:46:442 hours, 46 minutes, 44 secondsFinally we go over the definition of a group. So what is a group? A group is a set G with a binary operation satisfying
2:46:532 hours, 46 minutes, 53 secondsthree axium. First the binary operation should be associative. Meaning that uh for every ABC no matter what ABC we pick
2:47:032 hours, 47 minutes, 3 secondsin G A* B C has to be equal to A*
2:47:112 hours, 47 minutes, 11 secondsBC. Okay. And second, there is an element E. Uh we call this an identity
2:47:172 hours, 47 minutes, 17 secondselement such that E star A equals A* E equals A for all A and G. Uh this is called the identity element.
2:47:282 hours, 47 minutes, 28 secondsIdentity element. And for each elements of G there is an element A minus one such
2:47:372 hours, 47 minutes, 37 secondsthat uh if you binary operation these two you have E. So this is called an inverse.
2:47:452 hours, 47 minutes, 45 secondsOkay. And additionally a group is called aelion if its operation is also commutative.
2:47:522 hours, 47 minutes, 52 secondsAnd lastly the number of elements in a group G is called its order and it's denoted by uh like the absolute value
2:48:002 hours, 48 minutessign. So what are some examples of group? Um this would be a group the integral number set with addiction. Why
2:48:092 hours, 48 minutes, 9 secondsis this a group? Uh first is the binary operation well definfined meaning that if you add two um integer
2:48:182 hours, 48 minutes, 18 secondsuh does it gives back an integer? Yes, you add two integers and it's of course an integer, right?
2:48:242 hours, 48 minutes, 24 secondsUh and is the binary operation is the addiction associative? Yes, addiction is associative. And is there an element E
2:48:322 hours, 48 minutes, 32 secondssuch that E + A equals A + E equals A for all integer A?
2:48:422 hours, 48 minutes, 42 secondsYes, because uh we can take E as zero and this holds. So identity element here is zero.
2:48:522 hours, 48 minutes, 52 secondsAnd third, for each integer in Z, is there an element A minus one such that A
2:48:592 hours, 48 minutes, 59 secondsplus A minus one equals A minus one plus A equals in element in element here is zero, right? Uh but yes, a minus one
2:49:082 hours, 49 minutes, 8 secondsexists because minus A exists in Z, right? Like if you pick a equals 3 and
2:49:152 hours, 49 minutes, 15 secondsminus three exists in Z. Uh so we can call this Z with addiction a group. uh and particularly this group is an
2:49:242 hours, 49 minutes, 24 secondsabellia group because addiction is commutative.
2:49:292 hours, 49 minutes, 29 secondsSimilarly um Q with addiction is also a group
2:49:362 hours, 49 minutes, 36 secondsR with addiction C with addiction is also a group. However,
2:49:442 hours, 49 minutes, 44 secondsQ with multiplication is not a group because um let's see first is multiplicative associative? Yes,
2:49:522 hours, 49 minutes, 52 secondsmultiplication is associative. And is there an element E such that E star A equals A* E equals A? Um yes, because we
2:50:002 hours, 50 minutescan take one uh 1 * A equals A * 1 equals A for all A and Q,
2:50:082 hours, 50 minutes, 8 secondsright? But for each a and g is there an inverse element? Um no because if you pick zero zero has no inverse. Um there
2:50:172 hours, 50 minutes, 17 secondsexist no such integer such that 0 * b = b * 0 equals the identity one. Right? So for zero um the inverse does not exist.
2:50:272 hours, 50 minutes, 27 secondsSo we can't call this a group. However with addiction was a group. Right? So
2:50:342 hours, 50 minutes, 34 secondsthe distinction is very important. The same set can behave very differently depending on what operations we put on it.
2:50:422 hours, 50 minutes, 42 secondsAnother examples would be ZN with addiction. So what is ZN here? ZN
2:50:492 hours, 50 minutes, 49 secondsis basically a subset from zero to N minus one. Uh but the addiction
2:50:562 hours, 50 minutes, 56 secondshere is not the ordinary addiction. Uh we know. So in here we first add numbers
2:51:032 hours, 51 minutes, 3 secondsand take the remainder modulo n. So uh for example in z3
2:51:122 hours, 51 minutes, 12 seconds1 + 1 = 2 1 + 0 = 1 right but 1 + 2 does not
2:51:192 hours, 51 minutes, 19 secondsequals 3 because 3 is not in the set. We have to take the remainder modulo 3. So
2:51:242 hours, 51 minutes, 24 seconds1 + 2 equ= 3 / 3 modulo is zero in this
2:51:302 hours, 51 minutes, 30 secondsset. So for example um in Z5 with addiction is this a group? Uh yes
2:51:392 hours, 51 minutes, 39 secondsit's a group because the operation plus is associative and that is zero such that 0 + a= a + 0 equals a. So zero here
2:51:492 hours, 51 minutes, 49 secondsis the identity element and for each every element in Z5 an inverse exists.
2:51:552 hours, 51 minutes, 55 secondsFor example, if you pick um one four exist as an inverse because if you plus one and four and take remainder modul 5
2:52:042 hours, 52 minutes, 4 secondsthis is zero modulo 5 right. Uh if you pick uh numbers like two three is an
2:52:112 hours, 52 minutes, 11 secondsinverse because 2 + 3 = 3 + 2 = 0 modulo 5. So in general ZN
2:52:212 hours, 52 minutes, 21 secondswith addiction uh this is of course addiction and then taking the remainder modal n this is a group and using this
2:52:292 hours, 52 minutes, 29 secondsZN we can make a new group uh for example Z3 product Z4 uh this is a cartian product
2:52:392 hours, 52 minutes, 39 secondshere how do we define addiction so um this forms a group and we define
2:52:462 hours, 52 minutes, 46 secondsaddiction like This a1 b1 plus a2 b2
2:52:542 hours, 52 minutes, 54 secondsequals so a1 + a2 uh we take a remainder divided by three.
2:53:012 hours, 53 minutes, 1 secondSo a1 a2 modulo 3 b1 + b2
2:53:082 hours, 53 minutes, 8 secondsmodulo 4. So for example if you add one comma 2
2:53:142 hours, 53 minutes, 14 secondswith uh one comma 3 you get 2 comma 5
2:53:222 hours, 53 minutes, 22 secondsmodule 4 = 1. Another examples 2 comma 1 2a 2 plus uh 2 comma
2:53:322 hours, 53 minutes, 32 seconds3. This is equal to one because 2 + 2 is four and four modulo 3 is 1 and 2 + 3 =
2:53:412 hours, 53 minutes, 41 seconds5 and 5 modulo 4 is one. So this becomes 1 comma 1 and this is indeed uh again an
2:53:482 hours, 53 minutes, 48 secondselement of Z3 uh product Z4. So this addiction is well defined here in this set and since this is associative and
2:53:572 hours, 53 minutes, 57 secondsthere is an element identity element which is 0 comma 0 and for each every element you pick here that is an inverse
2:54:052 hours, 54 minutes, 5 secondsfor example you pick I don't know 2 comma 2 and what is an inverse element of this 1 comma 2 is an inverse element
2:54:132 hours, 54 minutes, 13 secondsright 2 + 1 module 3 equals 0 2 + 2 module 4 equals zero so this forms a
2:54:192 hours, 54 minutes, 19 secondsgroup and in general Z N Z MM is a group and if you add more group for example I
2:54:272 hours, 54 minutes, 27 secondsdon't know Z N1 PO Z N2 P Z N3 and so on
2:54:342 hours, 54 minutes, 34 secondsand so on this also forms a group and general linear group remember
2:54:412 hours, 54 minutes, 41 secondsgeneral linear group collection of matrices with um nonzero determinant so collection of invertible matrices is
2:54:512 hours, 54 minutes, 51 secondsso you take a general linear group with multiplication and this is still a group uh because first is multiplication well
2:54:592 hours, 54 minutes, 59 secondsdefinfined? Yes, because you pick any two invertible matrices and you multiply them.
2:55:092 hours, 55 minutes, 9 secondsThe result is also invertible because determinant A equals determinant A
2:55:192 hours, 55 minutes, 19 secondsdeterminant B and since A and B is in this group uh determinant A and determinant B uh both is not zero right
2:55:262 hours, 55 minutes, 26 secondsso this is not zero which means that A is also invertible so AB is still in this set so multiplication here uh in
2:55:342 hours, 55 minutes, 34 secondsthis set is well defined and we know that matrix multiplication is associative and that is an identity element such that this holds and for
2:55:422 hours, 55 minutes, 42 secondseach a an inverse uh inverse here here is inverse matrix right and every
2:55:502 hours, 55 minutes, 50 secondselement in here has an inverse matrix because uh literally it's a definition right general linear group it was the
2:55:572 hours, 55 minutes, 57 secondsset of um invertible matrices and similarly uh special linear group
2:56:052 hours, 56 minutes, 5 secondsuh with multiplication is a group and remember uh nth root of unity
2:56:132 hours, 56 minutes, 13 secondsuh if I define mu n as the collection of complex numbers satisfying z to the n
2:56:212 hours, 56 minutes, 21 secondsequals 1 and if we take mu n and multiplication this is still a group because uh first
2:56:292 hours, 56 minutes, 29 secondsis multiplication well definfined yes because if z1 and z2 are element of mu
2:56:382 hours, 56 minutes, 38 secondsZ1 Z2 is also an element from UN because if we take this to the nth power this
2:56:452 hours, 56 minutes, 45 secondsbecomes Z1 to the N Z to the N and this is equals to one. So Z1 and Z2 Z1 Z2 is
2:56:522 hours, 56 minutes, 52 secondsa element of mu n and we know that multiplication is associative and that
2:56:592 hours, 56 minutes, 59 secondsis one identity element here 1 to the^ of n equals 1. So one is in this set and
2:57:052 hours, 57 minutes, 5 secondsfor every um Z in mu n is there an inverse element? Yes. Because um
2:57:142 hours, 57 minutes, 14 secondsone over Z is still in the set right. Uh so we can call this a group. When we talk about a group technically we should specify both the set and the operation.
2:57:262 hours, 57 minutes, 26 secondsSo the honest notation would be something like this set and the binary operation. But people do not always say
2:57:332 hours, 57 minutes, 33 secondsthem both time. If the operation is obvious, we usually just say the set. Um for example, if I say R is a group, then
2:57:412 hours, 57 minutes, 41 secondsyou should immediately think, okay, um they probably mean are with addiction subgroup. It's a very similar concept
2:57:482 hours, 57 minutes, 48 secondswith subspace or subset. It's basically a smaller group sitting inside a larger group. So a subset H of a group G is
2:57:562 hours, 57 minutes, 56 secondscalled subgroup if H itself is a group under the operation of G. And we write uh like this HG.
2:58:052 hours, 58 minutes, 5 secondsUh so some examples of subgroup uh Z is a subgroup of Q. Uh of course
2:58:122 hours, 58 minutes, 12 secondsthe binary operation here is the addiction.
2:58:172 hours, 58 minutes, 17 secondsuh special linear group with matrix multiplication
2:58:232 hours, 58 minutes, 23 secondsis subgroup of general linear group with multiplication because both are group itself under
2:58:312 hours, 58 minutes, 31 secondsmultiplication and special linear group is a subset of general linear group. Uh that's why we can call this a subgroup
2:58:382 hours, 58 minutes, 38 secondsof this group. Uh and another example would be mu4.
2:58:462 hours, 58 minutes, 46 secondsA is a subgroup of mu2 because these both are a group under multiplication and mu4 is a subgroup of mu2.
2:58:572 hours, 58 minutes, 57 secondsNow let's talk about cyclic groups. The idea is very simple. Sometimes an entire group can be generated by just one
2:59:042 hours, 59 minutes, 4 secondselement. That means if we start from one element and keep applying the given uh
2:59:102 hours, 59 minutes, 10 secondsbinary operations and again and again so on and so on and eventually we get
2:59:192 hours, 59 minutes, 19 secondsevery element of a group. Um when this happens we call the group cyclic.
2:59:252 hours, 59 minutes, 25 secondsSo a group G is cyclic if it can be generated by a single element. uh and we write g equals um this I don't know what
2:59:342 hours, 59 minutes, 34 secondsto call this a and this is all the collection of a to the n um here a to the n does not mean ordinary
2:59:422 hours, 59 minutes, 42 secondsmultiplication it means applying the given uh group operation repeatedly n times so uh n a to the n uh this means
2:59:512 hours, 59 minutes, 51 secondsmeans you apply the uh binary operation n times so some examples of cyclic group
2:59:582 hours, 59 minutes, 58 secondsz is cyclic uh with generator one and also minus one because like if you pick seven seven is
3:00:083 hours, 8 secondsobtained by adding one seven times.
3:00:133 hours, 13 secondsUm another examples um ZN is also cyclic with generative one and minus one.
3:00:213 hours, 21 secondsUh however um Z7 is also a cyclic group but other than
3:00:283 hours, 28 secondsone and minus one three can be also generated because three if you add three
3:00:343 hours, 34 secondsone times is three two times it becomes six and you add three and it becomes uh nine and 9 modulo 7 is two right? two uh
3:00:443 hours, 44 seconds2 + 3 5 + 3 8 which is 1 modulo 7 and 1 + 3 = 4
3:00:513 hours, 51 secondsuh and 4 + 3 = 7 which is zero and this is
3:00:583 hours, 58 secondsZ7. We got all the elements by just adding up three. So three is a generator of cyclic group Z7 and mu is a cyclic
3:01:083 hours, 1 minute, 8 secondsgroup with generator 2 pi i n uh 2 pi i
3:01:143 hours, 1 minute, 14 secondsover n uh because the element of this group uh is the form of e to 2 pi i n
3:01:233 hours, 1 minute, 23 secondstimes k. Okay. So to understand the group we need to understand how the elements interact under that operation.
3:01:313 hours, 1 minute, 31 secondsOne way to do is to make an operation table. For example, let's look at Z3.
3:01:383 hours, 1 minute, 38 secondsSo Z3 we had uh three elements 0 1 and two. 0 1 2. And let's make an operation table uh like this.
3:01:553 hours, 1 minute, 55 secondsSo here uh the given operation was uh plus and you take the remainder module
3:02:003 hours, 2 minutes3. So 0 + 0 = 0 0 + 1 1 0 + 2 2 1 + 0 1
3:02:063 hours, 2 minutes, 6 seconds1 + 1 2 uh 1 + 2 = 3 but 3 mod 3 equals 0. So this is zero. Uh so two 0 2 + 2 =
3:02:163 hours, 2 minutes, 16 seconds4 and four mod 3 = 1. Okay. Uh so this was a group under uh adding and then you
3:02:253 hours, 2 minutes, 25 secondstake the main module 3 and on the other hand let's look at mu3 mu3 was the group of third group of
3:02:343 hours, 2 minutes, 34 secondsunity and it had three elements one e to the power of 2 pi i over 3 e to the
3:02:413 hours, 2 minutes, 41 secondspower of 4 pi i over 3 1 So let's make an operation table.
3:02:593 hours, 2 minutes, 59 secondsSo this was a group under multiplication. So 1 * 1 = 1. This is equal to two uh e to the 3 pi i over 3 e
3:03:093 hours, 3 minutes, 9 secondsto the 4 pi i over 3.
3:03:153 hours, 3 minutes, 15 secondsE to the 4 pi i over 3.
3:03:203 hours, 3 minutes, 20 secondsUm e to the 2 pi i. This is equals to one. E to the 4 pi i over 3. And e to
3:03:273 hours, 3 minutes, 27 secondsthe 6 pi r 3. This is one. And e to the 8 pi i over 3. And this is equal to e to the 2 pi i over 3.
3:03:403 hours, 3 minutes, 40 secondsSo let's look at this table side by side. Um if we match zero from z3 and
3:03:483 hours, 3 minutes, 48 secondsone from mu3 and one and e to the 2 pi i over 3 two here and e to the 4 pi i over
3:03:553 hours, 3 minutes, 55 seconds3. What happens? So we match zero here and one one here
3:04:043 hours, 4 minutes, 4 secondsand e to the 2 pi i over 3 and two here we match with e to the 4 pi i over 3.
3:04:163 hours, 4 minutes, 16 secondsSo we had zero here, here, and here, here, and here. Um, zero
3:04:223 hours, 4 minutes, 22 secondscorresponds to one, right? One, one, one,
3:04:313 hours, 4 minutes, 31 secondsone, one. Oh, and uh, there's one more zero here.
3:04:393 hours, 4 minutes, 39 secondsand one here one corresponds one corresponds to e to
3:04:473 hours, 4 minutes, 47 secondsthe 2 pi i over 3. So here here here um and here
3:05:023 hours, 5 minutes, 2 secondsand lastly um two here corresponds to e to the 4 pi over 3. two here. It's here, here, here, here, and here.
3:05:123 hours, 5 minutes, 12 secondsWe can find e to the 4 pi i over 3 here in the right table.
3:05:193 hours, 5 minutes, 19 secondsSo notice that the same color sits in same relative positions in the two table. So we have red here, here and
3:05:283 hours, 5 minutes, 28 secondsblue, blue and mint. If you erase all the number and just leave the color, the two tables will be completely same,
3:05:353 hours, 5 minutes, 35 secondsright? But again the two group has nothing in common. Uh Z3 it has 012 as an element and mu3 it even has an
3:05:433 hours, 5 minutes, 43 secondscomplex number as an element and this was a group under addiction and this was a group under multiplication. So completely different group with
3:05:513 hours, 5 minutes, 51 secondscompletely different element and completely different binary operations but it has exactly the same structure.
3:05:573 hours, 5 minutes, 57 secondsSo the actual names of the elements does not matter in this case. What matters is how the elements combine and interact
3:06:053 hours, 6 minutes, 5 secondswith each other. If two groups have the same operation structure after relabeling the elements um they are
3:06:123 hours, 6 minutes, 12 secondscalled isomorphic. So in this case we call these two groups isomeorphic. So
3:06:203 hours, 6 minutes, 20 secondswe write Z3 is isomorphic to mu3. Remember the examples we looked at?
3:06:293 hours, 6 minutes, 29 secondsWe saw that Z3 and mu3 uh was a different group but we saw that they had the same structure. We so we call them
3:06:373 hours, 6 minutes, 37 secondsisomeorphic. But how did we know? We drew two operations table compared them and matched the elements like this. So
3:06:443 hours, 6 minutes, 44 secondswe matched zero from Z3 side to one in mu3 and we matched one from Z
3:06:533 hours, 6 minutes, 53 seconds3 with E to the 2 pi I over 3 and two with E to the 4 pi I over 3 and this and
3:07:033 hours, 7 minutes, 3 secondsthis matching can be viewed as a function and from this matching or function we know that these two groups are isomeorphic. So what condition
3:07:123 hours, 7 minutes, 12 secondsshould this function satisfies? So um this is called an isomorphism.
3:07:173 hours, 7 minutes, 17 secondsIsomorphism from a group G to group G prime is a function that goes from G to G prime that satisfies these two
3:07:253 hours, 7 minutes, 25 secondscondition. First uh five should be byjection meaning that it should be one to one correspondence and second five preserves the operation.
3:07:353 hours, 7 minutes, 35 secondsuh doing the operations in the original word and then sending the result is the same as sending the elements first and
3:07:433 hours, 7 minutes, 43 secondsthen doing the operations in the new word. So the function doesn't randomly just match elements. It matches them in a way that respect the operations. The
3:07:523 hours, 7 minutes, 52 secondsrelative positions in the table were all the same. Remember we we did the coloring. So an isomorphism is a structure preserving by ejection between
3:07:593 hours, 7 minutes, 59 secondsgroups. And if there exist a isomorphism between two groups then we say the two groups are isomeorphic. So some examples
3:08:073 hours, 8 minutes, 7 secondsof isomorphisms C under addiction is isomeorphic to R².
3:08:143 hours, 8 minutes, 14 secondsHow do we know? How do we know? Because we can find an isomorphism.
3:08:193 hours, 8 minutes, 19 seconds5 a + b i if I define this phi to be a comma b this is an isomorphism because
3:08:263 hours, 8 minutes, 26 secondsfirst is this function by ejection is it one to one and on2 yes it is one to uh is is a bjection and second does this
3:08:343 hours, 8 minutes, 34 secondspreserve the operations um so let's see uh five
3:08:413 hours, 8 minutes, 41 secondsa1 + b 1 i plus a2 + b2 I so it's doing the
3:08:493 hours, 8 minutes, 49 secondsoperation first and then sending to R squ right and this is equal to 5 A1 + A2
3:08:563 hours, 8 minutes, 56 secondsplus B1 + B2 I right and by definition this is A1 + A2 comma B1 + B2 and this
3:09:073 hours, 9 minutes, 7 secondsis the same as A1 comma B1 plus A2 comma
3:09:123 hours, 9 minutes, 12 secondsB2 and this is equal to 5 A1 + B1 I + 5
3:09:193 hours, 9 minutes, 19 secondsA2 + B2 I. So rule number two holds which means that this preserves the operation five preserves the addiction.
3:09:283 hours, 9 minutes, 28 secondsSo we can call this uh isomorphism and we know that C is isomorphic to R squ.
3:09:363 hours, 9 minutes, 36 secondsUm another example would be um R under addiction is isomorphic to R plus uh
3:09:453 hours, 9 minutes, 45 secondswhich is the positive real numbers under multiplication. This is also a group because we can define five X equals E to
3:09:553 hours, 9 minutes, 55 secondsthe power of X. Uh of course five goes from this group to this group. Um because because phi is a bjection and it
3:10:043 hours, 10 minutes, 4 secondspreserves the operation. Well, why did preserve the operation? Because 5 x1
3:10:113 hours, 10 minutes, 11 seconds+ x2 equals e to the x1 + x2, right? And this is equal to e to the x1 e to the x2
3:10:193 hours, 10 minutes, 19 secondswhich is 5 x1 5 x2. So it satisfies. So this is a
3:10:273 hours, 10 minutes, 27 secondsisomeorphism. Uh so we know that these two groups are isomeorphic.
3:10:333 hours, 10 minutes, 33 secondsAnd lastly uh Z4 is isomorphic to uh
3:10:393 hours, 10 minutes, 39 secondsmu4 because there's an isomorphism Z five that goes from Z4
3:10:463 hours, 10 minutes, 46 secondsto mu4 such that 5k equals uh
3:10:533 hours, 10 minutes, 53 secondsik and this is an isomeorphism. So we know that these two are isomorphic. uh in general uh ZN is isomorphic
3:11:043 hours, 11 minutes, 4 secondsto mu n. Now that we have learned the idea of isomorphism, we can start thinking in a new way. If two groups are
3:11:123 hours, 11 minutes, 12 secondsisomeorphic, then structurally they're the same, right? The symbols may be different, the elements may be different, the binary operations may be
3:11:203 hours, 11 minutes, 20 secondsdifferent, but as groups they have the same structure. So naturally we can ask can we classify groups up to
3:11:273 hours, 11 minutes, 27 secondsisomorphism. In other words can we make a list of possible group structures where we do not distinguish groups that
3:11:353 hours, 11 minutes, 35 secondsare essentially the same. For general groups this is extremely difficult but for finitely generated a billion group
3:11:423 hours, 11 minutes, 42 secondsthat is a beautiful answer and this is called the fundamental theorem of finitely generate a billion group. So for every finitely generated a billion
3:11:503 hours, 11 minutes, 50 secondsgroup G uh we haven't learned this finely generated a billion group yet but uh just think of this as um finite
3:11:573 hours, 11 minutes, 57 secondsaelion group. Okay so this is isomorphic to a direct product of cyclic groups of the form that looks like this. So every
3:12:063 hours, 12 minutes, 6 secondsfinitely generated aellant group is isomeorphic to a direct product of cyclic group. So for example um we know
3:12:143 hours, 12 minutes, 14 secondsnothing about G. uh G is a group and we know that G is a billion
3:12:213 hours, 12 minutes, 21 secondsand the order of G is 12. But from this theorem we can see that but from this
3:12:303 hours, 12 minutes, 30 secondstheorem we know that G has a structure of Z4 product Z3 or
3:12:383 hours, 12 minutes, 38 secondsZ2 product Z2 product Z3 because every fitly generated a group has the form of
3:12:463 hours, 12 minutes, 46 secondsthis structure. Now we learn about cassettes. Suppose we have group G and a subgroup H. A cassette is when we get
3:12:543 hours, 12 minutes, 54 secondswhen we take the subgroup h and shift it by an element of g. So um it's a collection of all h a's when h is an
3:13:023 hours, 13 minutes, 2 secondselement of h and a is a fixed uh element of g. So you take every element of h do the operation by a and the left and
3:13:113 hours, 13 minutes, 11 secondscollect all the result. Um for example 5z is a subgroup of z. So what are some
3:13:203 hours, 13 minutes, 20 secondscassettes of 5C? If we take a equals 1 and make a cassette using one and 5C,
3:13:283 hours, 13 minutes, 28 secondsthis is um the collection of uh 1 6 11 16 blah blah. And how about um 2 + 5 z?
3:13:403 hours, 13 minutes, 40 secondsThis is 2 7 uh 12 17 22 blah blah. And
3:13:473 hours, 13 minutes, 47 secondsif we take I don't know um 11 11 + 5 Z
3:13:553 hours, 13 minutes, 55 secondsthis is equal to min -4 1 6 11 16 blah blah but this is the same as this set
3:14:033 hours, 14 minutes, 3 secondsright so 1 + 5 Z is equal to 11 + 5 Z and also it's equal to 6 + 5 Z and we
3:14:133 hours, 14 minutes, 13 secondscan also take uh uh 21 for example 21 + 5 Z and blah blah blah. So the way we represent this cassette is not unique.
3:14:223 hours, 14 minutes, 22 secondsIt depends on which representative we choose. So 1 + 5 Z we have this one big set and we can choose one as a
3:14:303 hours, 14 minutes, 30 secondsrepresentative and 11 as representative, six as a representative and 21 as a representative. So a cassette is usually
3:14:383 hours, 14 minutes, 38 secondsnot a subgroup but the important thing is that they partition the subgroup. For example, um let's look at all the
3:14:453 hours, 14 minutes, 45 secondscassettes of 5Z. So 1 + 5 Z is this 2 + 5 Z and you also have 3 + 5 Z uh which
3:14:523 hours, 14 minutes, 52 secondsis basically all the natural numbers that has remainder three when divided more to five. So -2 3 8 13
3:15:033 hours, 15 minutes, 3 seconds18 these kinds of numbers. And how about 4 + 5 Z
3:15:093 hours, 15 minutes, 9 seconds-1 4 9 14 and 0 + 5 Z this is just equals to 5 Z
3:15:183 hours, 15 minutes, 18 secondsmultiples of five. So - 10 - 5 0 5 10 blah blah blah.
3:15:283 hours, 15 minutes, 28 secondsSo if you see here, notice that uh the cusettes of 5Z partition Z, right? Um if
3:15:363 hours, 15 minutes, 36 secondsyou draw a diagram here, 5 Z, 5 Z + 1,
3:15:453 hours, 15 minutes, 45 seconds5 Z + 2, 5 Z + 4,
3:15:503 hours, 15 minutes, 50 seconds5 Z + uh 5, which is 5 Z + 3. Okay,
3:15:583 hours, 15 minutes, 58 secondslike this the cosets of 5 Z 5 Z 5 Z plus 1 5 Z plus 2 5 Z plus 3 5 Z plus4 they
3:16:053 hours, 16 minutes, 5 secondspartition uh Z u and this happens all the time for example
3:16:143 hours, 16 minutes, 14 secondsif I look at Z8 uh so G is Z8 and if I take this subgroup
3:16:213 hours, 16 minutes, 21 seconds0 comma 4 this is a subgroup uh the set of h. So we have h and we have 1 + h
3:16:293 hours, 16 minutes, 29 secondsright? This is equals to 1 comma 5.
3:16:363 hours, 16 minutes, 36 secondsAnd we also take two as a representative and made a cassette that has two and six
3:16:423 hours, 16 minutes, 42 secondsas an element and three plus h equals 37. And this four cassettes of age partition the original group Z8.
3:16:543 hours, 16 minutes, 54 secondsAnother example Z12 and if we take a cassette 048
3:17:043 hours, 17 minutes, 4 secondsH = 048 and if we take element one so 1 + H is
3:17:133 hours, 17 minutes, 13 secondsequal to 59 and 2 + H is
3:17:213 hours, 17 minutes, 21 seconds2 6 10 and finally You take three as a representative you get 371.
3:17:293 hours, 17 minutes, 29 secondsSo these four cassettes of the subgroup H forms a partition of the original group Z12.
3:17:393 hours, 17 minutes, 39 secondsJust before we talked about cassettes if H was a subgroup of G then the cassettes of H split the group G into disjoint
3:17:453 hours, 17 minutes, 45 secondspieces. So here we define G SN as the set of cassettes made by subgroup N. uh
3:17:533 hours, 17 minutes, 53 secondswe read this G mod N. So instead of looking at individual elements of G, we can also look at these larger pieces
3:18:013 hours, 18 minutes, 1 secondwhich is uh cassettes made by a certain subgroup. So let's slow down a little bit and think about what Z mod 5Z is
3:18:083 hours, 18 minutes, 8 secondstrying to do. So Z mod 5Z. So this is a set of cassette made by 5Z which is 5Z
3:18:183 hours, 18 minutes, 18 seconds5 Z + 1. Of course this 5 Z + 1 is same as 5 Z + 6 5 + 11. It depends on the
3:18:253 hours, 18 minutes, 25 secondsrepresentative right 5 Z + 2 5 Z + 3 5 Z + 4. So instead of
3:18:353 hours, 18 minutes, 35 secondstreating uh 1 6 11 16 blah blah blah into different integers we put them on one box uh which is 5 Z + one.
3:18:463 hours, 18 minutes, 46 secondsIn the same way, all integers with the same remainder model fives are grouped into the same box. Just before we talked about cassettes, if H is a subgroup of G
3:18:563 hours, 18 minutes, 56 secondsand the cassette of H split the group G into disjoint pieces. So here we define G/N
3:19:033 hours, 19 minutes, 3 secondsas the set of cassettes made by subgroup N and we read this as uh G mod N. So
3:19:103 hours, 19 minutes, 10 secondsinstead of looking at individual elements of G, we can also look at these larger pieces. So let's slow down a little and see uh what Z mod 5Z is
3:19:193 hours, 19 minutes, 19 secondstrying to do. So Z mod 5Z is a set of uh cassettes made by 5 Z. So 5Z,
3:19:293 hours, 19 minutes, 29 seconds5Z + 1, 5 Z + 2, 5 Z + 3, 5 Z + 4. And we know that these five cassettes split uh Z.
3:19:423 hours, 19 minutes, 42 secondsAnd of course 5 Z + 1 is equal to 5 Z + 6. then 5 Z z + 11. It depends on what representative we choose. So here its elements are not single numbers anymore.
3:19:543 hours, 19 minutes, 54 secondsSo instead of treating um 1 6 11 16 - 4 uh as different integers, we put them into one box and we name that 5 Z + one.
3:20:063 hours, 20 minutes, 6 secondsRight? Uh in the same way, all integers with the same remainder modulo 5 are grouped into the same box. For example,
3:20:133 hours, 20 minutes, 13 secondsintegers with uh three modulo 5 are in this box. Integrate with remainder four when divided to five are in this element
3:20:203 hours, 20 minutes, 20 seconds5 z + 4. So z mod 5z is basically this five remainder classes modul 5. Now this should feel very close to z5.
3:20:373 hours, 20 minutes, 37 secondsIn z5 we also only care about the remainders 0 1 2 3 4. Right? So we want this five cassettes to behave like Z5.
3:20:463 hours, 20 minutes, 46 secondsUm so we feel like Z mod 5Z to be a group isomorphic to Z5. We feel like 5Z
3:20:533 hours, 20 minutes, 53 secondsis related to zero and 5 Z 1 with one, 5 Z plus with two and 5 Z + 4 with four.
3:21:023 hours, 21 minutes, 2 secondsBut if we want cassettes to form a group, we need an operations between cassettes, right? Uh to be a group, we
3:21:093 hours, 21 minutes, 9 secondsneed elements and operation. uh we have elements here but we never define operations between cassettes right um so
3:21:173 hours, 21 minutes, 17 secondshow do we define operations between cassettes the most natural idea would be
3:21:233 hours, 21 minutes, 23 secondsif we have cassettes a n and bn we define the operation by multiplying the
3:21:313 hours, 21 minutes, 31 secondsrepresentatives uh a b here is the representatives so 5z um if we add 5 z plus I don't know
3:21:403 hours, 21 minutes, 40 seconds5 z + 2 and 5 Z + 4. We define this operation by
3:21:493 hours, 21 minutes, 49 secondsapplying the operation to the representative of two cassettes. So 2 + 4 and we make a cassettes uh with the new representative. So 2 + 4 equals 1.
3:22:013 hours, 22 minutes, 1 secondSo this uh equals 1 + 5 Z. So defining an operations between cassettes like
3:22:083 hours, 22 minutes, 8 secondsthis G mod N actually forms a group and here uh Z mod 5Z is isomorphic to Z5 but
3:22:183 hours, 22 minutes, 18 secondshere I missed a little detail uh it says normal subgroup here right so what is a normal subgroup well G mod N becomes a
3:22:273 hours, 22 minutes, 27 secondsgroup if and only if N is a normal subgroup but in this lecture I'm not going to go deeply into what normal
3:22:343 hours, 22 minutes, 34 secondsnormal subgroup means uh the reason is that most of the examples we will use are actually normal anyway. So we don't have to really care about uh a group
3:22:433 hours, 22 minutes, 43 secondsbeing normal. Now let's go back to the idea of isomorphism. An isomorphism was a map between two groups that satisfies
3:22:513 hours, 22 minutes, 51 secondstwo condition. First it had to be by ejection. It had to be one to one and onto and second it had to preserve the group
3:22:593 hours, 22 minutes, 59 secondsstructure which means that uh five a b equals 5 a star prime 5b. Now the
3:23:083 hours, 23 minutes, 8 secondsquestion is that what happens if we remove the bjection addition and that we call it homorphism. So homorphism is a
3:23:173 hours, 23 minutes, 17 secondsuh map between groups that only preserves the group operation. So only this formula holds. So a homorphism is a
3:23:253 hours, 23 minutes, 25 secondsmap that respects the structure of the group. So what are some examples of homorphism? Of course all isomorphisms are homorphisms.
3:23:353 hours, 23 minutes, 35 secondsAnd uh if we take phi that goes from z to z. We define five n as 2n. This is a
3:23:443 hours, 23 minutes, 44 secondshomorphism because uh well it might not be an isomorphism because this is not a bjection but it preserves the group
3:23:503 hours, 23 minutes, 50 secondsstructure because five n1 + n2 = 2 n1 +
3:23:563 hours, 23 minutes, 56 seconds2 n2 and this is 2 n1 + 2 n2 and this is 5 n1 + 5 n2.
3:24:073 hours, 24 minutes, 7 secondsHow about if I define phi that goes from general linear group to
3:24:163 hours, 24 minutes, 16 secondsuh uh without zero. So this is a multiplicative group and I'll define 5 A as determinant A.
3:24:273 hours, 24 minutes, 27 secondsThis is a homorphism because 5 A of course A and B is an element of general
3:24:343 hours, 24 minutes, 34 secondslinear group. by AB equals uh determinant AB
3:24:413 hours, 24 minutes, 41 secondsand because determinant can be splitted like this determinant A determinant B
3:24:483 hours, 24 minutes, 48 secondsthis is 5 A 5 B so it is called an homorphism
3:24:573 hours, 24 minutes, 57 secondsnow that we've defined homorphisms we can define kennel and image again this is almost the same idea as we saw in linear transformations
3:25:053 hours, 25 minutes, 5 secondsSo for a linear transformation the con was the set of vectors that got sent to zero. For a group homorphism the kernel
3:25:133 hours, 25 minutes, 13 secondsis a set of group elements that get sense to the identity element. So the collection of g uh that satisfies 5g
3:25:213 hours, 25 minutes, 21 secondsequals e prime. Uh e prime is a a identity element and the image is the
3:25:283 hours, 25 minutes, 28 secondsset of all possible outputs. Uh so nothing special. Um so some examples if
3:25:343 hours, 25 minutes, 34 secondsI define phi that goes from z to c and I'll define phi n as
3:25:423 hours, 25 minutes, 42 seconds3n. What is the kernel and image? So kernel phi would be the collection of n
3:25:503 hours, 25 minutes, 50 secondsuh such that 3 n equals zero. So kernel would be just zero vector. And how about
3:25:573 hours, 25 minutes, 57 secondsthe image of five? image is the all possible outputs of 3 n. So it's a multiple of
3:26:063 hours, 26 minutes, 6 secondsthree uh which is 3z.
3:26:103 hours, 26 minutes, 10 secondsAnd how about if I define five that goes from r squ to r and I'll define five x comm y as x
3:26:203 hours, 26 minutes, 20 seconds+ y. The kernel would be the collection of x comm y that satisfies x + y equals zero. So it will
3:26:303 hours, 26 minutes, 30 secondsbe a form of uh one and minus one. So x and y has the same absolute value but different signs. Uh so a is real number.
3:26:413 hours, 26 minutes, 41 secondsHow about image five?
3:26:453 hours, 26 minutes, 45 secondsUh actually image uh this can be any real number. If you pick any number any real number and you can find x comma y
3:26:523 hours, 26 minutes, 52 secondssuch that x + y equals that real number we picked. So image five equals the set of real numbers.
3:27:023 hours, 27 minutes, 2 secondsSo far we have studied groups as object by themselves. But very often groups becomes useful because they act on
3:27:083 hours, 27 minutes, 8 secondssomething else. The elements of a group can be thought as a transformation of some set and this idea is very important
3:27:173 hours, 27 minutes, 17 secondswhen it comes to gala theories or modular forms. So uh let's look at group actions and G set. A set X is called a G
3:27:263 hours, 27 minutes, 26 secondsset. If there is a map and this map is called the group action uh and this map takes one elements from G one elements
3:27:333 hours, 27 minutes, 33 secondsfrom X and it gives one elements uh back in X and it has to satisfy the following. First uh E star X should be
3:27:423 hours, 27 minutes, 42 secondssame as X for all element in X and second uh this formula should hold for
3:27:483 hours, 27 minutes, 48 secondsall G1 G2 and X. So some examples um if I take G as the addictive group of
3:27:573 hours, 27 minutes, 57 secondsintegers and X as R and R will define uh N* X= N + X.
3:28:083 hours, 28 minutes, 8 secondsUh first of all is X a G set? Um we should check if these two rule holds.
3:28:163 hours, 28 minutes, 16 secondsFirst uh identity element of this group is zero right? Zero star X is it X? Yes. Uh
3:28:263 hours, 28 minutes, 26 secondsbecause uh the definition of star is adding these two. This is equal to X.
3:28:313 hours, 28 minutes, 31 secondsAnd second uh does this uh equation holds? Uh let's see.
3:28:453 hours, 28 minutes, 45 secondsSo n1 + n_sub_2* x is it equal to um n1 star
3:28:553 hours, 28 minutes, 55 secondsuh g2* x. So n2* x but yes this holds because star here
3:29:023 hours, 29 minutes, 2 secondsis the same as addiction right and um addiction the associivity law holds because of so obviously this works. So
3:29:113 hours, 29 minutes, 11 secondswe can call X a G set and this uh operation particularly is called a group action.
3:29:203 hours, 29 minutes, 20 secondsAnother example, I will look at G uh real number addictive group and I will take X as R²
3:29:303 hours, 29 minutes, 30 secondsand I will define uh theta X comma Y uh with the matrix multiplication
3:29:383 hours, 29 minutes, 38 secondscosine theta minus sin theta sin theta cosine theta X Y. This is a
3:29:483 hours, 29 minutes, 48 secondsvery famous group action. If you check these two rules, you can see that this satisfies which means that we can call x
3:29:553 hours, 29 minutes, 55 secondsa g set and this uh theta function as a group action. Uh this is actually a transformation of rotating x comma y by
3:30:043 hours, 30 minutes, 4 secondstheta by the origin. So what does it mean? uh for examples uh I want to rotate
3:30:113 hours, 30 minutes, 11 secondsthe point uh 2 comma 1 by I don't know 60° and we want to know the coordinates of
3:30:193 hours, 30 minutes, 19 secondsthis uh rotated point uh then uh I put theta as 60° in this matrix
3:30:263 hours, 30 minutes, 26 secondsmultiplication so if I take theta as 60° uh cosine 60° = 1 /2 minus square /
3:30:363 hours, 30 minutes, 36 seconds2 square / 2 1 / two and x = 2 and y = 1. So if I uh compute
3:30:463 hours, 30 minutes, 46 secondsthe matrix multiplication, it becomes 1 - square / 2 square 3 + 1 / 2.
3:30:563 hours, 30 minutes, 56 secondsSo the new coordinates the rotated coordinates will be 1 - square / 2
3:31:033 hours, 31 minutes, 3 seconds2 over 1 /2. So this is very useful.
3:31:083 hours, 31 minutes, 8 secondsSo a group action lets us study a group by watching how it moves or transforms elements of another set. And this is
3:31:153 hours, 31 minutes, 15 secondsvery important because many abstract group become much easier to understand when we see what they act on.
3:31:243 hours, 31 minutes, 24 secondsNow once you have a group action there's a very natural question we can ask. If we start from one element X where can
3:31:313 hours, 31 minutes, 31 secondsthe group move it? In other words, um if we have X, of course, this is a element
3:31:383 hours, 31 minutes, 38 secondsof the G set and we let every element of G act on this X. So X can be moved
3:31:453 hours, 31 minutes, 45 secondsaround. So for example, if we take G2 and let G2 act in X, uh it means that we
3:31:523 hours, 31 minutes, 52 secondsuh do the operations with G2 and X and this is another element in X, right? So X can be moved around using elements in
3:32:013 hours, 32 minutes, 1 secondG. So G1 it can be moved around here using GN this could be moved around here like G7
3:32:093 hours, 32 minutes, 9 secondsthis X could be uh moved to another elements in X. So if we collect all these possible outcomes
3:32:183 hours, 32 minutes, 18 secondsthese set is called the orbit of X. So if X is a G set the orbit of X looks
3:32:253 hours, 32 minutes, 25 secondslike this. all the possible collection of G star X for all G and G.
3:32:323 hours, 32 minutes, 32 secondsUh this means take all group elements G, apply them to X and collect all points you can reach. So the orbit is a set of
3:32:403 hours, 32 minutes, 40 secondsall positions that are reachable from X using the group action. Orbit is not the whole set X in general because it's the
3:32:483 hours, 32 minutes, 48 secondsonly part of X that's connected to X through the action of G. Some atoms may be reachable from X, some may not be. Uh without further ado, let's look at some examples.
3:32:583 hours, 32 minutes, 58 secondsSo here's some group actions examples.
3:33:013 hours, 33 minutes, 1 secondUh this is the examples we just saw. We know that this is a G-r and this is a group action. So this coordinate plane
3:33:083 hours, 33 minutes, 8 secondsdenotes R squ which is a G set. So if we pick any element from this coordinate.
3:33:173 hours, 33 minutes, 17 secondsSo where can this point move under the action of G. So the group action is shifting x coordinate by n. So this
3:33:253 hours, 33 minutes, 25 secondspoint uh can be moved to this point and this point can be also moved to this point if you shift the x coordinate by
3:33:323 hours, 33 minutes, 32 secondstwo and also uh it can be moved to these kind of points. Right?
3:33:413 hours, 33 minutes, 41 secondsSo this infinitely many points uh this point forms a orbit uh that includes
3:33:483 hours, 33 minutes, 48 secondsthis point and you can pick any point from the coordinate plane and there's an orbit including that point. So if we
3:33:563 hours, 33 minutes, 56 secondspick this point, this is the orbit that includes this point.
3:34:123 hours, 34 minutes, 12 secondsUh we pick this point and there is an orbit for this point.
3:34:223 hours, 34 minutes, 22 secondsSo here same color means same orbits. And the orbit can cover the whole set.
3:34:283 hours, 34 minutes, 28 secondsIn other words, the set can be partitioned into orbit. Um if you do this fit infinitely many times, this orbit will fill up the entire coordinate plane. Right?
3:34:393 hours, 34 minutes, 39 secondsAnd here if we pick point x comma y, the group action moves this point around the origin. Right? So as theta changes uh
3:34:483 hours, 34 minutes, 48 secondsover all real numbers the points moved around a circle because this point can be moved to this point and also this
3:34:553 hours, 34 minutes, 55 secondspoint and if I take theta as pi / two uh this point can move to this point and also this point this point and so on. So
3:35:033 hours, 35 minutes, 3 secondsthese uh these points lie on a circle like this. So the orbit that includes
3:35:103 hours, 35 minutes, 10 secondsthis point forms a circle around the center and the origin and you could pick another point and the
3:35:193 hours, 35 minutes, 19 secondsorbit that includes this point is also a circle.
3:35:273 hours, 35 minutes, 27 secondsUm another orbit if you pick this point the orbit uh including the point will be like this.
3:35:503 hours, 35 minutes, 50 secondsinfinitely many uh circles.
3:35:573 hours, 35 minutes, 57 secondsSo if you do this infinitely many times uh infinitely many circles will cover the whole coordinate plane. So the entire set is partitions into orbit.
