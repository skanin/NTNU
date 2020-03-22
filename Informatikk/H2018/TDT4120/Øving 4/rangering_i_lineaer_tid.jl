function counting_sort_letters(liste, pos)
    min = 0
    max = 0

    for word in liste
        if Int(word[pos])-96 < min
            min = Int(word[pos])-96
        elseif Int(word[pos])-96 > max
            max = Int(word[pos])-96
        end
    end

    count = [0 for i = 1:max]
    output = ["0" for i = 1:length(liste)]
    for i=1:length(liste)
        count[Int(liste[i][pos])-96] = count[Int(liste[i][pos])-96] + 1
    end

    for i=2:length(count)
        count[i] = count[i] + count[i-1]
    end

    for i = length(liste):-1:1
        letter = liste[i][pos]
        index = Int(letter)-96
        for j = length(count):-1:1
            if j == index
                output[count[j]] = liste[i]
                count[j] = count[j] - 1
            end
        end
    end
    return output
end


#println(counting_sort_letters(["bar", "thr", "har", "lkr", "gtr", "gar", "git"], 2))

function counting_sort_length(liste)
    min = 0
    max = 0

    for word in liste
        if length(word) < min
            min = length(word)
        elseif length(word) > max
            max = length(word)
        end
    end

    count = [0 for i=1:max+1]
    output = ["0" for i=1:length(liste)]

    for i=1:length(liste)
        count[length(liste[i]) + 1] = count[length(liste[i]) + 1] + 1
    end

    for i=2:length(count)
        count[i] = count[i] + count[i-1]
    end
    println("Count: ", count)
    for i = length(liste):-1:1
        lengde = length(liste[i])
        for j = length(count):-1:1
            if j == lengde + 1
                output[count[j]] = liste[i]
                count[j] = count[j] - 1
            end
        end
    end
    return output
end

#println(counting_sort_length(["bbbb", "aa", "aaaa", "ccc", ""]))


function flexradix(A, max_length)
    
end

println(flexradix(["elvr", "germoinio", "fe", "dope", "mapjrom", "meiogreno"], 9))
