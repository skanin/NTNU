functor
import
    Application(exit:Exit)
    System
define
    fun {Max X Y}
        if X > Y then
            X
        else
            Y
        end
    end

    {System.showInfo {Max 5 19}}
    {Exit 0}
end