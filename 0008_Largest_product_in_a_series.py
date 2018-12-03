"""
Problem 8 - Largest product in a series

The 4 adjacent digits in the 1000-digit number that have
the greatest product are 9 × 9 × 8 × 9 = 5832.

7316717653133062491922511967442657474235534919493496983520312
7745063262395783180169848018694788518438586156078911294949545
9501737958331952853208805511125406987471585238630507156932909
6329522744304355766896648950445244523161731856403098711121722
3831136222989342338030813533627661428280644448664523874930358
9072962904915604407723907138105158593079608667017242712188399
8797908792274921901699720888093776657273330010533678812202354
2180975125454059475224352584907711670556013604839586446706324
4157221553975369781797784617406495514929086256932197846862248
2839722413756570560574902614079729686524145351004748216637048
4403199890008895243450658541227588666881164271714799244429282
3086346567481391912316282458617866458359124566529476545682848
9128831426076900422421902267105562632111110937054421750694165
8960408071984038509624554443629812309878799272442849091888458
0156166097919133875499200524063689912560717606058861164671094
0507754100225698315520005593572972571636269561882670428252483
600823257530420752963450

Find the 13 adjacent digits in the 1000-digit number that have
the greatest product. What is the value of this product?
"""

def Largest_product(Num, digits):

    Num = str(Num)
    Max = -1

    for i in range(len(Num)-digits+1):
        Mul = 1
        for j in range(i, i+digits):
            Mul *= int(Num[j])
            if(Mul > Max):
                Max = Mul
    return Max

print(Largest_product(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13))
