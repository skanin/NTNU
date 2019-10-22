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