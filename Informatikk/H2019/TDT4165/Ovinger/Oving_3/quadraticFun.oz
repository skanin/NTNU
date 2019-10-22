functor
import
    Application(exit:Exit)
    System
define
    fun {Quadratic A B C}
        fun{$ X}
            A * X * X + B * X + C
        end
    end

    {System.show {{Quadratic 3 2 1} 3}}
    {Exit 0}
end