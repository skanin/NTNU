try
    struct Node
        children::Dict{Char,Node}
        posi::Array{Int}
    end
catch

end

# A

function parse_string(sentence)
    tempList = split(sentence, " ")
    returnList = Any[]
    for i = 1:length(tempList)
        if i == 1
            push!(returnList, (tempList[i], 1))
        else
            lengde = 0
            for j = 1:length(returnList)
                lengde = lengde + length(returnList[j][1])
                if j == i-1
                    push!(returnList, (tempList[i], lengde + i))
                end
            end
        end
    end
    return returnList
end

#B
Node() = Node(Dict(), [])

function build(list_of_words)
    toppNode = Node()
    for (ord, posisjon) in list_of_words
        node = toppNode
        for bokstav in ord
            if !(haskey(node.children, bokstav))
                node.children[bokstav] = Node()
            end
            node = node.children[bokstav]
        end
        append!(node.posi, posisjon)
    end
    return toppNode
end

#C
function positions(word, node, index=1)
    if index > length(word)
        return node.posi
    elseif word[index] == '?'
        posi = []
        for child in values(node.children)
            if  positions(word, child, index+1) != []
                posi = append!(posi, positions(word, child, index+1))
            end
        end
    elseif haskey(node.children, word[index])
        posi = positions(word, node.children[word[index]], index+1)
    else
        posi = []
    end
    return posi
end
