functor
import
    Application(exit:Exit)
    System
define

    fun {LazyNumberGenerator StartValue}
        StartValue|fun {$} {LazyNumberGenerator StartValue+1} end
    end

    {System.show {{{{{{LazyNumberGenerator 5}.2}.2}.2}.2}.2}.1}
    {Exit 0}
end