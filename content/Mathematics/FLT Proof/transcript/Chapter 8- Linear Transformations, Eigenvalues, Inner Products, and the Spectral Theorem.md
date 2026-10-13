Chapter 8: Linear Transformations, Eigenvalues, Inner Products, and the Spectral Theorem
2:02:292 hours, 2 minutes, 29 secondssingle vector space now we move on to functions defined between distinct vector spaces so um t goes from V to W.
2:02:392 hours, 2 minutes, 39 secondsThis means that T takes a vector from vector space V and it gives a vector from vector space W.
2:02:482 hours, 2 minutes, 48 secondsUh but among all possible functions between these two vector spaces, some functions are especially nice and these
2:02:562 hours, 2 minutes, 56 secondsare called linear transformation. So a linear combination is a function that goes from vector space 3 to vector space
2:03:032 hours, 3 minutes, 3 secondsw that preserves vector space operations which means that t cx + y = ctx + ty.
2:03:132 hours, 3 minutes, 13 secondsUh so um let's look at this equation.
2:03:182 hours, 3 minutes, 18 secondsIf you put um x and y equals zero and c
2:03:242 hours, 3 minutes, 24 seconds= 1, what do we get? uh c tt 0 equals uh t 0
2:03:332 hours, 3 minutes, 33 secondsplus t 0. So we know that for uh you take any linear transformation and t 0
2:03:402 hours, 3 minutes, 40 secondsequals z. This means that takes uh zero vectors from v and sends it to the zero vector to w. Right?
2:03:512 hours, 3 minutes, 51 secondsAnd now I would put c = 1 in this equation.
2:03:572 hours, 3 minutes, 57 secondsSo we get t x + y = tx + ty.
2:04:062 hours, 4 minutes, 6 secondsUh then I'll put y as zero. We get t cx equals um ctx plus t0. But t 0 equals z.
2:04:192 hours, 4 minutes, 19 secondsSo it's just ctx.
2:04:222 hours, 4 minutes, 22 secondsNotice that t preserves uh addiction here and t preserves scalar multiplication here. And there were two
2:04:292 hours, 4 minutes, 29 secondsoperation defined in vector spaces, right? Scarlet multiplication and addiction. That's why here I wrote uh t preserves vector space operations. Okay.
2:04:392 hours, 4 minutes, 39 secondsSo let's look at some examples. T that goes from r squ to r squ. And I will
2:04:462 hours, 4 minutes, 46 secondsdefine t x comm y as 2x 3 y. Uh first
2:04:532 hours, 4 minutes, 53 secondsoff this is obviously a function satis uh connecting these two vector spaces.
2:04:592 hours, 4 minutes, 59 secondsBut is it a linear transformation? To find out we uh test if this satisfies this equation. So
2:05:082 hours, 5 minutes, 8 secondst uh we'll pick any c and two vectors from r squ c x1 x2 + y1 y2.
2:05:212 hours, 5 minutes, 21 secondsUh this is equal to cx1 + y1 cx2 + y2.
2:05:292 hours, 5 minutes, 29 secondsRight?
2:05:302 hours, 5 minutes, 30 secondsAnd by definition of t this is equals to 2 cx1 + 2 y1
2:05:392 hours, 5 minutes, 39 seconds3 cx2 + 3 y2 and this is equal to c 2x1
2:05:492 hours, 5 minutes, 49 seconds2x2 plus uh 2 i1
2:05:562 hours, 5 minutes, 56 seconds2 i2 and this is uh actually equals to t
2:06:002 hours, 6 minutesx1 x2 plus t y1 and y2. So comparing
2:06:082 hours, 6 minutes, 8 secondsthese two this equation holds. So we know that this is a linear transformation.
2:06:142 hours, 6 minutes, 14 secondsUm some other examples of the transformation t that goes from r 2 to r
2:06:252 hours, 6 minutes, 25 secondstx comma y equals I don't know uh minus y
2:06:322 hours, 6 minutes, 32 secondsuh minus y. This is a linear transformation.
2:06:352 hours, 6 minutes, 35 secondsand uh t from p to r
2:06:432 hours, 6 minutes, 43 secondsr and uh tfx is defined as uh f0 zero.
2:06:512 hours, 6 minutes, 51 secondsUh this is also a linear transformation.
2:06:542 hours, 6 minutes, 54 secondsYou can check that if this uh definition of t satisfies this uh rule. Another
2:07:012 hours, 7 minutes, 1 secondexample T that goes from 2x two matrix to R
2:07:092 hours, 7 minutes, 9 secondsand I will define T A B CD as A + D. This is also a linear transformation.
2:07:192 hours, 7 minutes, 19 secondsUh but but if I define C t that goes
2:07:242 hours, 7 minutes, 24 secondsfrom R 2 to R square and T X comma Y as
2:07:312 hours, 7 minutes, 31 secondsuh X + 1 comma Y. This is not a linear transformation because um can find any
2:07:382 hours, 7 minutes, 38 secondscounter examples like t 1 comma 1 = 2 comma 1 right tn 0 comma 1 equals 0
2:07:462 hours, 7 minutes, 46 secondscomma 1 uh 1 comma 1 and if you add this two um t one comma 2 should equal to the
2:07:542 hours, 7 minutes, 54 secondssum of these two which is 3 comma 2 right but this uh doesn't hold so this is not a linear transformation
2:08:022 hours, 8 minutes, 2 secondsum similarly If you define t that goes from r² to r and you define t x comm y
2:08:112 hours, 8 minutes, 11 secondsas the product of the two uh this is not a linear transformation kernel and image of a linear transformation.
2:08:192 hours, 8 minutes, 19 secondsSo what is a kernel? Kennel is the set of all vectors in V that are sent to zero vectors in W.
2:08:302 hours, 8 minutes, 30 secondsAn image of t is uh basically the set of all possible outcomes of the t or possible outputs of t.
2:08:392 hours, 8 minutes, 39 secondsUh some examples. Consider the map that goes from r 2 to r 2 and t x y is
2:08:492 hours, 8 minutes, 49 secondsdefined as um x + y comma zero. Um if you test this this is uh a this is a
2:08:582 hours, 8 minutes, 58 secondslinear transformation right. Um so what is a kernel of this linear transformation? So kernel we want this
2:09:062 hours, 9 minutes, 6 secondsto be zero vector right 0 comma 0. Uh so the kernel of this linear transformation
2:09:142 hours, 9 minutes, 14 secondswould be the collection of vectors satisfying x + y
2:09:222 hours, 9 minutes, 22 secondsequals zero. So we can write this as vectors of the form min - x comma x
2:09:322 hours, 9 minutes, 32 secondswhere x is real number. And what is the image of this linear transformation?
2:09:412 hours, 9 minutes, 41 secondsUm actually the image
2:09:492 hours, 9 minutes, 49 secondslooks like this right any x comma zero form can be made by this linear transformation. Some other examples.
2:09:592 hours, 9 minutes, 59 secondsUh if I define t that goes from rx again real number a real coefficients
2:10:072 hours, 10 minutes, 7 secondspolomial to rx and I define tp as p prime. So
2:10:162 hours, 10 minutes, 16 secondswhat is the kernel of this linear transformation? So we want p prime to be zero which means that p has to be a constant function right.
2:10:272 hours, 10 minutes, 27 secondsSo the kettle of t is uh a constant.
2:10:372 hours, 10 minutes, 37 secondsAnd how about image? Image of t.
2:10:432 hours, 10 minutes, 43 secondsUh the image of t is actually rx itself, right?
2:10:512 hours, 10 minutes, 51 secondsbecause the indefinite integral of uh any polomial is still in rx.
2:10:582 hours, 10 minutes, 58 secondsNow we connect two ideas that we have already seen. We learn about matrices and we learn about linear transformations.
2:11:062 hours, 11 minutes, 6 secondsU one important fact in linear algebra is that every linear transformation can be uniquely represented by a matrix once
2:11:152 hours, 11 minutes, 15 secondswe choose a basis for v and w. Um, of course, a linear transformation itself is not literally a matrix, right? It was
2:11:242 hours, 11 minutes, 24 secondsa function defined between two vector spaces. But if we choose a vector u, if we choose a basis for v and if we choose
2:11:342 hours, 11 minutes, 34 secondsa basis for w, then we can describe the action of the linear transformation
2:11:392 hours, 11 minutes, 39 secondsusing a matrix. Um, so how does this work? First, let's choose a basis for v
2:11:472 hours, 11 minutes, 47 secondsand w. So for V I will choose the basis as V1 V2 uh blah blah blah V N. So the
2:11:552 hours, 11 minutes, 55 secondsdimension of V is N. For W the basis would be something like uh W1 small W1 small W2 to W.
2:12:082 hours, 12 minutes, 8 secondsSo the dimension of the vector space W is M.
2:12:122 hours, 12 minutes, 12 secondsUm so if I pick any vector from V this can be uniquely represented by the
2:12:192 hours, 12 minutes, 19 secondslinear combinations of the basis of v right so it's like a1 v1 plus a2 v2 plus
2:12:272 hours, 12 minutes, 27 secondsbaba a n vn so if we look at uh so if you apply the
2:12:342 hours, 12 minutes, 34 secondstar transformation so if we apply t to v what happens pins
2:12:422 hours, 12 minutes, 42 secondsa1 v1 plus a2 v2 plus blah blah blah a n v 3 n. Okay.
2:12:522 hours, 12 minutes, 52 secondsAnd since t is a linear transformation, we can split this and make it simple
2:12:582 hours, 12 minutes, 58 secondslike this. A1 T V1 A2 T V2
2:13:072 hours, 13 minutes, 7 secondsA N T VN like this. And uh T was a linear
2:13:142 hours, 13 minutes, 14 secondstransformation that sends a vector from V to a vector from W. Right? So TV v1
2:13:212 hours, 13 minutes, 21 secondsthrough TV VN is a member of W. This is an element of W.
2:13:272 hours, 13 minutes, 27 secondsAnd since we chose a basis for W, we can represent this TV v1, TV2, TVN uh with the linear combination of the basis.
2:13:362 hours, 13 minutes, 36 secondsRight? So A1 um I will write
2:13:442 hours, 13 minutes, 44 secondsB11 W1 plus B12 W2 plus
2:13:522 hours, 13 minutes, 52 secondsB1 M W. Okay. Plus A2
2:14:012 hours, 14 minutes, 1 secondB21 W1 plus B2 W2 plus
2:14:082 hours, 14 minutes, 8 secondsB 2 M W.
2:14:132 hours, 14 minutes, 13 secondsIf you go till the end, plus a n
2:14:182 hours, 14 minutes, 18 secondsbn1 w1 plus b n2 w2 plus all the way up to bn m wm.
2:14:302 hours, 14 minutes, 30 secondsUh so we want to simplify this and we want to look at uh particularly the coordinates or the coefficients of the
2:14:382 hours, 14 minutes, 38 secondsw1's w2s wm right and consider this matrix multiplication
2:14:482 hours, 14 minutes, 48 secondsuh a1 a2
2:14:562 hours, 14 minutes, 56 secondsa n here we have B11,
2:15:052 hours, 15 minutes, 5 secondsB21, E12, B22, B32,
2:15:112 hours, 15 minutes, 11 secondsall the way up to B uh N2
2:15:192 hours, 15 minutes, 19 seconds1 M B 2 M over
2:15:262 hours, 15 minutes, 26 secondsB N M. So here this is a um
2:15:332 hours, 15 minutes, 33 secondsm byn matrix and this is a n by one matrix and the result should be
2:15:442 hours, 15 minutes, 44 secondsa n by one matrix and it would be the uh coefficients uh the collection of coefficients of w1s
2:15:532 hours, 15 minutes, 53 secondsthrough wm right you can compute this and For example, the first entry will be
2:16:002 hours, 16 minutessomething like a1 b11 plus a2 b 2 plus blah blah blah plus a n bn1. And if you
2:16:102 hours, 16 minutes, 10 secondslook at this, this is actually the coefficients of w1, right? A1 b1 a2 b 2
2:16:162 hours, 16 minutes, 16 secondsa n bn1. Okay, so we can actually treat this matrix as the matrix uh representing this linear transformation.
2:16:272 hours, 16 minutes, 27 secondsUm if you look at some uh real world examples, t goes from r cube to r cube and if I
2:16:372 hours, 16 minutes, 37 secondsdefine tx comma y comma z = tx + y + z c + x, I can represent the
2:16:472 hours, 16 minutes, 47 secondst with matrix multiplication like
2:16:552 hours, 16 minutes, 55 secondsthis. So you can say that um this matrix represent this linear transformation. So
2:17:032 hours, 17 minutes, 3 secondsif this feels too technical and complicated, you don't have to know all the details. But I need you to remember that the linear transformation can be
2:17:112 hours, 17 minutes, 11 secondsrepresented as a matrix once we choose a basis for V and W. Now we're going to be looking at values and igen vectors.
2:17:192 hours, 17 minutes, 19 secondsSuppose we have a linear transformation that goes from V to V. So here the domain and the co-domain are the same
2:17:272 hours, 17 minutes, 27 secondsvector space. An igen vector is a special vector whose direction doesn't
2:17:332 hours, 17 minutes, 33 secondschange under t. More precisely uh the igen vector is a vector such that
2:17:412 hours, 17 minutes, 41 secondstv equals lambda v for some scar value lambda. The direction of v does not
2:17:482 hours, 17 minutes, 48 secondschange after applying t. an igen vector and IG value generally comes as a pair.
2:17:552 hours, 17 minutes, 55 secondsSo what do I mean by that? If v_sub_1 is an igen vector of this linear transformation there exist lambda 1 such
2:18:042 hours, 18 minutes, 4 secondsthat t v1 equals lambda 1 v1 right so the associated value for v1 is lambda 1.
2:18:112 hours, 18 minutes, 11 secondsSo lambda 1 and v1 we can make a pair of them and there could be more than one vector. So this would be something as uh
2:18:212 hours, 18 minutes, 21 secondslike lambda 2 v2. So v_sub_2 and lambda 2 and you can find these uh pairs. So
2:18:292 hours, 18 minutes, 29 secondsvalues and vectors comes in a pair like this. Some examples t that goes from r 2 to r 2.
2:18:392 hours, 18 minutes, 39 secondsConsider tx comma y = 2x comma 3 y. um one comma 0
2:18:492 hours, 18 minutes, 49 secondsis an igen vector. Why? Because if you apply t one comma 0, this becomes 2 comma 0 and this is a multiple of 1
2:18:592 hours, 18 minutes, 59 secondscomma 0. So igen vector here is this vector and igen value here is two and there's one more igon vector to this uh
2:19:072 hours, 19 minutes, 7 secondslinear transformation which is 0 comma 1 because t 0 comma 1 equals 0 comma 3
2:19:152 hours, 19 minutes, 15 secondsand this is uh 3 * 0 comma 1. So 0 comma 1 is an vector and three is an igen value.
2:19:232 hours, 19 minutes, 23 secondsUm another examples um P goes from C infinite R
2:19:322 hours, 19 minutes, 32 secondsto C infinite R. Um we haven't looked at this previously. This is a vector space uh that contains uh infinitely
2:19:402 hours, 19 minutes, 40 secondsdifferentiable functions. Okay. And I'll define T F as the derivative of F. Um if
2:19:522 hours, 19 minutes, 52 secondsI put ex the derivative of ex
2:19:582 hours, 19 minutes, 58 secondsis ex right so um ex here this is the
2:20:032 hours, 20 minutes, 3 secondsigon vector and one is a igon value uh e to the 3x
2:20:122 hours, 20 minutes, 12 secondsthis is also on vector and three here is the value uh
2:20:192 hours, 20 minutes, 19 secondsbut if you put like any function This normally doesn't work. So if you
2:20:262 hours, 20 minutes, 26 secondsput t sinx and the result is cosine x and this is obviously not a multiple of sin x right.
2:20:342 hours, 20 minutes, 34 secondsSo sin x is not a vector of this linear transformation and we can also define values and
2:20:432 hours, 20 minutes, 43 secondsvectors for a matrix similarly for what we did for a linear transformation. So if a is a n byn matrix and if there
2:20:522 hours, 20 minutes, 52 secondsexists a vector uh a non-zero vector that is an fn so this is a n by one uh matrix
2:21:012 hours, 21 minutes, 1 secondcolumn vector that satisfies a v equals lambda v for some number lambda
2:21:102 hours, 21 minutes, 10 secondsv is called igen vectors and lambda is called value. So uh some examples
2:21:192 hours, 21 minutes, 19 secondsif I take a as a 2x2 matrix 7 2 -4 1 uh
2:21:262 hours, 21 minutes, 26 seconds1 comma minus one is a value of this matrix vector of this matrix because if
2:21:332 hours, 21 minutes, 33 secondsyou compute the matrix multiplication we have five and minus4 minus uh 1 = -5.
2:21:422 hours, 21 minutes, 42 secondsSo the direction did not change after applying the matrix multiplication. So here 1 comma minus one is a uh vector
2:21:512 hours, 21 minutes, 51 secondsand five is an igon value. Uh actually one more vector to this matrix
2:22:002 hours, 22 minutes1 comma minus 2 is an vector because uh if you compute the multiplication this
2:22:082 hours, 22 minutes, 8 secondsis 3 - 4 - 2 6. So this is a multiple of
2:22:152 hours, 22 minutes, 15 secondsthe vector 1 comma minus 2. So three here is an igon value and 1 comma minus 2 is an ig vector here. And we can also
2:22:242 hours, 22 minutes, 24 secondsfind igen values and igen vectors for a 3x3 matrix. uh if I take a prime equals
2:22:312 hours, 22 minutes, 31 seconds8 m - 13 7
2:22:352 hours, 22 minutes, 35 secondsuh 3 - 6 5 3 - 9 8 uh the vector 1 comma
2:22:442 hours, 22 minutes, 44 seconds1 comma 1 is a vector for this matrix because if you compute the multiplication
2:22:522 hours, 22 minutes, 52 secondsuh you have two uh two uh third row first column right so two
2:23:022 hours, 23 minutes, 2 secondsand this is a multiple of 11 one so here 111 is an igen vector and two is an igen
2:23:082 hours, 23 minutes, 8 secondsvalue now the question is how do we find the igen value and ig vector for a given
2:23:152 hours, 23 minutes, 15 secondsmatrix for given matrix A we want to find lambda and v such that a v equals
2:23:222 hours, 23 minutes, 22 secondslambda v of course uh v is a column vector
2:23:282 hours, 23 minutes, 28 secondsand lambda is a scalar and v is non zero right because in the definition of
2:23:372 hours, 23 minutes, 37 secondsvector uh it says that vector should not be a zero vector okay
2:23:442 hours, 23 minutes, 44 secondsuh and I will write the right hand side using the identity matrix like this and
2:23:532 hours, 23 minutes, 53 secondsI will move this 10 to the left and uh factor out the v. So we have a minus
2:24:002 hours, 24 minuteslambda i v equals zero.
2:24:072 hours, 24 minutes, 7 secondsUm wait um in this equation if a minus lambda i has an inverse what happens if
2:24:162 hours, 24 minutes, 16 secondsa minus lambda i has an inverse we can multiply the inverse on both sides which means that a minus lambda i minus one a
2:24:252 hours, 24 minutes, 25 secondsminus lambda i 3 = a minus lambda i zero the right hand side is zero and this
2:24:342 hours, 24 minutes, 34 secondsis identity Right? So I V equals V and the right side is zero. So V automatically becomes zero. But we don't
2:24:432 hours, 24 minutes, 43 secondswant V to be zero. Right? So we don't want A minus lambda I to have a inverse.
2:24:502 hours, 24 minutes, 50 secondsMeaning that we want A minus lambda I uh to be not invertible and we had a special function to
2:24:592 hours, 24 minutes, 59 secondsdetermine whether matrix is invertible or not and that was a determinant.
2:25:042 hours, 25 minutes, 4 secondsSo since we want a minus lambda i to be not invertible, we want the determinant
2:25:112 hours, 25 minutes, 11 secondsof a minus lambda i equals zero. So in order to find values and vectors of a
2:25:192 hours, 25 minutes, 19 secondsgiven matrix a, we would solve this equation for lambda and find lambda such that determinant of a minus lambda i
2:25:282 hours, 25 minutes, 28 secondsequals zero. So uh this determinant a minus lambda i is
2:25:352 hours, 25 minutes, 35 secondsgenerally a polomial of lambda and we call this the characteristic polomial of
2:25:412 hours, 25 minutes, 41 secondsa okay so the example we just saw a was equal to 7 2 - 4 1 okay so what is the
2:25:512 hours, 25 minutes, 51 secondscharacteristic polomial of this matrix so determinant a minus lambda i equals Equals
2:25:592 hours, 25 minutes, 59 secondsdeterminant 7 - lambda 2 - 4 1 - lambda and this is equal to 80 minus bc right.
2:26:092 hours, 26 minutes, 9 secondsSo lambda squar - 8 lambda + 7
2:26:142 hours, 26 minutes, 14 seconds+ 8 so this is 15 right and this could be factorized into lambda minus 3 lambda
2:26:222 hours, 26 minutes, 22 secondsminus 5 so we have lambda= 3 and five and this is actually the value we uh we
2:26:282 hours, 26 minutes, 28 secondssaw right so this characteristic polomis actually works for finding value now
2:26:362 hours, 26 minutes, 36 secondslet's talk about a slightly different quantity attached to matrix and this one is called the trace. Um the trace is
2:26:432 hours, 26 minutes, 43 secondsmuch simpler than the determinant and it's only defined for square matrices.
2:26:492 hours, 26 minutes, 49 secondsSo um the trace of a n byn matrix a denoted by trace a is the sum of its diagonal entries. So this is very easy.
2:26:592 hours, 26 minutes, 59 secondsUh we take all the entries in the diagonal and we just add them. So for example, if A is the matrix that looks
2:27:082 hours, 27 minutes, 8 secondslike this, the trace of A is equal to 1
2:27:142 hours, 27 minutes, 14 seconds+ A. So this is nine. Uh if B is a 3x3 matrix
2:27:222 hours, 27 minutes, 22 seconds7 0 - 4 the trace of B
2:27:292 hours, 27 minutes, 29 secondsuh we add one five and minus four. So this is two. It's very easy.
2:27:362 hours, 27 minutes, 36 secondsUh and this is how we compute a trace of a matrix.
2:27:402 hours, 27 minutes, 40 secondsSo similar similar matrices. What it means by two matrices being similar? Let A and B uh be n byn matrices over a
2:27:492 hours, 27 minutes, 49 secondsfield f and a is said to be similar to b if there exists an invertible n byn
2:27:562 hours, 27 minutes, 56 secondsmatrix p such that b equals uh inverse p a and p.
2:28:032 hours, 28 minutes, 3 secondsAt first this formula may look a little artificial but the meaning is important.
2:28:092 hours, 28 minutes, 9 secondsSimilar matrices represent the same linear transformation just written different bases. Uh remember when we
2:28:162 hours, 28 minutes, 16 secondsrepresent a linear transformation as a matrix the matrix depends on the choice of basis right we chose the basis for V
2:28:242 hours, 28 minutes, 24 secondsand we chose the basis for W. So the matrix changed because the coordinate system changed but the underlying linear
2:28:312 hours, 28 minutes, 31 secondstransformation is the same and this is why similar matrices share many important properties. Uh so if A and B
2:28:402 hours, 28 minutes, 40 secondsare similar matrices the determinant are the same and the traces are the same and even they have the same characteristic polomials and values.
2:28:522 hours, 28 minutes, 52 secondsUm so let's look at some examples. If A is a matrix of 2 1 03,
2:29:032 hours, 29 minutes, 3 secondsB is a matrix of 3 2 0 2. We know that A and B are similar
2:29:122 hours, 29 minutes, 12 secondsbecause there exist P such that uh this equation holds and P uh
2:29:222 hours, 29 minutes, 22 secondslooks like this. So if you compute this uh we know that A and B are similar. Uh and about the determinant of A and B are
2:29:302 hours, 29 minutes, 30 secondsthey the same? Yes, they're the same because they have both uh six as determinant. And how about the trace?
2:29:382 hours, 29 minutes, 38 secondsBoth matrices have five as the trace, right? So their traces are the same. And the characteristic polomial
2:29:472 hours, 29 minutes, 47 secondsum the characteristic polomial of a is uh characteristic pol of a equals
2:29:552 hours, 29 minutes, 55 secondsdeterminant 2 minus lambda 1 03 minus lambda right and this is equal to lambda
2:30:032 hours, 30 minutes, 3 secondssquare minus first squar + 6 characteristic polomial of p equals
2:30:102 hours, 30 minutes, 10 secondsdeterminant 3 minus lambda 2 0 2 minus lambda and this is equal to lambda^ 2 -
2:30:182 hours, 30 minutes, 18 seconds5 lambda + 6 and this is the same when people talk about vectors in
2:30:282 hours, 30 minutes, 28 secondsphysics they usually mean vectors in r square or r cube right so that we can
2:30:362 hours, 30 minutes, 36 secondsdraw them as arrows and once you have arrows we can talk about their length and the angle between them and whether
2:30:432 hours, 30 minutes, 43 secondstwo vectors are perpendicular right a cartisian plane if we pick um arrow 3
2:30:522 hours, 30 minutes, 52 secondscomma 2 the length of the arrow is square 13 and the uh theta right
2:30:592 hours, 30 minutes, 59 secondsthe tangent theta is 2 over 3 so we can do this kind of geometric uh stuff here
2:31:072 hours, 31 minutes, 7 secondsso all of this is usually done using the dot product for example in
2:31:142 hours, 31 minutes, 14 secondsR to the n. The dot product is defined as um x1 x2 x3
2:31:222 hours, 31 minutes, 22 secondsxn dot y1 y2 power yn equals x1 y1 + x2
2:31:312 hours, 31 minutes, 31 secondsy2 plus all the way up to x and yn.
2:31:362 hours, 31 minutes, 36 secondsUsing this we can measure length because um we can define a length of a vector as
2:31:432 hours, 31 minutes, 43 secondsa square root of the inner product uh like this right and we say that two vectors are perpendicular
2:31:512 hours, 31 minutes, 51 secondsif the inner product of them is zero for example uh in R squ
2:31:592 hours, 31 minutes, 59 secondsthe vector um I don't know 2A 3 is perpendicular
2:32:062 hours, 32 minutes, 6 secondsto 3 comma minus 2. We know this because if we take a dotproduct of these two vectors,
2:32:142 hours, 32 minutes, 14 secondsthis is 6 - 6 and this is zero. So we know that these two vectors are perpendicular each other. So dot product
2:32:222 hours, 32 minutes, 22 secondslets us talk about length, angle and orthogonality.
2:32:262 hours, 32 minutes, 26 secondsBut now we have seen the vector spaces was not always uh like r squ or r cube, right? We have many other vector spaces.
2:32:332 hours, 32 minutes, 33 secondsanything could be a vector. So it's not immediately clear what it mean for like a polomial to be perpendicular or what
2:32:422 hours, 32 minutes, 42 secondslength of a function should be. And that is why we introduce the idea of an inner
2:32:482 hours, 32 minutes, 48 secondsproduct. An inner product is a function that takes um two vector and it sends uh
2:32:562 hours, 32 minutes, 56 secondsto a scholar uh in here that is the complex number. So you can think inner product as a generalized dotproduct.
2:33:042 hours, 33 minutes, 4 secondsIt's designed to let us talk about geometric ideas inside abstract vector spaces.
2:33:122 hours, 33 minutes, 12 secondsSo for a function to be an inner product it should satisfy these three rules. Uh so first um x and y inner product of x
2:33:212 hours, 33 minutes, 21 secondsand y should equal to the conjugate of y and x. Uh so here uh this is this bar denotes the complex conjugation. So for
2:33:302 hours, 33 minutes, 30 secondsexample the complex conjugation of 3 + 2 I is equal to 3 - 2 I. You've seen this right?
2:33:392 hours, 33 minutes, 39 secondsAnd second inner product should be linear to the uh first coordinate. And
2:33:472 hours, 33 minutes, 47 secondsrule number three says that if you inner product the same vector it should be non- negative. And if the inner product
2:33:542 hours, 33 minutes, 54 secondsof itself is zero, it means uh that x is zero. So if you have a valid inner
2:34:022 hours, 34 minutes, 2 secondsproduct in a vector space, you call that vector space an inner product space.
2:34:072 hours, 34 minutes, 7 secondsInner product space is a vector space equipped with an inner product. And the norm of a vector um you can think of
2:34:152 hours, 34 minutes, 15 secondsnorm as a generalization of length. The norm of a vector is defined as the square root of the inner product with
2:34:232 hours, 34 minutes, 23 secondsitself. And two vector we call them orthogonal if the inner product is zero.
2:34:302 hours, 34 minutes, 30 secondsAnd the orthonormal basis is a basis consisting of mutually orthogonal vectors of norm one. So some examples of
2:34:382 hours, 34 minutes, 38 secondsinner product spaces. Uh the most common one would be the dot product in Rn. If x
2:34:462 hours, 34 minutes, 46 secondsis the vector of x1 x2 through xn and y y1 y2 through yn. The inner
2:34:562 hours, 34 minutes, 56 secondsproduct of x and y is equal to x1 y2 1 x2 y2 plus blah x and yn. This is a value inner product.
2:35:092 hours, 35 minutes, 9 secondsAnd we know this because we can check the three rules we just saw.
2:35:142 hours, 35 minutes, 14 secondsAnd some examples of another inner product spaces.
2:35:192 hours, 35 minutes, 19 secondsIf I take V as uh C minus pi 2 pi, this
2:35:252 hours, 35 minutes, 25 secondsis the vector space of all continuous functions from minus pi
2:35:322 hours, 35 minutes, 32 secondsto pi. And if I define the inner product of two functions as
2:35:412 hours, 35 minutes, 41 secondsminus pi to pi integration
2:35:482 hours, 35 minutes, 48 secondsthis is an inner product. So why is this an inner product? Uh first we need to show that
2:35:562 hours, 35 minutes, 56 secondsthis is equal to conjugation of g comma f. But this is obvious because uh
2:36:052 hours, 36 minutes, 5 secondsuh fg is equal to gf by the definition and we can take a conjugation and it does not do anything because this is a
2:36:132 hours, 36 minutes, 13 secondsreal number right. And the second one uh c f_sub_1 + f_sub_2
2:36:202 hours, 36 minutes, 20 secondsg it has to be equal to c inner product f_sub_1 g plus f_sub_2 g. Um and this
2:36:302 hours, 36 minutes, 30 secondsalso holds because you actually put C f_sub_1 plus f_sub_2 into this. So
2:36:372 hours, 36 minutes, 37 secondsc f_sub_1 + f_sub_2 inner product g equals uh integration
2:36:452 hours, 36 minutes, 45 secondsc f_sub_1 + f_sub_2 gdx and this is equal to minus pi pi
2:36:542 hours, 36 minutes, 54 secondsf_sub_1 g dx plus uh it gets dead here f_sub_2g dx and this is equal to inner
2:37:032 hours, 37 minutes, 3 secondsproduct for f_sub_1 and x and this is equal to inner product of f_sub_2 and x.
2:37:072 hours, 37 minutes, 7 secondsSo this rules and number three is the result of an inner product is non-
2:37:152 hours, 37 minutes, 15 secondsnegative and if this is zero we need to show that f is
2:37:212 hours, 37 minutes, 21 secondszero and this is also obvious. Um if you um take a inner product with itself
2:37:332 hours, 37 minutes, 33 secondsthis is of course non- negative and uh if this is zero we know that f is zero
2:37:392 hours, 37 minutes, 39 secondsin this uh range right so this is an inner product and using this we can
2:37:472 hours, 37 minutes, 47 secondsactually show that uh the function cossine x and sinx X actually they're perpendicular in this vector space
2:37:562 hours, 37 minutes, 56 secondsbecause if we compute this integral this is sinx
2:38:052 hours, 38 minutes, 5 secondscossine x dx right and this is
2:38:112 hours, 38 minutes, 11 secondsequal to sin 2x over 2 dx and uh this is
2:38:212 hours, 38 minutes, 21 secondsum cosine 2x - 4
2:38:262 hours, 38 minutes, 26 seconds- pi pi and it equals zero. So the inner product is zero. So we can say that the
2:38:342 hours, 38 minutes, 34 secondsfunction sin x and cosine x they're perpendicular in this vector space.
2:38:402 hours, 38 minutes, 40 secondsDirect sum of subspaces. Let w1 and w2 be subspaces of a vector space v. And we
2:38:472 hours, 38 minutes, 47 secondswrite V = W1. This this is a O plus sign W1 O + W2. If V = W1 + W2 and W1 and W2
2:38:582 hours, 38 minutes, 58 secondsonly share zero vectors. So what does that actually mean? Because we never defined uh how to add between subspaces.
2:39:052 hours, 39 minutes, 5 secondsRight? It's equivalent to saying every vector V can be written uniquely as V =
2:39:112 hours, 39 minutes, 11 secondsW1 + W2 when W1 is an element of W2 and W2 is a member of W2.
2:39:182 hours, 39 minutes, 18 secondsUm so what does it actually means?
2:39:222 hours, 39 minutes, 22 secondsSometimes vector space can be decomposed into several smaller pieces. It's like breaking one vector space into
2:39:292 hours, 39 minutes, 29 secondsindependent components. Um for example in R squ um so any element of R squ is the form
2:39:382 hours, 39 minutes, 38 secondsof X comm Y right and this is a sum of X comma 0 plus 0 comma Y.
2:39:462 hours, 39 minutes, 46 secondsUm so R square we can write it as a de composition of two subspaces
2:40:012 hours, 40 minutes, 1 second0 comma y when y is a real number.
2:40:092 hours, 40 minutes, 9 secondsThis set is a vector space itself and this set is a vector space and x comma 0 here is an element of this vector space
2:40:162 hours, 40 minutes, 16 secondsand 0 comma y is a element of this vector space and since x comma y can be written as a sum of these two we can say
2:40:242 hours, 40 minutes, 24 secondsthat r squ can be decomposed into these two vector spaces. Another example would be um P2R.
2:40:342 hours, 40 minutes, 34 secondsRemember P2R uh this was a vector space of polomials with real coefficient whose degree was
2:40:422 hours, 40 minutes, 42 secondsmaximum two. Okay. And this is actually a decomposition of
2:40:492 hours, 40 minutes, 49 secondsspan 1 plus span x plus span x². Um, this is pretty obvious
2:40:582 hours, 40 minutes, 58 secondsbecause you pick any element in uh P2R and it looks like this. A + BX plus CX
2:41:062 hours, 41 minutes, 6 secondssqu and A is a member of span one and BX is a member of span X and CX squared is an element of span X squ and the three vector space only shares zero vectors.
2:41:192 hours, 41 minutes, 19 secondsUm one last examples um R squ can be also decomposed into two vector
2:41:262 hours, 41 minutes, 26 secondsspaces such that uh the first one is a form of x 1 comma minus one
2:41:352 hours, 41 minutes, 35 secondsand the second one looks like this uh y one comma 1
2:41:422 hours, 41 minutes, 42 secondsy = r first um all these two vector spaces yes they are vector space this is a vector space and this is a vector
2:41:502 hours, 41 minutes, 50 secondsspace and if you pick any element from R squ can you write that element as the sum of these two vector space? Uh yes
2:42:002 hours, 42 minutesbecause uh if you pick x comma y this is equal to x + y / 2
2:42:112 hours, 42 minutes, 11 seconds1 comma 1 + x - y uh over 2 1 comma minus one. Uh so this
2:42:202 hours, 42 minutes, 20 secondsis a member of this vector space and this is an element of this vector space.
2:42:252 hours, 42 minutes, 25 secondsAnd we know that these two vector space only share zero vectors. So R squ can be decomposed into these two smaller subspaces.
2:42:332 hours, 42 minutes, 33 secondsAnd the last slide of linear algebra is spectral theorem. And honestly at this point it may feel a little bit unmotivated uh but I want to put it here
2:42:422 hours, 42 minutes, 42 secondsbecause it'll come back later in a very important way when we talk about uh modulative forms. This theorem is called the spectral theorem or in this version
2:42:512 hours, 42 minutes, 51 secondsuh simultaneous diagonalization. Um if you Google spectral theorem you'll see so many people talking about different theorems and it's because it has many
2:42:582 hours, 42 minutes, 58 secondsversion of this. Um and we are looking at this particular version. Um the rough idea is that suppose we have a
2:43:052 hours, 43 minutes, 5 secondsdimensional inner product space and we have several linear transformation acting on it. If these transformations are all self adjoined self adjoined
2:43:142 hours, 43 minutes, 14 secondsmeans that um so we have an inner product because we are looking at a inner product space. uh self adjoint
2:43:212 hours, 43 minutes, 21 secondsmeans that these two are the same. So inner product of tiix and y equals inner
2:43:272 hours, 43 minutes, 27 secondsof x and tiy for all xy and v and all t i's and um if the operators commute it means that titj equals tji.
2:43:402 hours, 43 minutes, 40 secondsuh you can think of commutativity. Okay.
2:43:432 hours, 43 minutes, 43 secondsSo if these transformations are all self adjoined and if they commute with each other then we can choose one orthonormal
2:43:502 hours, 43 minutes, 50 secondsbasis that diagonalizes all of them at the same time. This theorem is very powerful because it tells us that under the right condition many different
2:43:592 hours, 43 minutes, 59 secondsoperators can be understood using one common basis.
2:44:032 hours, 44 minutes, 3 secondsChapter three is abstract algebra. Here we go a little deeper into the world of algebra. Remember what I said earlier. I
2:44:112 hours, 44 minutes, 11 secondssaid that the two main object of the video are elliptic curves and modular forms. And one of the most important facts about elliptic curves is that
2:44:202 hours, 44 minutes, 20 secondstheir points form a group. That's the reason why we can view elliptic curves as algebraic objects. So in this chapter
2:44:272 hours, 44 minutes, 27 secondswe study that structure. We started with groups. Then we move on to rings and fields. These are the basic algebraic structure we need before uh elliptic cap
2:44:362 hours, 44 minutes, 36 secondsstart making sense. And finally, we'll also take a glimpse at gala theory. This will become extremely important later because scala representations are one of
2:44:442 hours, 44 minutes, 44 secondsthe most important object that connects between elliptic curves and modular forms.
