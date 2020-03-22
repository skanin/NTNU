functor
import
    System
define
    proc {Circle R}
        local
            Pi = 3.14
            A = Pi*R*R
            C = 2.0*Pi*R
            D = 2.0*R
        in
            {System.showInfo A}
            {System.showInfo C}
            {System.showInfo D}
        end
    end
    {System.showInfo 1+1.0}
end

   
    
    