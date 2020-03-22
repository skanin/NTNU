try
    mutable struct Record
    next::Union{Record,Nothing}  # next kan peke på et Record-objekt eller ha verdien nothing.
    value::Int
    end
catch

end

function createlinkedlist(length, valuerange)
    # Lager listen bakfra.
    next = nothing
    record = nothing
    for i in 1:length
        record = Record(next, rand(valuerange))  # valuerange kan f.eks. være 1:1000.
        next = record
    end
    return record
end

function traversemax(first_element)
    largest = first_element.value
    println(largest)
    current = first_element

    while true
        println(current.value)
        if current.value > largest
            largest = current.value
        end
        if current.next == nothing
            break
        else
            current = current.next
        end
    end
    return largest
end

lst = createlinkedlist(10, 1:600)
println(lst)
println(traversemax(lst))
