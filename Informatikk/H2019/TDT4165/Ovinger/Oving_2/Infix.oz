functor
import
    Application(exit:Exit)
    Browser(browse:Browse)
    System
define
    \insert List.oz
    \insert Mdc.oz

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

    {System.showInfo {Infix {Tokenize {Lex "3.0 10.0 9.0 * - 0.3 +"}}}}
    {Exit 0}
end