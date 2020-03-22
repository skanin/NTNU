functor
import
    Application(exit:Exit)
    System
define
    proc {PrintGreater X Y}
        if X > Y then
            {System.showInfo X}
        else
            {System.showInfo Y}
        end
    end

    {PrintGreater 5 4}
    {Exit 0}
end