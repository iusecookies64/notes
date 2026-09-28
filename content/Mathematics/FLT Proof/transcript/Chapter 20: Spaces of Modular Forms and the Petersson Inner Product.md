Chapter 20: Spaces of Modular Forms and the Petersson Inner Product
7:07:407 hours, 7 minutes, 40 secondsmodular forms. But what happens if we collect all modular forms of a fixed weight? Do they form some kind of algebraic object a vector space maybe a
7:07:487 hours, 7 minutes, 48 secondsring? Can we talk about bases and dimension? And the violence formula gives us the first clue here. Roughly
7:07:557 hours, 7 minutes, 55 secondsspeaking, this formula says that if f is a non-zero modular form of weight k, then the total number of zeros and poles
7:08:037 hours, 8 minutes, 3 secondsof f counted the right way on the fundamental domain is controlled by k.
7:08:087 hours, 8 minutes, 8 secondsSo more precisely the total weighted orders of finishing is k over 12. So let f be a nonzero memorphic modular form of
7:08:177 hours, 8 minutes, 17 secondsweight k for the full modular group. And the sums of all orders of zeros and poles of f in the fundamental domain
7:08:257 hours, 8 minutes, 25 secondsweighted by the stabilizer orders of the points is constant which is k over 12.
7:08:317 hours, 8 minutes, 31 secondsSo a zero here means that a point where the functions become zero and a pool is where functions blows up to infinity. Uh
7:08:397 hours, 8 minutes, 39 secondsso like if a function f is something like 1 / z minus 3 cub + 1 / z - 2² here
7:08:497 hours, 8 minutes, 49 secondsz = 2 and z = 3. They blow up right. So uh we say that uh this function has poles in z equals 2 and z equ= 3 and the order is uh two and three.
7:09:017 hours, 9 minutes, 1 secondAnd here I is uh just I and row is E to the 2 pi I over 3. And this infinitely
7:09:097 hours, 9 minutes, 9 secondsand this infinity means cusp. These three are in these three are for whatever reasons are treated differently
7:09:187 hours, 9 minutes, 18 secondsand they are weighted by one over two and one over three and these are all the other zeros and poles of uh the
7:09:257 hours, 9 minutes, 25 secondsfunction. So the important point is not the exact technical form of this formula right now for us. So the important point is not the exact formula right now. The
7:09:347 hours, 9 minutes, 34 secondsimportant point is that once the way K is fixed, the function is heavily constrained. Modular forms have limited
7:09:417 hours, 9 minutes, 41 secondsfreedom. In other words, it start to make sense to ask for a basis or dimension and an actual linear algebraic structure on modular forms.
7:09:527 hours, 9 minutes, 52 secondsSo the valance formula tells us that modular forms have limited freedom and in fact uh for a given weight k the
7:09:597 hours, 9 minutes, 59 secondsspaces of modular forms and cost forms of dimensional complex vector spaces and this holds choose for all kinds of
7:10:067 hours, 10 minutes, 6 secondssubgroups whether the group is the full modular group or the congrent subgroups like gamma zero n mk here denotes the
7:10:147 hours, 10 minutes, 14 secondsspace of modular forms and sk here means the set of c forms and this is a big deal because Now modular forms becomes
7:10:227 hours, 10 minutes, 22 secondssomething we can study using a linear algebra. Uh we can ask what is the dimension of this space? Can we find a basis or can we write every modular
7:10:307 hours, 10 minutes, 30 secondsforms as a linear combinations of some standard modular forms. And when we talk about modular forms from now on the
7:10:387 hours, 10 minutes, 38 secondssubgroup can often be confusing because sometimes the subgroup will be the full module group and sometimes it will be a
7:10:447 hours, 10 minutes, 44 secondscongrent subgroup comma 0 m. They are similar but there are also many differences. So it's important to
7:10:517 hours, 10 minutes, 51 secondsdistinguish between them. If we write MK and SK without specifically mentioning the associated subgroup, we mean the
7:10:587 hours, 10 minutes, 58 secondsfull modular group. And if we write MK gamma 0 N sk like this explicitly mentioning the
7:11:077 hours, 11 minutes, 7 secondssubgroup then we usually mean a congruent subgroup. And in some cases we can actually compute the dimension
7:11:147 hours, 11 minutes, 14 secondsexplicitly. For example, when the weight is k= 2 and the group is gamma 0 n, there is a dimension formula for the
7:11:237 hours, 11 minutes, 23 secondsspace of cost forms. So we can literally hand compute the dimensions of this modular group ourselves. Um, of course I'm not going to derive the formula
7:11:327 hours, 11 minutes, 32 secondshere. The point is just that these spaces are concrete enough that we can talk about their dimensions. And this is spoiler but this will become very important later.
7:11:437 hours, 11 minutes, 43 secondsAnother structural fact about the space of modular forms is that the space of modular forms can be splitted like this.
7:11:507 hours, 11 minutes, 50 secondsSo the space of modular forms is decomposed into the eenstein series and the cusp form space. Of course this is
7:11:587 hours, 11 minutes, 58 secondsonly for the full modular group. So what does it mean? It means that if we take any modular forms from uh the space of
7:12:067 hours, 12 minutes, 6 secondsmodular forms, this can be uniquely written as um CK plus G where G is a cusp form.
7:12:177 hours, 12 minutes, 17 secondsAnd if you think about it, this is actually um very obvious [clears throat] because earlier we saw that the Einstein series EK has constant term one, right?
7:12:327 hours, 12 minutes, 32 secondsAnd if f has constant term a z
7:12:397 hours, 12 minutes, 39 secondswe can choose c to be a z and then f minus a z e k
7:12:477 hours, 12 minutes, 47 secondshas constant term zero. But a mod form with constant terms zero is a cusp form.
7:12:527 hours, 12 minutes, 52 secondsMeaning that f minus a z e k is a c form. And that's why every mod of form can be split into eenstein part and the
7:13:007 hours, 13 minutescost form part. Now think back to what we did in linear algebra. Once we had a vector space, we did not stop there. We
7:13:097 hours, 13 minutes, 9 secondsintroduced an inner product. And once we had an inner product, we could talk about things like length, norm, and orthogonality.
7:13:177 hours, 13 minutes, 17 secondsWe want to do the same kind of thing here. We have these dimensional vector spaces of modular forms like MK or SK.
7:13:267 hours, 13 minutes, 26 secondsSo we want to know if it's possible to define an inner product on this space.
7:13:307 hours, 13 minutes, 30 secondsCan we say that two modular forms are perpendicular? Can we measure the size of a modular form? And the answer is yes. The inner product we use is called
7:13:397 hours, 13 minutes, 39 secondsthe Peterson inner product. It's defined on the cost form. So f and g here are
7:13:467 hours, 13 minutes, 46 secondscost forms and it's defined by these equation.
7:13:517 hours, 13 minutes, 51 secondsYou do not need to memorize this integral right now. The important part is the role it plays. Now that we have
7:13:587 hours, 13 minutes, 58 secondsthe pers inner product, the space of uh cus form with weight kh becomes more
7:14:057 hours, 14 minutes, 5 secondsthan just a vector space. It becomes an inner product space. So we can talk about geometric ideas inside the space
7:14:127 hours, 14 minutes, 12 secondsof functions. For example, the norms of a cel form is defined as the square root of the pet inner product with the same
7:14:217 hours, 14 minutes, 21 secondsuh function and two cus forms are set to be orthogonal if their pet inner product is zero. So the slide says that this
7:14:317 hours, 14 minutes, 31 secondsgives the space of cusp form with weight k uh the structure of a hilbert space.
7:14:367 hours, 14 minutes, 36 secondsVery briefly a hbert space is an inner product space that is complete. Complete means that if a sequence of vectors
7:14:447 hours, 14 minutes, 44 secondsshould converge according to the norm, then its limit always uh stays inside the space. It's similar to the analytic
7:14:527 hours, 14 minutes, 52 secondsconstructions of QP. In our case, we don't need to worry too much about the technical condition. [clears throat] Now, let's look at something a bit
