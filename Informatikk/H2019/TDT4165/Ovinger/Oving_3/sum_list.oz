functor
import
    Application(exit:Exit)
    System
define
    fun {Sum List}
        case List of Head|Tail then
            Head + {Sum Tail}
        [] nil then
            0
        end
    end

    {System.show {Sum [1 2 3 4 5 6 7 8 9 10]}}
    {Exit 0}
end