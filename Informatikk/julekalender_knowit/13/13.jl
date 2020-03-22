function is_prime(n)
    if n == 2
        return true
    end

    if n % 2 == 0
        return false
    end

    for i = 3 : 2 : Int(round(n^0.5+0.5))
        if n % i == 0
            return false
        end
    end
    return true
end


a = [1, 3]
primes = [3]
function find_seq(k = 1)
    if length(primes) == 100
        return sum(primes)
    end

    temp = []
    for i = 1 : length(a)-1
        for j = i+1 : length(a)
            if a[i] + a[j] > a[length(a)] + k || length(temp) > 1
                break
            end
            if a[i] + a[j] == a[length(a)] + k
                append!(temp, a[i]+a[j])
            end
        end
    end

    if length(temp) == 1
        if is_prime(temp[1])
            append!(primes, temp[1])
        end
        append!(a, temp[1])
        k = 1
        return find_seq(k)
    end
    return find_seq(k+1)
end

println(find_seq())
