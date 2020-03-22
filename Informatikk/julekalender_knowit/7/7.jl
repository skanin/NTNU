cd("/Users/sanderlindberg/Dropbox/NTNU/Informatikk/julekalender_knowit/")
function test()
    f = open("input-vekksort2.txt")
    s = readlines(f)
    lst = []
    for line in s
        append!(lst, parse(Int, line))
    end
    println(length(lst))
    longest = []
    for i = 1 : length(lst)
        temp = []
        j = i
        while j <= length(lst)
            if length(temp) != 0
                if lst[j] > lst[j]
                    append!(temp, lst[j])
                    j += 1
                else
                    j += 2
                end
            else
                append!(temp, lst[j])
                println("Hei")
                j += 1
            end
        end
        if length(temp) > length(longest)
            longest = temp
        end
        println(i)
    end
    return length(longest)
end

#println(test())
f = open("input-vekksort2.txt")
s = readlines(f)
lst = map(x -> parse(Int, x), s)
longest = []

function test2(lst)
    n = length(lst)

    lis = [1 for i = 1 : n]

    for i = 2 : n
        for j = 1 : i
            if lst[i] > lst[j] && lis[i] < lis[j] + 1
                lis[i] = lis[j] + 1
            end
        end
        println(i)
    end

    maximum = 0

    for i = 1 : n
        maximum = max(maximum, lis[i])
    end

    return maximum
end

println(test2(lst))
