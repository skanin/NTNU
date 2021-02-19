using DataStructures

try
    mutable struct Node
        ip::Int
        neighbours::Array{Tuple{Node,Int}}
        risk::Union{Float64, Nothing}
        predecessor::Union{Node, nothing}
        probability::Float64
    end
catch

end

Node(ip, prob) = Node(ip, [], nothing, nothing, prob)
n1 = Node(1, 4.3)

println(n1)

function initialize_single_source!(graph, start)
    for v in graph
        v.risk = typemax(Int)
        v.predecessor = nothing
    end
    start.risk = 0
end

function relax!(from_node,to_node,cost)
    if to_node.risk > from_node.risk + (cost/to_node.probability)
        to_node.risk = from_node.risk + (cost/to_node.probability)
        to_node.predecessor = from_node
    end
end

function dijkstra!(graph,start)
    initialize_single_source!(graph, start)
    S = []
    Q = Queue{Node}()
    for n in graph
        enqueue!(Q, n)
    end
    println(Q)
    while length(Q) > 0
        u = dequeue!(Q)
        push!(S, u)
        for n in u.neighbours
            relax!(u, n[1], n[2])
        end
    end
end
g = [Node(1,5.4), Node(2,3.6)]
dijkstra!(g, g[1])


function bellman_ford!(graph,start)
    initialize_single_source!(graph, start)
    for i = 1:length(graph)-1
        for n in graph[i].neighbours
            relax!(graph[i], n[1], n[2])
        end
    end
    for i = 1:length(graph)
        for n in graph[i].neighbours
            if n[1].risk > graph[i].risk + (n[2]/n[1].probability)
                return false
            end
        end
    end
    return true
end
