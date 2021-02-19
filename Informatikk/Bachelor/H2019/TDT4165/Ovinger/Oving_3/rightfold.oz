functor
import
    Application(exit:Exit)
    System
define
    fun {RightFold List Op U}
        case List of Head|Tail then
            {RightFold Tail Op {Op U Head}}
        [] nil then
            U
        end
    end
    
    fun {Length List}
        {RightFold List fun {$ X Y} X + 1 end 0}
    end

    fun {Sum List}
        {RightFold List fun {$ X Y} X + Y end 0}
    end

    {System.show {RightFold [1 2 3 7] fun{$ X Y} X * Y end 1}}
    {Exit 0}
end