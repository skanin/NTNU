functor 
import 
    Application(exit:Exit)
    System
define
    /**************Start Task 1**************/
    /* The procedure takes parameters A B and C */
    proc {QuadraticEquation A B C ?RealSol ?X1 ?X2}
        /* Calculates D with the formula in the appendix */ 
        D = (B*B) - (4.0 * A * C) in
        /* If D >= 0, the quadratic equation does have solution(s) so we calculate these with the formula in the appendix
            and set RealSol to true, because there is a solution */
        if D >= 0.0 then
            X1 = (~B + {Sqrt D})/(2.0*A)
            X2 = (~B - {Sqrt D})/(2.0*A)
            RealSol = true
        else
            /* If D < 0 there does not exist any real solutions, so we set RealSol to false. */
            RealSol = false
        end
    end
    /***************End Task 1***************/

    /**************Start Task 2**************/
    /* Function Sum takes a list as parameter */
    fun {Sum List}
        /* Checks if the list has any elements */
        case List of Head|Tail then
            /* Calls itself recursively with List's tail and remembering the head for summation later. */
            Head + {Sum Tail}
        /* If  the list is nil, we return 0 */
        [] nil then
            0
        end
    end

    /***************End Task 2***************/

    /**************Start Task 3**************/
    /* The function RightFold takes a List, operator (as a function) and an inital value as parameters */
    fun {RightFold List Op U}
        /* Checks if the list has elements */
        case List of Head|Tail then
            /* 
                If it does, call recursively with the taik while setting the initial value U to the operation between U and Head. 
                Example: If U = 0 (as the inital value in summation) and the operation is summation, the "first round of recursion" 
                will call itself recursively with U + Head = 0 + Head as U. That way, "the next initial value" (in the "next round
                of recursion") will be the last Operation done. 
                Example2: {RightFold [1 2 3] fun{$ X Y} X + Y end 0} calls {RightFold [2 3] fun{$ X Y} X + Y end (0 + 1)} 
                calls {RightFold [3] fun{$ X Y} X + Y end (1 + 2)} calls 
                {RightFold [2 3] fun{$ X Y} X + Y end (3 + 3)} which returns U which is 6. 
            */
            {RightFold Tail Op {Op U Head}}
        /* If the list does not have any more elements return U */
        [] nil then
            U
        end
    end
    
    /* Length with RightFold implementation. Initial value is 0, add one each time we encounter an element */
    fun {Length List}
        {RightFold List fun {$ X Y} X + 1 end 0}
    end

    /* Sum with RightFold implementation. Initial value is 0. The anonymous funtion returns X + Y, where X the first time is U and
        later the sum already calculated */
    fun {FoldSum List}
        {RightFold List fun {$ X Y} X + Y end 0}
    end
    /***************End Task 3***************/
    
    /**************Start Task 4**************/
    /* 
        Quadratic returns an anonymous funtion which calculates Ax^2 + Bx + C. X is an input given when calling quadratic. 
        I.e {{Quadratic 3 2 1} 2} <- X = 2. (The last one). The anonymous function is triggered due to the outer curly brackets.
        So, {Quadratic 3 2 1} will return the anonymous function which is called with X = 2.
     */
    fun {Quadratic A B C}
        fun{$ X}
            A * X * X + B * X + C
        end
    end
    /***************End Task 4***************/

    /**************Start Task 5**************/
    /* High level description can be found in Theory.pdf. */
    /* Function LazyNumberGenerator returns a list with a value and an anonymous function, which is triggered when accessing it (List.2) */
    fun {LazyNumberGenerator StartValue}
        StartValue|fun {$} {LazyNumberGenerator StartValue+1} end
    end
    /***************End Task 5***************/

    /**************Start Task 6**************/
    /* Sum with tail recursion takes a list as parameter */
    fun {TailSum List}
        /* Internal function Add for remembering result */
        fun {Add List Result}
            /* If the list has a head and a tail */
            case List of Head|Tail then
                /* 
                    Call recursively wtih tail and result = Result + Head. This is what makes it tail recursive.
                    When calculating the result when we call the function recursively, we are updating our variable and the stack
                    remains the same size. Without tail recursion, the calls would have been like this when calculating {Sum [1 2 3]}:

                    {Sum [1 2 3]}
                    -> (1 + {Sum [2 3]})
                    -> (1 + (2 + {Sum [3])
                    -> (1 + (2 + 3))
                    -> (1 + 5)
                    -> 6

                    With tail recursion we do not have to "move upwards" in the end, our result is already calculated.
                */
                {Add Tail Result+Head}
            else
                /* If it does not have a head and tail, just return the result */
                Result
            end
        end 
        in
        {Add List 0}
    end

    fun {RightFold2 List Op U}
        case List of Head|Tail then
            {Op Head {RightFold2 Tail Op U}}
        else
            U
        end
    end

    /***************End Task 6***************/

    /************Start Examples**************/

    /* Example Quadratic equation, A=2, B=1, C=-1 */
    RealSol X1 X2 in
    {QuadraticEquation 2.0 1.0 ~1.0 RealSol X1 X2}
    {System.show [RealSol X1 X2]}
    /* Expected output [true 0.5 -1] */
    /* Expected output with A=2 B=1 C=2 = [false _ _] */

    /* Exapmple "regular" sum */
    {System.show {Sum [1 2 3 4 5 6 7 8 9 10]}}
    /* Expected output: 55 */

    /* Example RightFold with multiplication */
    {System.show {RightFold [1 2 3 7] fun{$ X Y} X * Y end 1}}
    /* Expected output 1*2*3*7 = 42 */

    /* Example Length with RightFold */
    {System.show {Length [1 2 3 4 5 6 7 8]}}
    /* Expected output: 8 */

    /* Example sum with RighFold */
    {System.show {FoldSum [1 2 3 4 5 6 7 8 9 10]}}
    /* Expected output: 55 */

    /* Example  quadratic with anonymous function */
    {System.show {{Quadratic 3 2 1} 2}}
    /* Expected output: 17 */

    /* Example LaxyNumberGenerator */
    {System.show {{{{{{LazyNumberGenerator 0}.2}.2}.2}.2}.2}.1}
    /* Expected output: 5 */

    /* Example sum with tail recursion */
    {System.show {TailSum [1 2 3 4 5 6 7 8 9 10]}}
    /* Expected output: 55 */

    
    {System.show {RightFold [1 2 3 4 5 6 7 8] fun{$ X Y} X-Y end 0}}
    {Exit 0}
    /*************End Examples***************/
end