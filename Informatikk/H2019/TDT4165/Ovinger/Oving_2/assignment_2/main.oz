functor
import
    Application(exit:Exit)
    System
define
    % START LIST.OZ-------------------------------------------------
    fun {Length List}
        % If the list have a Head and a Tail add 1
        case List of _|Tail then
            1 + {Length Tail}
        % If not add 0
        else
            0
        end
    end

    fun {Take List Count}
        % If count is bigger or equal to the length of the list, return the list
        if {Length List} =< Count then
            List
        % If not, we have to "split" the list
        else
            % If the list have a Head and Tail check if count is 1, if it is, we only want the head
            case List of Head|Tail then
                if Count == 1 then
                    Head|nil
                % If count is not 1, we call the function recursively with the tail, and return the head
                else
                    Head|{Take Tail Count-1}
                end
            end
        end
    end

    fun {Drop List Count}
        % If count is 0 return the list
        if Count == 0 then
            List
        % If count is greater than the length of the list, return nil
        elseif Count > {Length List} then
            nil
        else
            /* 
                If the list has a head and tail, call the function recursively until count is 0, then we have removed all elements
                that we have to remove
            */
            case List of _|Tail then
                {Drop Tail Count-1}
            end
        end
    end

    fun {Append List1 List2}
        % If List1 is empty, return List2
        case List1 of nil then
            List2
        % Else if List1 consists of a Head and a Tail, take the call the function recursively with the Tail and return the head
        [] Head|Tail then
            Head|{Append Tail List2}
        end
    end

    fun {Member List Element}
        % If the List contains a Head and Tail, check if the element equals the Head, if not, call recursively with the Tail
        case List of Head|Tail then
            if Head == Element then
                true
            else
                {Member Tail Element}
            end
        % If it does not have a Head and Tail, return false. If we get here, the recursive calls have deduced the list into an empty list
        else
            false
        end
    end

    fun {Position List Element}
        /*  
            Check if the List have a Head and Tail, if it does, chek if the Head equals the element
            if it does, return 1 position, if not, add 1 position and call recursively with the tail untiil we find the element.
        */
        case List of Head|Tail then
            if Head == Element then
                1
            else
                1 + {Position Tail Element}
            end
        end
    end
    % END LIST.OZ-------------------------------------------------

    % START MDC.OZ------------------------------------------------
    fun {Lex Input}
        % Split the string on space
        {String.tokens Input & }
    end
    
    fun {Tokenize Lexemes}
        % If the Lexemes list have a head and a tail
        case Lexemes of Head|Tail then
            % Let Token be a variable 
            local Token in
                try
                    % If the head is an int, Token should be number(N)
                    if {String.isInt Head} orelse {String.isFloat Head}then
                        Token = number({String.toFloat Head})
                    % Check if head is the different types of operators and let Token be operator(type:operator)
                    elseif Head == "+" then
                        Token = operator(type:plus)
                    elseif Head == "-" then
                        Token = operator(type:minus)
                    elseif Head == "/" then 
                        Token = operator(type:divide)
                    elseif Head == "*" then
                        Token = operator(type:multiply)
                    % Check if head is the different types of commands and let Token be command(command)
                    elseif Head == "p" then
                        Token = command(print)
                    elseif Head == "d" then
                        Token = command(duplicatetop)
                    elseif Head == "i" then
                        Token = command(i) 
                    elseif Head == "^" then
                        Token = command(inverse)
                    % Set Token to error if we get non operator, non number or non command
                    else
                        Token = "Error"
                    end
                catch _ then
                    Token = "Error"
                end
                % Call recursively with Lexemes' tail and let Token be added to the list. 
                if Token == "Error" then
                    {Tokenize Tail}
                else
                    Token|{Tokenize Tail}
                end
            end
        else
            nil
        end
    end
        
    fun {Interpret Tokens}
        % Define different types of operators
        Operations = operator(
                plus:Number.'+'
                minus:Number.'-'
                multiply:Number.'*'
                divide:Int.'div'
                )
        fun {Iterate Stack Tokens}
                % If Tokens is empty ..
                case Tokens of nil then
                    % Map each element in the stack (witch is only containing numbers) to number(N) and reverse the stack. 
                    {Map {List.reverse Stack} fun{$ X} number(X) end}
                % If Top of the stack is a number, add the number to the stack and call recursively with Tokens' tail
                [] number(N)|Tail then
                    {Iterate {String.toFloat N}|Stack Tail}
                /*
                    If Top of the stack is an operator, do the calculation with 
                    Top of stack and Next to top of stack (the two first elements in the stack)
                    and add the result back to the stack (in place 1). Call recursively with Tokens' tail
                */
                [] operator(type:Operator)|Tail then
                    Top|NextToTop|Rest = Stack in
                    {Iterate {Operations.Operator NextToTop Top}|Rest Tail}
                /*
                    If Top of the stack is a command check witch command it is
                */
                [] command(Command)|Tail then
                    Top|Rest = Stack in
                    /*
                        If the command is print, print the stack and call recursively without modifying the stack
                        and with the Tokens' tail, so that the command is removed
                    */
                    case Command of print then
                        {System.showInfo "Printing the stack: "}
                        {System.show {Map {List.reverse Stack} fun{$ X} number(X) end}}
                        {Iterate Stack Tail}
                    % If the command is duplicate call recursively while adding The top of the stack to The top of the stack
                    [] duplicatetop then
                        {Iterate Top|Stack Tail}
                    % If the operator is i, inverse the Top of the stack
                    [] i then
                        {Iterate {Number.'~' Top}|Rest Tail}
                    % If the operator is inverse, divide 1 by the top of the stack and let this be the new top of the stack.
                    [] inverse then
                        {Iterate {Float.'/' 1. Top}|Rest Tail}
                    end
                end
            end
        in
        {Iterate nil Tokens}
    end
     % END MDC.OZ------------------------------------------------

     % START INFIX.OZ--------------------------------------------
     fun {InfixInternal Tokens ExpressionStack}
        % If the Tokens list is empty, return the expressionstack
        case Tokens of nil then
            ExpressionStack
        % If we encounter a number ...
        [] number(N)|Tail then
            % and the stack is empty, create a stack with the number ...
            case ExpressionStack of nil then
                {InfixInternal Tail [{Float.toString N}]}
            % If not, add the number to the stack
            else
                {InfixInternal Tail {Float.toString N}|ExpressionStack}
            end
        % If we enounter an operator ..
        [] operator(type:Operator)|Tail then
            % .. get the last numbers added to the stack ..
            First|Second|Rest = ExpressionStack in
                % .. and find out witch operator we encountered and put it between the numbers, with parenteces around
                if Operator == plus then
                    {InfixInternal Tail "(" #Second #" + " #First #")"|Rest}
                elseif Operator == minus then
                    {InfixInternal Tail "(" #Second #" - " #First #")"|Rest}
                elseif Operator == multiply then
                    {InfixInternal Tail "(" #Second #" * " #First #")"|Rest}
                elseif Operator == divide then
                    {InfixInternal Tail "(" #Second #" / " #First #")"|Rest}
                end
            
        end
    end

    fun {Infix Tokens}
        % Call InfixInternal with Tokens and an empty stack. Return the first element in the stack returned (Witch is our expression)
        {InfixInternal Tokens nil}.1
    end
    % END INFIX.OZ--------------------------------------------

    % START EXAMPLES------------------------------------------

    % Ex. fun Lex
    {System.showInfo "Ex. fun Lex"}
    {System.show {Lex "1 2 + 3 *"}}
    % Expected output ["1" "2" "+" "3" "*"]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Tokenize w/o Lex
    {System.showInfo "Ex. fun Tokenize w/o Lex"}
    {System.show {Tokenize ["1" "2" "+" "3" "*"]}}
    % Expected output [number(1) number(2) operator(type:plus) number(3) operator(type:mulitply)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Tokenize w/Lex
    {System.showInfo "Ex. fun Tokenize w/Lex"}
    {System.show {Tokenize {Lex "1 2 + 3 *"}}}
    % Expected output [number(1) number(2) operator(type:plus) number(3) operator(type:mulitply)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Interpret w/o Lex and Tokenize
    {System.showInfo "Ex. fun Interpret w/o Lex and Tokenize"}
    {System.show {Interpret [number(1) number(2) number(3) operator(type:plus)]}}
    % Expected output [number(1) number(5)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Iterpret w/Lex and Tokenize
    {System.showInfo "Ex. fun Iterpret w/Lex and Tokenize"}
    {System.show {Interpret {Tokenize {Lex "1 2 3 +"}}}}
    % Expected output [number(1) number(5)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Interpret w/command(p)
    {System.showInfo "Ex. fun Interpret w/command(p)"}
    {System.show {Interpret {Tokenize {Lex "1 2 3 p +"}}}}
    % Expected output: Print [number(1) number(2) number(3)], return [number(1) number(5)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Interpret w/command(d)
    {System.showInfo "Ex. fun Interpret w/command(d)"}
    {System.show {Interpret {Tokenize {Lex "1 2 3 + d"}}}}
    % Expected output  [number(1) number(5) number(5)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Interpret w/command(i)
    {System.showInfo "Ex. fun Interpret w/command(i)"}
    {System.show {Interpret {Tokenize {Lex "1 2 3 + i"}}}}
    % Expected output  [number(1) number(-5)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Interpret w/command(invese)
    {System.showInfo "Ex. fun Interpret w/command(invese)"}
    {System.show {Interpret {Tokenize {Lex "1 2 3 + ^"}}}}
    % Expected output  [number(1) number(0.2)]
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun InfixInternal
    {System.showInfo "Ex. fun InfixInternal"}
    {System.show {InfixInternal {Tokenize {Lex "3.0 10.0 9.0 * - 0.3 +"}} nil}}
    % Expected output ["("(3.0 - (10.0 * 9.0) + 0.3)"] (or a list with the ASCII values)
    {System.showInfo ""} % Just for printing purposes

    % Ex. fun Infix
    {System.showInfo "Ex. fun Infix"}
    {System.showInfo {Infix {Tokenize {Lex "3.0 10.0 9.0 * - 0.3 +"}}}}
    % Expected output (3.0 - (10.0 * 9.0) + 0.3)"
    {System.showInfo ""} % Just for printing purposes

    % END EXAMPLES------------------------------------------
    {Exit 0}
end