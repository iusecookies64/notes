Chapter 6: Matrices, Linear Systems, and Determinants
1:07:031 hour, 7 minutes, 3 secondsfirst object we need is the first object we need is a matrix. A matrix is just a rectangular array of scholars. Um here
1:07:121 hour, 7 minutes, 12 secondsscholars you can just think of numbers and this field f this is a number set.
1:07:201 hour, 7 minutes, 20 secondsYou can just uh think of as a number set where these scholars or numbers comes from.
1:07:291 hour, 7 minutes, 29 secondsSome examples.
1:07:361 hour, 7 minutes, 36 secondsThis is a matrix and this is a 2x two matrix because it has two rows right one two and this has three columns uh two
1:07:441 hour, 7 minutes, 44 secondscolumns one two. So this is a 2x two matrix. uh we write uh like this and we often write uh like this 2x2 matrix.
1:07:561 hour, 7 minutes, 56 secondsThen how about um this matrix 1 2 4 7 I know - 7 - 6.
1:08:051 hour, 8 minutes, 5 secondsThis is a 2x3 matrix because it has one two rows and it has one two three columns. So this is
1:08:141 hour, 8 minutes, 14 secondsa 2x3 matrix. This denotes the number of rows and this uh means the number of columns in the matrix.
1:08:211 hour, 8 minutes, 21 secondsUh so in general m by n matrix a has m rows and n columns. Okay. Uh and the
1:08:291 hour, 8 minutes, 29 secondsentry in the i row and j column is denoted by a iig j. Uh so for example if
1:08:371 hour, 8 minutes, 37 secondsI name this matrix A and um A12
1:08:431 hour, 8 minutes, 43 secondsis the entries in first row second column right the first number it means rows and the second number it means that
1:08:501 hour, 8 minutes, 50 secondsit comes from the second column. So first row second column first row second column. So A12 equals 2. How about then a um 23?
1:09:031 hour, 9 minutes, 3 secondsA 23 is a second row, third column, right? Second row, third column. So it's minus six. Uh how about a one three?
1:09:151 hour, 9 minutes, 15 secondsA13. So first row, third column. So four. And how about a uh 32. This doesn't exist because A is a 2x3 matrix.
1:09:261 hour, 9 minutes, 26 secondsA does it have a third row? Now in this slide I wrote that the entries comes from a field F. So what is a field? I
1:09:351 hour, 9 minutes, 35 secondssaid that it's a number set. Uh a field mathematically is an algebraic structure that we can add, subtract, multiply and divide of course by non-zero elements.
1:09:451 hour, 9 minutes, 45 secondsBut don't worry about the definition of field right now. Um we will talk about fields more carefully later. For now,
1:09:521 hour, 9 minutes, 52 secondsyou can just think of F as where the entries of the matrix or numbers comes from. In this lecture, most of the time,
1:10:001 hour, 10 minutesthis F will be either R or C. Meaning that we'll be only looking at matrices
1:10:071 hour, 10 minutes, 7 secondswith entries from real numbers or complex numbers. For example, um these two matrix are a matrix over R, right?
1:10:171 hour, 10 minutes, 17 secondsBecause the entries are real numbers. Of course, this is a matrix over C, right?
1:10:221 hour, 10 minutes, 22 secondsUm, but this matrix 1 + i - 2 i square
1:10:291 hour, 10 minutes, 29 seconds2 i - 7, this is a matrix over complex number. This is a matrix over c. Well,
1:10:371 hour, 10 minutes, 37 secondsthis matrix pi e1 - 6 over I don't know 30,0001.
1:10:441 hour, 10 minutes, 44 secondsThis is a matrix over r because the entries comes from real number. This is a matrix over C because the entries
1:10:511 hour, 10 minutes, 51 secondscomes from complex number sets. We can define operations on matrix. First matrix addiction is very
1:10:591 hour, 10 minutes, 59 secondsstraightforward. If two matrices have the same size, then we can add them entry by entry. So for example, uh if I
1:11:071 hour, 11 minutes, 7 secondswere to add these two matrix 1 2 3 4 this is a 2x2 matrix and this is also a
1:11:151 hour, 11 minutes, 15 seconds2x2 matrix same size. uh that's why we can add them. So how do we add? We add
1:11:221 hour, 11 minutes, 22 secondscorresponding entries. So 2 + 1 3 3 + 2 5 4 + 3 7 and 1 + 4 5. So the resulting
1:11:321 hour, 11 minutes, 32 secondsmatrix is also the same size as these two matrices. Okay. And subtraction works basically the same. So 1 3 7 4
1:11:421 hour, 11 minutes, 42 secondsminus um - 3 2 0 7 if I compute this subtraction it would be of course the
1:11:501 hour, 11 minutes, 50 secondssame size uh 4 1 7 minus 3 it would be something like this next is scolar
1:11:591 hour, 11 minutes, 59 secondsmultiplication this means multiplying a matrix by a scholar C here C is a scholar just one numbers so you multiply
1:12:081 hour, 12 minutes, 8 secondsone number on a matrix. So how do you do this? Um so if I take any matrix 1 2 3 4 58. So
1:12:171 hour, 12 minutes, 17 secondsthis is a 2x3 matrix. And if you take any scholar um for example minus three and if you multiply this scalar to this
1:12:261 hour, 12 minutes, 26 secondsmatrix you multiply to every possible entries. So the resulting matrix would be the same size as this matrix and it
1:12:361 hour, 12 minutes, 36 secondswill be -3 - 6 - 9 - 12 - 15 - 24. It's
1:12:431 hour, 12 minutes, 43 secondsvery straightforward and easy. Um another examples 7 * 1 7 9 - 8
1:12:521 hour, 12 minutes, 52 secondsit would be 749 63 - 56. It works like this. Now matrix
1:13:001 hour, 13 minutesmultiplication is a little bit complicated. So you might think matrix complication works like this. So if I uh
1:13:071 hour, 13 minutes, 7 secondstake 1 2 3 4 3 4 5 7. You might think that oh if you uh multiply these two matrices you uh multiply corresponding
1:13:171 hour, 13 minutes, 17 secondsterms. So 1 * 3 3 2 4 8 15 24. But matrix multiplication doesn't work like this. So this is not how it's done.
1:13:261 hour, 13 minutes, 26 secondsOkay. So to compute matrix multiplication a b the number of columns in a has to be same as the number of
1:13:351 hour, 13 minutes, 35 secondsrows in b. So if a is a n byn matrix then b should be some matrix of n by uh p matrix. So these n are the same right?
1:13:481 hour, 13 minutes, 48 secondsn was the number of columns in a and n was uh this n was the number of rows in b. So this two should be the same. And
1:13:571 hour, 13 minutes, 57 secondsso if I calculate this A product B, the resulting matrix is a M by P matrix. M
1:14:041 hour, 14 minutes, 4 secondsuh comes from here. It's the number of rows in the matrix A and P is the number of columns in matrix B. Okay.
1:14:131 hour, 14 minutes, 13 secondsSo how do we actually compute this? So the E row of J column of the resulting matrix AB um is computed like this.
1:14:251 hour, 14 minutes, 25 secondsUm so this a i k is the entry of the i row of k e i e i e
1:14:331 hour, 14 minutes, 33 secondsi e i e i e i e i e i e i e i e i row of a right e i row of a and this bkj comes from j
1:14:431 hour, 14 minutes, 43 secondscolumn of b right so we take i both of t a and
1:14:501 hour, 14 minutes, 50 secondsj column of b and we uh multiply corresp responding terms and add them. So let's
1:14:561 hour, 14 minutes, 56 secondslook at some examples. 1 2 3 4 2 4 03.
1:15:071 hour, 15 minutes, 7 secondsSo first of all uh this I will call this matrix A and call this matrix B. A is a
1:15:131 hour, 15 minutes, 13 seconds2x2 matrix and B is a 2x2 matrix. The number of columns in A is the same as number of rows in B. So the resulting
1:15:201 hour, 15 minutes, 20 secondsmatrix would be 2x two matrix and this matrix multiplication we can do it because uh stay in two right
1:15:281 hour, 15 minutes, 28 secondsuh then um the resulting matrix should be 2x2 matrix and what about the uh first
1:15:361 hour, 15 minutes, 36 secondsrow first column entries of the resulting matrix. So first row first column we take first row from A second
1:15:441 hour, 15 minutes, 44 secondsfirst column from B. So first row, first column, first row, first column. So 1 * 2 + 2 * 0. This is two.
1:15:541 hour, 15 minutes, 54 secondsFirst row, second column of the resulting matrix. First row, second column. So 1 * 4, 2 * 3. If you add
1:16:031 hour, 16 minutes, 3 secondsthem, it's 10, right? Second row, first column, second row, first column. 6 + 0, 6. second row, second column, second
1:16:121 hour, 16 minutes, 12 secondsrow, second column, 12 + 12 = 24. Okay, this works like this. Um, how about so
1:16:211 hour, 16 minutes, 21 secondsmatrix A, it's a 2x three matrix, right? Two rows, three
1:16:291 hour, 16 minutes, 29 secondscolumns and matrix B is 3x two matrix, three rows and two column, right? So A
1:16:371 hour, 16 minutes, 37 secondsand B uh so the number of columns in A is the same as number of rows in B. So we can compute this matrix
1:16:441 hour, 16 minutes, 44 secondsmultiplication and the resulting matrix would end up in 2x two matrix. Right?
1:16:491 hour, 16 minutes, 49 secondsThis two comes from here. This two comes from here. So uh first row first column
1:16:561 hour, 16 minutes, 56 secondsfirst row first column. So 3 + 8 minus 3 8 [snorts] first row uh second column first row
1:17:061 hour, 17 minutes, 6 secondssecond column first row second column 2 - 8 + three uh plus zero 2 - 8 + 0 - 6.
1:17:181 hour, 17 minutes, 18 secondsUh second row first column second row first column 12 + 20 - 6. So is it 26 12
1:17:301 hour, 17 minutes, 30 seconds20 minus 6
1:17:361 hour, 17 minutes, 36 seconds12 + 20 - 6 uh yes it's 26
1:17:421 hour, 17 minutes, 42 secondsuh second row second column 8 - 20 + 0 so 8 - 20 = -12
1:17:511 hour, 17 minutes, 51 secondsand in general matrix multiplication is not commutative meaning that AB is not equals to PA. So you cannot change the order of multiplication.
1:18:031 hour, 18 minutes, 3 secondsBut uh the surprising thing is that matrix multiplication is associative meaning that we can regroup the
1:18:101 hour, 18 minutes, 10 secondsmultiplication. A B C equals A multiply the matrix multiplication B C. So this works. Uh we will not going to prove
1:18:181 hour, 18 minutes, 18 secondsthis but we can check that these uh hold right.
1:18:241 hour, 18 minutes, 24 secondsUh so maybe we can pick any matrix ABC uh 2x2 matrix 1 2 3 4 I don't know I'm
1:18:321 hour, 18 minutes, 32 secondschoosing any random numbers minus 2 3 - one 1 2 - 2 okay so first we will going
1:18:421 hour, 18 minutes, 42 secondsto compute these this first and this gives us uh -4
1:18:501 hour, 18 minutes, 50 seconds1 + 6 is 7 second row first column - 8.
1:18:551 hour, 18 minutes, 55 secondsSecond row, second column. So 3 + 12 is 15.
1:19:011 hour, 19 minutes, 1 secondAnd if you um do the multiplication one more time, we have first row, first
1:19:071 hour, 19 minutes, 7 secondscolumn, uh 18. Is it right? I think it's right. First row, second column - 4 -4 - 18. Second row, first column, uh 38.
1:19:201 hour, 19 minutes, 20 secondsSecond row, second column, minus 38. Okay.
1:19:261 hour, 19 minutes, 26 secondsSo, uh now we will going to regroup this
1:19:331 hour, 19 minutes, 33 secondsuh by doing these multiplication first.
1:19:381 hour, 19 minutes, 38 secondsOkay. And it becomes okay. We had 1 2 3 4 and 2
1:19:451 hour, 19 minutes, 45 seconds- 2 uh 2 + 6 8 - 2 - 6 - 8
1:19:541 hour, 19 minutes, 54 secondsand this is equal to 2 +
1:19:581 hour, 19 minutes, 58 seconds16 oh it's 18 oh - 2 minus uh 16 it's -
1:20:051 hour, 20 minutes, 5 seconds18 6 + 32 38 8 - 6 - 32 - 38. So it's the
1:20:161 hour, 20 minutes, 16 secondssame. So we check that matrix multiplication is associative. Some types of matrices. First, a square
1:20:241 hour, 20 minutes, 24 secondsmatrix. What is a square matrix? A square matrix is a matrix where the number of rows equals the number of
1:20:301 hour, 20 minutes, 30 secondscolumns. So generally an n byn matrix is a square matrix. Number of row equals
1:20:371 hour, 20 minutes, 37 secondsthe number of columns. So this is a square matrix. This is a 2x2 matrix, right? Same row, same column.
1:20:451 hour, 20 minutes, 45 secondsAnd - 76 uh 77 0 - 61.
1:20:551 hour, 20 minutes, 55 secondsThis is a 3x3 matrix. So this is a square matrix.
1:21:001 hour, 21 minutesAnd zero matrix. Zero matrix is a matrix where all entries are zero and it acts as the addictive identity which means
1:21:091 hour, 21 minutes, 9 secondsthat we can pick any matrix and add to the zero matrix and we get the same matrix back. So um for example
1:21:201 hour, 21 minutes, 20 secondsthis is a 2x3 zero matrix and if we pick
1:21:251 hour, 21 minutes, 25 secondsany other 2x3 matrix 1 5 - 6 0 1 2 and of course because the all of the entries
1:21:341 hour, 21 minutes, 34 secondsof the zero matrix are zero. This is equal to uh the matrix we picked 012.
1:21:421 hour, 21 minutes, 42 secondsUh so this is why we call zero matrix as the addictive identity. This zero matrix acts like the zero we see in ordinary
1:21:501 hour, 21 minutes, 50 secondsnumber addiction because zero you add to any number you get the same number back same as a zero matrix. Okay. And what is
1:21:591 hour, 21 minutes, 59 secondsa diagonal matrix? Diagonal matrix is a square matrix where all nondiagonal entries are zero. So what does diagonal
1:22:071 hour, 22 minutes, 7 secondsmean for a matrix? The entries um of a square matrix on this line is called uh
1:22:151 hour, 22 minutes, 15 secondsthe diagonal entries. Usually when you say the diagonals of a matrix we mean this diagonal the top left to the bottom
1:22:231 hour, 22 minutes, 23 secondsright. About the other diagonal this we did not usually call this a diagonal of a matrix. If we call diagonal of matrix we usually only mean this line. Okay.
1:22:371 hour, 22 minutes, 37 secondsSo for a diagonal matrix all the nondiagonal entries the entries that are here should be all zero.
1:22:461 hour, 22 minutes, 46 secondsSome examples of uh diagonal matrix 1 3 0 0. This is a diagonal matrix right
1:22:551 hour, 22 minutes, 55 secondsonly the entries in the diagonal could be non zero.
1:23:001 hour, 23 minutesThis is also a diagonal matrix. This is a 3x3 diagonal matrix. Okay.
1:23:061 hour, 23 minutes, 6 secondsAnd lastly uh the identity matrix. The identity matrix is the n byn diagonal
1:23:121 hour, 23 minutes, 12 secondsmatrix with ones on the diagonal and it acts as a multiplicative identity which means that you pick any matrix any
1:23:211 hour, 23 minutes, 21 secondssquare matrix uh multiplying the identity matrix uh does nothing to the matrix.
1:23:291 hour, 23 minutes, 29 secondsSo for examples the 2x2 identity matrix is the matrix 1
1:23:371 hour, 23 minutes, 37 seconds0 0 1 and if you pick any 2x2 matrix for example a b cd and multiply to the
1:23:461 hour, 23 minutes, 46 secondsidentity matrix so 1 0 0 1 let's actually compute this so first row first column first row second column second
1:23:541 hour, 23 minutes, 54 secondsrow first column C and we have D so we got the same matrix back and even if you change the order of the multiplication
1:24:091 hour, 24 minutes, 9 secondsA first row second column B second row first column C second row second column D okay so matrix multiplication is not
1:24:181 hour, 24 minutes, 18 secondscommutative in general right but no matter what the matrix we take multiplying by the identity gives the matrix itself regardless of the order so
1:24:281 hour, 24 minutes, 28 secondsSo that's why we call a identity matrix a multiplicative identity. Uh it acts like one in ordinary multiplication. In
1:24:371 hour, 24 minutes, 37 secondsordinary multiplication, you can take any number and multiply it by one and you get the same number back. Right? Uh same as the identity matrix. You pick
1:24:441 hour, 24 minutes, 44 secondsany matrix and multiply it by the identity.
1:24:511 hour, 24 minutes, 51 secondsUh the order doesn't matter. You get the same matrix back.
1:24:571 hour, 24 minutes, 57 secondsNow because we define matrix multiplication in such an awkward way, we can do something useful here. It lets us rewrite a whole system of linear
1:25:061 hour, 25 minutes, 6 secondsequation in one compact form. For example, suppose we have a system like this. Uh we have x unknowns. So we want
1:25:161 hour, 25 minutes, 16 secondsto find x1 through xn and we have m equations. So um this is the first
1:25:231 hour, 25 minutes, 23 secondsequation. This is the mth equation. So we can write this systems of linear equation like this uh with this matrix
1:25:321 hour, 25 minutes, 32 secondsmultiplication here. We collect all the coefficients of X A and make this one
1:25:391 hour, 25 minutes, 39 secondsbig matrix and we put all the unknowns into one vertical matrix and we make this X1 through Xn matrix and we do the
1:25:471 hour, 25 minutes, 47 secondssame with the B's and this matrix multiplication uh represents the systems of linear equations. So how does this
1:25:551 hour, 25 minutes, 55 secondswork? So let's look at the systems of linear equations. So 2x + 3 y + 5 z = 7.
1:26:051 hour, 26 minutes, 5 secondsUh I'm making up uh any uh random equations = -3
1:26:111 hour, 26 minutes, 11 secondsx + 5 y - 9 z = 8. So um if I write this as a mat
1:26:201 hour, 26 minutes, 20 secondsmatrix multiplication uh we take all the coefficients here. So
1:26:251 hour, 26 minutes, 25 seconds2 3 5 1 5 8 1 5 - 9 and we make a
1:26:341 hour, 26 minutes, 34 secondsvertical matrix. This vertical matrix is often called a column vector because this looks like a column, right? and we
1:26:411 hour, 26 minutes, 41 secondsmake it a u unknown vertical uh matrix like this a column vector. Well, if you
1:26:481 hour, 26 minutes, 48 secondsactually compute this uh this is a 3x3 matrix. This is a 3x1 matrix. So, the result should be also a 3x1 matrix. So
1:26:551 hour, 26 minutes, 55 secondsfirst row, first column 2x + 5 y
1:27:001 hour, 27 minutesuh 3 y + 5 z x + 4 y + 8 z x + 5 y - 9
1:27:111 hour, 27 minutes, 11 secondsz. And look at this. This is equal to this equation. So this is equal to 7 - 3
1:27:191 hour, 27 minutes, 19 seconds8. So if I name this big matrix as A and if I name this as um X of course this X
1:27:261 hour, 27 minutes, 26 secondsis different to this X and if I name this B uh we can write this huge systems of linear equation into just this one uh simple matrix multiplication ax= b.
1:27:411 hour, 27 minutes, 41 secondsUm so the natural question is that how do we solve this right we want to actually find the values of xyz how do
1:27:491 hour, 27 minutes, 49 secondswe how do we find this um for ordinary numbers if we have something like ax
1:27:561 hour, 27 minutes, 56 secondsequals b of course when a is not zero we divide both sides by a uh it's equivalent to saying we multiply the
1:28:041 hour, 28 minutes, 4 secondsreciprocals of a both sides right so we multiply 1 / a into both sides Right.
1:28:121 hour, 28 minutes, 12 secondsRight. And since uh multiplication is associative, we can regroup this like
1:28:181 hour, 28 minutes, 18 secondsthis. And the reciprocals uh times the original value is just one, right? So 1
1:28:251 hour, 28 minutes, 25 secondsx = 1 / a b. So we found x as 1 / a * b,
1:28:321 hour, 28 minutes, 32 secondswhich is uh simply b over a, right? Um so here uh the key value is 1 / a right
1:28:411 hour, 28 minutes, 41 secondsone over a if you multiply with the a you get one which is the multiplicative inverse in ordinary multiplication but
1:28:491 hour, 28 minutes, 49 secondsmultiplicative uh identity in matrix multiplication
1:28:551 hour, 28 minutes, 55 secondsuh was the identity matrix right so we would want to find something I don't
1:29:011 hour, 29 minutes, 1 secondknow but some matrix that satisfies A B equals PA
1:29:071 hour, 29 minutes, 7 secondsequals I. We want to find this B for a given A. And that is the idea of a
1:29:141 hour, 29 minutes, 14 secondsinverse matrix. A square matrix A is invertible if an inverse matrix A minus
1:29:211 hour, 29 minutes, 21 secondsone exists such that A a minus one equals A minus 1 A equals the identity matrix.
1:29:301 hour, 29 minutes, 30 secondsUm for example if a is given as this 2 312 the inverse of a
1:29:391 hour, 29 minutes, 39 secondsdoes exist and it's 2 - 3 -1 2
1:29:471 hour, 29 minutes, 47 secondsuh if you actually compute the multiplication we know that this is an identity because 1 2 2 - 3 -1 2 this is
1:29:591 hour, 29 minutes, 59 secondsuh 2 1 - 6 + 6 0 2 - 2 0 - 3 + 4 this is
1:30:061 hour, 30 minutes, 6 secondsone this is 2x2 identity matrix and if you change the order of the multiplication you get the same identity
1:30:121 hour, 30 minutes, 12 secondsmatrix so we know that these are in inverse relationship um another example
1:30:201 hour, 30 minutes, 20 secondsif I take B as one one B minus one exists
1:30:291 hour, 30 minutes, 29 secondsAnd it is 1 - 0 1 0 1 - one 1.
1:30:381 hour, 30 minutes, 38 secondsThis is actually minus one. These are an inverse relationship. So you multiply these two matrixes
1:30:451 hour, 30 minutes, 45 secondsB minus 1 B and it's equals to the 3x3 identity matrix. But not every matrix is uh invertible.
1:30:541 hour, 30 minutes, 54 secondsMeaning that not every matrix has an inverse like a zero matrix 0 0 0. Is there an inverse to zero
1:31:041 hour, 31 minutes, 4 secondsmatrix? No. Because you multiply any matrix to a zero matrix and it's still a zero matrix. This
1:31:131 hour, 31 minutes, 13 secondscannot be an identity matrix. Right? So not every matrix is invertible. Some matrices have inverse, other matrices don't. Okay.
1:31:231 hour, 31 minutes, 23 secondsAnd using this um we can actually solve the systems of linear equation we just uh saw. So uh suppose there is a linear
1:31:331 hour, 31 minutes, 33 secondsequations that looks like this. 2x + 3 y = um uh 13
1:31:401 hour, 31 minutes, 40 secondsx + 2 y equals a. Okay. So we want to solve this equation.
1:31:491 hour, 31 minutes, 49 secondsUh so if we write this into matrix multiplication this becomes 2 3 1 2
1:31:571 hour, 31 minutes, 57 secondsxy = 138 and we know the uh inverse of this
1:32:051 hour, 32 minutes, 5 secondsmatrix right so we multiply the inverse into both sides of uh this equation. So
1:32:121 hour, 32 minutes, 12 secondsthe inverse is actually 2 minus 3
1:32:211 hour, 32 minutes, 21 seconds-12 and we multiply this to both sides.
1:32:341 hour, 32 minutes, 34 secondsAnd because matrix multiplication is associative uh we can compute this first and we know that this is identity matrix because this is inverse of this matrix.
1:32:441 hour, 32 minutes, 44 secondsSo this is I2 but if you multiply any matrix to a identity matrix you get the same matrix back. So this is the left
1:32:531 hour, 32 minutes, 53 secondshand side is x comma y and the right hand side oh this is uh 138. the right hand side if you compute the
1:33:011 hour, 33 minutes, 1 secondmultiplication uh 26 - 16 10 - 13 + 16 3
1:33:091 hour, 33 minutes, 9 secondsoh this is actually two so we have found x and y right you put x = 2 y = 3 and
1:33:161 hour, 33 minutes, 16 secondsyou know that this holds now that we've learned about invertible matrix and inverse matrix we want to find the inverse of given matrices let's start
1:33:241 hour, 33 minutes, 24 secondswith the 2x two case so we want to find the inverse of this matrix ABC D. At
1:33:311 hour, 33 minutes, 31 secondsthis point, we don't even know that this matrix has an inverse. Right? If A B C D are all zero, this matrix is not invertible, meaning that there uh does not exist any inverse, right?
1:33:441 hour, 33 minutes, 44 secondsSo, um hopefully we want to find matrix XYZ W such that the multiplication of
1:33:511 hour, 33 minutes, 51 secondsthis is equal to the identity matrix like this.
1:33:561 hour, 33 minutes, 56 secondsUh so if we actually um compute this explicitly we have xc
1:34:021 hour, 34 minutes, 2 secondsx uh ax plus bz a y + b w
1:34:091 hour, 34 minutes, 9 secondscx + d z c y + dw.
1:34:161 hour, 34 minutes, 16 secondsSo we have ax + bz = 1,
1:34:221 hour, 34 minutes, 22 secondsa y + b w = 0, cx + dz
1:34:301 hour, 34 minutes, 30 seconds= z, and c y + dw = 1. Um,
1:34:371 hour, 34 minutes, 37 secondsI'm going to multiply d and both sides of the first equation. So a dx plus b dz equals d.
1:34:471 hour, 34 minutes, 47 secondsAnd uh I'll multiply b in this equation.
1:34:501 hour, 34 minutes, 50 secondsSo b c x + b dz equals zero. If I subtract these two the
1:34:581 hour, 34 minutes, 58 secondsb dz disappears and we have a d minus b c x = d. Oh, so we found x
1:35:071 hour, 35 minutes, 7 secondsequals of course when a d minus bc is not zero is t over a d minus bc when a minus bc is not zero.
1:35:221 hour, 35 minutes, 22 secondsAnd we can apply the same thing to y zw as well. And if you carry out all the computations, we get the result. The
1:35:301 hour, 35 minutes, 30 secondsinverse matrix we are looking for is 1 minus a d minus b c
1:35:371 hour, 35 minutes, 37 secondsuh d a minus b minus c. Of course, a d minus b c
1:35:451 hour, 35 minutes, 45 secondsisn't zero. So if a d minus bc is non zero, there exist a matrix. There exist a inverse matrix that looks like this.
1:35:531 hour, 35 minutes, 53 secondsAnd if a d minus bc is zero, the matrix does not have an inverse meaning that it's not invertible.
1:36:001 hour, 36 minutesUm so a d minus bc is the key quantity here. It determines whether the inverse exist. Right? So we know that it's very
1:36:091 hour, 36 minutes, 9 secondsimportant value for a 2x two matrix. So we denote this as the determinant of 2x
1:36:161 hour, 36 minutes, 16 secondstwo matrix. So determinant of this matrix A B CD
1:36:231 hour, 36 minutes, 23 secondsis A D minus BC. Without solving the equation, we can just compute AD minus BC and determine whether if a 2x two
1:36:331 hour, 36 minutes, 33 secondsmatrix has an inverse. Right? Now what's interesting is that something similar exists for larger square matrices. For a
1:36:411 hour, 36 minutes, 41 seconds3x3 matrix or a 4x4 matrix in general n byn matrix there's still a special number attached to the matrix just like
1:36:501 hour, 36 minutes, 50 secondsa minus bc that determines whether the matrix is invertible or not and that number is called the determinant. So you
1:36:591 hour, 36 minutes, 59 secondscan view determinant of a function as a function that goes from the self matrix to a number and saying that the matrix
1:37:071 hour, 37 minutes, 7 secondsis invertible is the same as saying the determinant of a matrix is non zero
1:37:141 hour, 37 minutes, 14 secondsand uh particularly determinant AB actually separates into determinant a determinant b uh which is a very good
1:37:211 hour, 37 minutes, 21 secondsproperty and for a 2x two matrix like we uh derived here the determinant is a d minus bc P. Um, in this lecture we are
1:37:301 hour, 37 minutes, 30 secondsnot going to learn how to compute determinants for larger matrices bigger than two. And honestly, we are almost never going to compute them by hand. But
1:37:381 hour, 37 minutes, 38 secondsyou have to know that if determinant is zero, the matrix is not invertible. And if determinant is non zero, a is invertible, meaning that there is an
1:37:461 hour, 37 minutes, 46 secondsinverse for a. Before going further, let's fix some notations for matrices.
1:37:511 hour, 37 minutes, 51 secondsThis is mostly for convenience. We're going to see matrices again and again later. So instead of explaining the same thing every time we give these sets
1:38:001 hour, 38 minutesstandard names. So first this uh met and f uh this is the set of all n byn
1:38:071 hour, 38 minutes, 7 secondsmatrices with entries in f um easy uh just like what it says. So for example M
1:38:151 hour, 38 minutes, 15 seconds2 um R uh this contains matrices like um 2 3
1:38:211 hour, 38 minutes, 21 secondsminus one square 7 pi 3 + square 2 - 7 3 over 4 uh because
1:38:311 hour, 38 minutes, 31 secondsthey are all 2x2 matrices with entries from real numbers okay and this GL and F
1:38:381 hour, 38 minutes, 38 secondsthing uh this GL is from general linear okay so I will often call this a general linear group. This is the group or a set
1:38:471 hour, 38 minutes, 47 secondsof all invertible matrices in uh the n byn matrix. Okay.
1:38:531 hour, 38 minutes, 53 secondsSo it's equivalent to saying uh that this is a collection of matrices with nonzero determinants. Right. So um
1:39:021 hour, 39 minutes, 2 secondsif we look at general linear uh three R
1:39:071 hour, 39 minutes, 7 secondsuh oh general linear 2 R 1 2 3 4. So this matrix is invertible meaning that this is a element of this uh set.
1:39:201 hour, 39 minutes, 20 secondsHowever uh this matrix 2 4 5 10. This
1:39:261 hour, 39 minutes, 26 secondsmatrix is not a element of this general linear group because if you uh compute the determinant it's zero 20 minus 20.
1:39:351 hour, 39 minutes, 35 secondsSo this is not a member of general linear group. This is a non-invertible matrix.
1:39:411 hour, 39 minutes, 41 secondsAnd among these uh general linear groups particularly if you collect the matrix
1:39:481 hour, 39 minutes, 48 secondswith determinant one that is this SLNF this is called special linear group.
1:39:541 hour, 39 minutes, 54 secondsThis is a subgroup of general linear group consisting of matrices with determinant one. So um matrices like 3
1:40:031 hour, 40 minutes, 3 secondsfive 27 is in specially new group because the determinant if you compute
1:40:111 hour, 40 minutes, 11 secondsthis 3 * 5 - 2 * 7 this is one you have determinant one
1:40:171 hour, 40 minutes, 17 secondsbut um 4 6 01 this matrix has determinant four right so this is not a
1:40:251 hour, 40 minutes, 25 secondsmember of this special group earlier I've said that one reason we study algebra is that mathematics is not only