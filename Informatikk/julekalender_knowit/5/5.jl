memo = Dict()

function combine_nums(num1, num2)
    return parse(Int64, string(num1, num2))
end

function contains(a, b)
    return b in a
end


function forty_two(a)
    b = []
    sum = 0

    lst = a
    j = 2
    comb_lst = []
    for i = 1 : length(a)-1
        append!(comb_lst, combine_nums(a[i], a[i+1]))
    end

    while !contains(b, sort!(lst)) || !contains(b, combine_nums)
        if j > length(a)
            break
        end
        #println("Hei")
        if !contains(b, lst)
            push!(b, lst)
        end
        if !contains(b, comb_lst)
            push!(b, comb_lst)
        end

        lst = []
        temp = j
        for i = 1 : j-1
            append!(lst, a[i])
        end
        for i = j : length(a)
            if i == temp
                append!(lst, -1*a[i])
            else
                append!(lst, a[i])
            end
            temp += 1
        end
        comb_lst = []
        for i = j : length(a)-1
            append!(comb_lst, combine_nums(a[i], a[i+1]))
        end
        j += 1
    end




    counter = 0

    minus = 0
    pluss = length(a)


#=
    for i=1:length(a)
        if pluss
            sum += a[i]
            pluss = !pluss
            minus = !minus
        elseif minus
            sum -= a[i]
            minus = !minus
            pluss = !pluss
        end
    end
=#
#=
for i=1:7
    sum += a[i]
end


    if sum == 42
        counter += 1
    end
=#
    return b

end

a = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]


#println(forty_two(a))
#=
function test()
    temp = forty_two(a)
    count = 0
    sum = 0
    for i=1:length(temp)
        for j=1:length(temp[i])
            sum += temp[i][j]
        end
        println(sum)
        if sum == 42
            count += 1
        end
    end
    return count
end

test()
=#

function test()
    temp = []
    lst = []
    j = 1
    t = 1
    x = 0
    #=
    for i = 1 : 2 : length(a) - 1
        append!(lst, combine_nums(a[i], a[i+1]))
        t += 2
    end

    append!(lst, a[t:length(a)])
    =#
    for f = 1 : length(a)
        lst = []
        while true
            #=
            if x != length(a)
                x += 1
            else
                @goto escape
            end=#

            lst = []
            #=
            for i = 1 : j
                append!(lst, a[i])
            end
            =#
            if j > t
                append!(lst, a[t:j-1])
            end

            #append!(lst, a[1:j-1])
            for i = j : 2 : length(a) - 1
                println("I: ----------------------", i)
                if i != length(a) - 1
                    append!(lst, combine_nums(a[i], a[i+1]))
                end
            end

            if !(length(a) == length(lst))
                append!(lst, a[length(a)])
            end

            j += 1
            push!(temp, lst)
        end
        @label escape
    end

    return temp
end
println("----------------------------------")
println(test())
#=
a[1] + a[2] ...........
a[1] + a[2] + a[3] + a[4] ........
a[1] + a[2] + a[3] + a[4] + a[5] + a[6] ........
a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] + a[8] ...........
.. a[2]

for i = 1:length(a)
    combine_nums(a[i], a[i+1])
    for j = i+1 : length(a)
=#
