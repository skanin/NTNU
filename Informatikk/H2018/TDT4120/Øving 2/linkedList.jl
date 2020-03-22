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


function traversemax(record)
    max = record.value
    current_record = record
    while current_record != nothing
        if(max > current_record.value)
            current_record = current_record.next
            continue
        else
            max = current_record.value
            current_record = current_record.next
        end
    end
    return max
end




record5 = Record(nothing, 10000)
record4 = Record(record5, 672)
record3 = Record(record4, 74)
record2 = Record(record3, 30)
record1 = Record(record2, 10)

record = createlinkedlist(10, 1:100)
println(record)
println(traversemax(record1))
