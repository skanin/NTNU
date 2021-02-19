function cut_rod(p, n)
    if n == 0
        return 0
    end

    q = -typemax(Float64)
    for i=1:n
        q = max(q, p[i] + cut_rod(p, n-1))
    end

    return q
end

a = [3,5,4,2,1,4,6,7]
println(cut_rod(a, length(a)))
