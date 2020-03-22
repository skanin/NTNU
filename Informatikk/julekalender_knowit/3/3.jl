function divisable(n, i)
    return n % i == 0
end

function is_prime(n)
    if n == 0
        return true
    end

    if n == 2
        return true
    end
    if divisable(n,2)
        return false
    end
    for i=3:2:Int(round(n^0.5+0.5))
        if divisable(n, i)
            return false
        end
    end
    return true
end

memo = Dict()
function primes(n, i = 2, count = 0, t = [])
    #=
    if haskey(memo, Int(n))
        return memo[Int(n)]
    else
        if is_prime(i) && divisable(n,i) && n > 1
            memo[n] = primes(Int(n/i), i) + 1
        else
            if n == 1 || n/i < 0
                return 1
            elseif is_prime(n)
                memo[n] = 1
                return memo[n]
            else
                memo[n] = primes(n, i+1, count)
            end
        end
    end
    return memo[n]  =#
    i = 2
    factors = []
    while i * i <= n
        if n % i != 0
            i += 1
        else
            n = Int(n/i)
            append!(factors, i)
        end
    end

    if n > 1
        append!(factors, n)
    end

    return length(factors)
end

lst = []
function juletall(n)
    count = 0

    for i = 2^24:2:n+1
        if primes(i) == 24
            println(i)
            #append!(lst, i)
            count += 1
        end
    end

    #=
    i = 2^24
    while i <= n+1
        if primes(i) == 24

            count += 1

        end
        println(i)
        i += sqrt(2^32)

    end=#
    return "Det er ", count, " juletall"
end

println(juletall(2^32))

#println("15 er delelig på 3: ", is_prime(15))
