weights = [3 6 8 6 3; 7 6 5 7 3; 4 10 4 1 6; 10 4 3 1 2; 6 1 7 3 9]

function cumulative(weights)
    rows, cols = size(weights)
    new_list = copy(weights)
    for i in 1:rows-1
        for j in 1:cols
            if j == 1
                new_list[i + 1, j] = min(new_list[i+1, j]+new_list[i, j], new_list[i, j+1]+new_list[i+1, j])
            elseif j == cols
                new_list[i + 1, j] = min(new_list[i+1, j]+new_list[i, j], new_list[i, j-1]+new_list[i+1, j])
            else
                new_list[i + 1, j] = min(new_list[i+1, j]+new_list[i, j], new_list[i+1, j]+new_list[i, j-1], new_list[i+1, j]+new_list[i, j+1])
            end
        end
    end
    return new_list
end

#println(cumulative(weights))
#=
function back_track(path_weights)
    rows, cols = size(path_weights)
    ny = []
    minst = (path_weights[rows, 1], 1)
    for i in rows:-1:1

        println("minst: ", minst)
        for j in 1:cols
            if i == rows
                if path_weights[i, j] < minst[1]
                    minst = (path_weights[i, j], j)
                    println("J: ", j)
                    println("Minst: ", minst)
                end

            elseif ny[length(ny)][2] == 1 || j == 1
                println("Øverste elseif: ", i)
                #=
                if j == ny[length(ny)][2]
                    minst = (min(path_weights[i, j], path_weights[i, j+1]), j)
                end=#
                if path_weights[i, j] < path_weights[i, j+1]
                    minst = (path_weights[i, j], j)
                else
                    minst = (path_weights[i, j+1], j+1)
                end
            elseif ny[length(ny)][2] == cols || j == cols
                println("Nest nederste elseif: ", i)
                if path_weights[i, j-1] < path_weights[i, j]
                    minst = (path_weights[i, j-1], j-1)
                else
                    minst = (path_weights[i, j], j)
                end
            else
                #=
                if j == ny[length(ny)][2]
                    #=
                    println("Hei, J er ", j, " I er ", i)
                    println("Ny 2 er ", ny[length(ny)][2])
                    println("J-1: ", path_weights[i, j-1])
                    println("J: ", path_weights[i, j])
                    println("J+1: ", path_weights[i, j+1])
                    =#
                    minst = (min(path_weights[i, j-1], path_weights[i, j], path_weights[i, j+1]), j)
                    break=#
                    println("Nederste elseif: ", i)
                    #println("J: ", j)
                    if j == ny[length(ny)][2]
                        println("J: ", j)
                        if path_weights[i, j-1] < path_weights[i, j] && path_weights[i, j-1] < path_weights[i, j+1]
                            minst = (path_weights[i, j-1], j-1)
                        elseif path_weights[i, j] < path_weights[i, j-1] && path_weights[i, j] < path_weights[i, j+1]
                            minst = (path_weights[i, j], j)
                        else
                            minst = (path_weights[i, j+1], j+1)
                        end
                    end
                end
        end
        #println("Minst: ", minst)
        push!(ny, (i, minst[2]))
    end
    return ny
end
=#

function back_track(w)
    rows, cols = size(w)
    ny = []
    for i in rows:-1:1
        minst = (w[i, 1], 1)
        for j in 1:cols
            if i == rows
                if w[i, j] < minst[1]
                    minst = (w[i, j], j)
                end
            elseif j == 1
                if w[i, j] < w[i, j+1]
                    minst = (w[i, j], j)
                else
                    minst = (w[i, j+1], j+1)
                end
            elseif j == cols
                if j == ny[length(ny)][2]
                    if w[i, j] < w[i, j-1]
                        minst = (w[i, j], j)
                    else
                        println("J: ", j)
                        minst = (w[i, j-1], j-1)
                    end
                end
            else
                if j == ny[length(ny)][2]
                    if (w[i, j] < w[i, j + 1])
                        if (w[i, j] < w[i, j - 1])
                            minst = (w[i, j], j)
                        else
                            minst = (w[i, j-1], j-1)
                        end
                    elseif (w[i, j] < w[i, j-1])
                        minst = (w[i, j], j)
                    else
                        minst = (w[i, j-1], j-1)
                    end
                end
            end
        end
        push!(ny, (i, minst[2]))
        println("NY: ", ny)
    end
    return ny
end

println(back_track(cumulative(weights)))
