function can_use_greedy(coins)
    for i in 1:length(coins)-1
        if coins[i]%coins[i+1] != 0
            return false
        end
    end
    return true
end

function min_coins_greedy(coins, value)
    liste = []
    if !can_use_greedy(coins)
        return 0
    else
        for i in 1:length(coins)
            while true
                if (value - coins[i]) >= 0
                    push!(liste, coins[i])
                    value = value - coins[i]
                else
                    break
                end
            end
        end
    end
    return length(liste)
end
#=
function aux(coins, value, memo = Dict())
    if (value == 0)
        memo[1] = 0;
        return 0
    end
    if value == 1
        memo[2] = 1
        return 1
    end

    liste = []
    for coin in coins
        if value - coin >= 0
            if memo[value - coin] == -typemax(Int)
                aux(liste, value - coin, memo)
            end
            push!(liste, memo[value-coin] + 1)
        end
    end
    println("Liste: ", liste)
    memo[value] = minimum(liste)
end

function min_coins_dynamic(coins, value)
    memo = [i for i in 0:value]
    for i in 1:length(memo)
        memo[i] = -typemax(Int)
    end
  aux(coins, value, memo)
  return memo[value]
end
=#

function min_coins_dynamic(coins, value)
    results = [typemax(Int) for i in 1:value]
    usefulCoins = []
    for coin in coins
        if coin <= value
            results[coin] = 1
            push!(usefulCoins, coin)
        end
    end
    for curVal in 1:value
        if results[curVal] != typemax(Int)
            continue
        end
        best = typemax(Int)
        for coin in usefulCoins
            if coin < curVal
                current = 1 + results[curVal - coin]
                if current < best
                    best = current
                end
            end
        end
        results[curVal] = best
    end
    return results[value]
end
#=
function aux(coins, value, r)
    if value != 0
        if r[value] >= 0
            return r[n]
        end
    end
    if value == 0
        q = 0
    else
        q = -typemax(Int)
    end
    for i in 1:length(coins)
        temp = coins[i] + aux(coins, value-i, r)
        q = max(temp, q)
    end
    r[value] = q
    return q
end

function min_coins_dynamic(coins, value)
    #=
    count = [0]
    for i in length(count):value
        push!(count, count[i-1] + 1)
        for coin in coins
            if coin <= i && (count[i-coin] + 1 < count[i])
                count[i] = count[i-coin] + 1
            end
        end
    end

    return count[value]=#
    #=
    q = -typemax(Int)
    r = [q for i in 1:value]
    println(r)
    return aux(coins, value, r)=#
    r = [i for i in 1:value]
    r[1] = 0
    for j in 2:value
        q = -typemax(Int)
        for i in q:j
            q = max(q, coins[i] + coins[j-i])
        end
        r[j] = q
    end
    return r[value]
end=#
println(min_coins_dynamic([1000,500,100,20,5,1],1226))
