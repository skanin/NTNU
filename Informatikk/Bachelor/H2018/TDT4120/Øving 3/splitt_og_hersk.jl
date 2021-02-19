using Traceur

function bisect_left(A, p, r, v)
    i = p
    if p < r
       q = floor(Int, (p+r)/2)  # floor() er en innebygd funksjon som runder ned. ceil() runder opp.
       if v <= A[q]
           i = bisect_left(A, p, q, v)
       else
           i = bisect_left(A, q+1, r, v)
       end
    end
    return i
end

function bisect_right(A, p, r, v)
    i = p
    if p < r
       q = floor(Int, (p+r)/2)  # floor() er en innebygd funksjon som runder ned. ceil() runder opp.
       if v + 1 <= A[q]
           i = bisect_right(A, p, q, v)
       else
           i = bisect_right(A, q+1, r, v)
       end
    end
    return i
end

function algdat_sort!(A)

    function partition!(A, lo, hi)
        pivot = A[hi]
        i = lo
        for j in lo:(hi-1)
            if A[j] < pivot
                A[i], A[j] = A[j], A[i]
                i = i + 1
            end
        end
        A[i], A[hi] = A[hi], A[i]
        return i
    end


    function quicksort!(A, lo, hi)
        if lo < hi
            p = partition!(A, lo, hi)
            quicksort!(A, lo, p-1)
            quicksort!(A, p+1, hi)
        end
    end

    A = quicksort!(A, 1, length(A))

end

function find_median(A, lower, upper)
    algdat_sort!(A)
    nyListe = A[bisect_left(A, 1, length(A) + 1, lower):(bisect_right(A, 1, length(A) + 1, upper) - 1)]

    println(nyListe)
    if length(nyListe)%2 == 0
        median = (nyListe[trunc(Int, length(nyListe)/2)] + nyListe[trunc(Int, (length(nyListe)/2) + 1)])/2
    else
        median = (nyListe[trunc(Int, ceil(length(nyListe)/2))])
    end
    return median
end
