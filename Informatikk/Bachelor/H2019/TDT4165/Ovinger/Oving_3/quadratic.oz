functor
import
    Application(exit:Exit)
    System
define
    proc {QuadraticEquation A B C ?RealSol ?X1 ?X2}
        D = (B*B) - (4.0 * A * C) in
        if D >= 0.0 then
            X1 = (~B + {Sqrt D})/(2.0*A)
            X2 = (~B - {Sqrt D})/(2.0*A)
            RealSol = true
        else
            RealSol = false
        end
    end

    RealSol X1 X2 in
    {QuadraticEquation 2.0 1.0 ~1.0 RealSol X1 X2}
    {System.show [RealSol X1 X2]}
    {Exit 0}
end