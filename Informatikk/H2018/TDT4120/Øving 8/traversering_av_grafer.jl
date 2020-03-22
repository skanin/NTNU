using DataStructures
try
    mutable struct Node
        id::Int
        neighbours::Array{Node}
        color::Union{String, Nothing}
        distance::Union{Int, Nothing}
        predecessor::Union{Node, Nothing}
    end
catch

end

#A
Node(id) = Node(id, [], nothing, nothing, nothing)
function makenodelist(adjacencylist)
    nodeList = []
    for i in 1:length(adjacencylist)
        node = Node(i)
        for j in 1:length(adjacencylist[i])
            push!(node.neighbours, Node(adjacencylist[i][j]))
        end
        push!(nodeList, node)
    end
    return nodeList
end

println("LISTE: ", makenodelist([[4], [3], [1, 2, 5], [3], [3]]))



listeMedNoder = makenodelist([[4], [3], [1, 2, 5], [3], [3]])
#println("--------------------------------------------------\nListe Med Noder: ", listeMedNoder)

function isgoalnode(node)
    listeMedNoder = makenodelist([[4], [3], [1, 2, 5], [3], [3]])
    return node == listeMedNoder[1]
end

function bfs!(nodes, start)
    for node in nodes
        if node == start
            continue
        end
        node.color = "white"
        node.distance = typemax(Int)
        node.predecessor = nothing
    end

    start.color = "gray"
    start.distance = 0
    start.predecessor = nothing

    q = Queue{Node}()
    enqueue!(q, start)

    while !isempty(q)
        u = dequeue!(q)
        for v in u.neighbours
            if isgoalnode(v)
                return v
            end

            if v.color == "white"
                v.color = "gray"
                v.distance = u.distance + 1
                v.predecessor = u
                enqueue!(q, v)

            end
        end
        u.color = "black"
    end
    return nothing
end

println(bfs!(listeMedNoder, listeMedNoder[1]))

function makepathto(goalnode)
    currentNode = goalnode
    path = []
    while currentNode.predecessor != nothing
        push!(path, currentNode.id)
        currentNode = currentNode.predecessor
    end

    temp = []
    for i in length(path):1
        push!(temp, path[i])
    end
    return temp
end
