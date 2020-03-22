function nim(sticks)
    counter = 0
    while counter < 7
        if((sticks - counter) % 8 == 1)
            break
        else
            counter = counter + 1
        end
    end
    if(counter == 0)
        println("Ingen garanti for å vinne")
    else
        println("Du må ta vekk " * string(counter))
    end
end

nim(268)
