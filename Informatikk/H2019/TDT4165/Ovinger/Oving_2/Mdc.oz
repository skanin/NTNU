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
                % Show a message if we get a non operator, command or number.
                else
                    {Browse "Got non operator, non number or non command ----Skipping"}
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
                    {System.show Stack}
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