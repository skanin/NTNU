functor
import
    Application(exit:Exit)
    System
define
    fun {Sum List}
        fun {Add List Result}
            case List of Head|Tail then
                {Add Tail Result+Head}
            else
                Result
            end
        end 
        in
        {Add List 0}
    end

    {System.show {Sum [1 2 3 4 5]}}
    {Exit 0}
end