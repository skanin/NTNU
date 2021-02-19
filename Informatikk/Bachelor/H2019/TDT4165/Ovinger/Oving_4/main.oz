functor
import
    Application(exit:Exit)
    OS
    System
define
    /************ Start Task 1 **********/
    fun {GenerateOdd S E}
        if S =< E then % Check that start is less than end
            if {IsOdd S} then % Check if number is odd
            % If it is odd, add it to the list and call recursively with the number + 2 (so we don't have to call recursively unecessary
            % number of times. If we find an odd number, the next odd number is this + 2.)
                S|{GenerateOdd S+2 E} 
            else
                % If it's an even number, add 1 and call recursively. 
                {GenerateOdd S+1 E}
            end
        else
            nil
        end
    end

    fun {IsOdd X}
        X mod 2 \= 0 % Return if the number is divisable by 2.
    end
    /********* End Task 1 *********/

    /********** Start Task 2 **********/
    fun {Product S}
        case S of Head|Tail then % Check if the list has a head and tail
            Head * {Product Tail} % If it does, call recursively while multiplying with head.
        else
            1 % Return 1 if the list does not have more elements. 
        end
    end
    /********* End Task 2 *********/

    /********** Start Task 3 **********/
    {System.showInfo "Task 3: \n"}
    local Xs Prod in % Generate list of odd numbers on one thread and calculate product on another. Theory can be found in theory.pdf
        thread Xs = {GenerateOdd 0 1000} end
        thread Prod = {Product Xs} end
        {System.showInfo Prod}
    end
    {System.showInfo "\n\n\n"}
    /********** End Task 3 **********/

    /********** Start Task 4 **********/
    fun lazy {GenerateOddLazy S E} % The same function as above, except it is lazy. Theory can be found in theory.pdf.
        if S =< E then
            if {IsOdd S} then
                S|{GenerateOddLazy S+2 E}
            else
                {GenerateOddLazy S+1 E}
            end
        else
            nil
        end
    end

    {System.showInfo "Task 4: \n"}
    local Xs Prod in
        thread Xs = {GenerateOddLazy 0 1000} end
        thread Prod = {Product Xs} end
        {System.showInfo Prod}
    end
    {System.showInfo "\n\n\n"}
    /********** End Task 4 **********/

    /********** Start Task 5 **********/
    % Given function to generate random number. 
    fun {RandomInt Min Max}
        X = {OS.rand}
        MinOS
        MaxOS
    in
        {OS.randLimits ?MinOS ?MaxOS}
        Min + X*(Max - Min) div (MaxOS - MinOS)
    end

    /* a) */
    fun lazy {HammerFactory}
        % There's a 1sec delay for creating hammer. 
        {Delay 1000}
        /*
            There's a 10 percent chance of getting a defect hammer. There's a 10 percent chance of getting any number between
            1 and 10 (roughly). I check if the number we get is 10, if it is we add a defect hammer, else (1-9) we add a working.
        */
        if {RandomInt 1 11} == 10 then 
            defect|{HammerFactory}
        else
            working|{HammerFactory}
        end 
    end
    /* b) */

    fun {HammerConsumer HammerStream N}
        if N == 0 then
            0 % If we are to read 0 elements from the hammerstream, we simply return 0 cuz no hammers are working if we are to check 0.
        else
            if HammerStream.1 == working then
                1 + {HammerConsumer HammerStream.2 N-1} % If we find a working hammer, add 1
            else
                0 + {HammerConsumer HammerStream.2 N-1} % Else, add 0.
            end
        end
    end

    /* c) */
    fun {BoundedBuffer HammerStream N}
        /* 
            LookAhead "Looks ahead" N elements from HammerStream. When calling List.drop, we "skip" the N first
            elements in the stream, fills up HammerStream with N elements and LookAhead will be a list with future elements where we
            can get elements on demand.

        */
        LookAhead = thread {List.drop HammerStream N} end
        fun lazy {GenerateHammer HammerStream LookAhead}
            case HammerStream of Head|Tail then
                /*
                    We add the first element of hammerstream to the buffer and call the function recursively, whilst calling LookAhead.2 
                    on a different thread, so that the function HammerFactory is triggered and creates a new hammer 
                    (because lookahead.2 conatins the lazy function {HammerFactory}). This way, the buffer always contains up to N
                    elements. I'm using threads so that these operatons can run in parallel. 
                */
                Head|{GenerateHammer Tail thread LookAhead.2 end}
            end
        end
    in
        {GenerateHammer HammerStream LookAhead}
    end
    /********** End Task 5 **********/   

    /********** Start Examples **********/

    /********** GenerateOdd **********/
    {System.showInfo "GenerateOdd -3 10 \n"}
    {System.show {GenerateOdd ~3 10}} % should print [∼3 ∼1 1 3 5 7 9].
    {System.showInfo "\nGenerateOdd 3 3 \n"}
    {System.show {GenerateOdd 3 3}} % should print [3].
    {System.showInfo "\nGenerateOdd 2 2 \n"}
    {System.show {GenerateOdd 2 2}} % should print nil.
    {System.showInfo "\n\n\n"}

    /********** Product **********/
    {System.showInfo "Product [1 2 3 4] \n"}
    {System.show {Product [1 2 3 4]}} % Should print 24
    {System.showInfo "\n\n\n"}

    /********** GenerateOdd without lazy and product **********/
    {System.showInfo "GenerateOdd without lazy and product: \n"}
    local Xs Prod in
        thread Xs = {GenerateOdd 0 1000} end
        thread Prod = {Product Xs} end
        {System.showInfo Prod}
    end
    {System.showInfo "\n\n\n"}

    /********** GenerateOdd with lazy and product **********/
    {System.showInfo "GenerateOdd with lazy and product: \n"}
    local Xs Prod in
        thread Xs = {GenerateOddLazy 0 1000} end
        thread Prod = {Product Xs} end
        {System.showInfo Prod}
    end
    {System.showInfo "\n\n\n"}

    /********** HammerFactory **********/
    {System.showInfo "HammerFactory: \n"} % <-- Printing purposes
    local HammerTime B in
        HammerTime = {HammerFactory}
        B = HammerTime.2.2.2.1
        {System.show HammerTime}
    end
    {System.showInfo "\n\n\n"}

    /********** HammerFactory and HammerConsumer *********/
    {System.showInfo "HammerFactory and HammerConsumer: \n"}
    local HammerTime Consumer in
        HammerTime = {HammerFactory}
        Consumer = {HammerConsumer HammerTime 10}
        {System.show Consumer}
    end
    {System.showInfo "\n\n\n"}

    /********** HammerConsumer without buffer ***********/
    {System.showInfo "HammerConsumer, HammerStream and HammerFactory without buffer: \n"}
    local HammerStream Consumer in
        HammerStream = {HammerFactory}
        {Delay 6000}
        Consumer = {HammerConsumer HammerStream 10}
        {System.show Consumer}
    end
    {System.showInfo "\n\n\n"}

    /********** HammerConsumer with buffer ***********/
    {System.showInfo "HammerConsumer, HammerStream and HammerFactory with buffer: \n"}
    local HammerStream Buffer Consumer in
        HammerStream = {HammerFactory}
        Buffer = {BoundedBuffer HammerStream 6}
        {Delay 6000}
        Consumer = {HammerConsumer Buffer 10}
        {System.show Consumer}
    end
    {System.showInfo "\n\n\n"}
    {Exit 0}
end