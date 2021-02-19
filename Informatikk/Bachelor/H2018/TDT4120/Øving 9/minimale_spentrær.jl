try
    mutable struct DisjointSetNode
    rank::Int
    p::DisjointSetNode
    DisjointSetNode() = (obj = new(0); obj.p = obj;)
    end
catch

end

function makeset(x::DisjointSetNode)
    x.p = x
    x.rank = 0
end

function findset(x::DisjointSetNode)
    if x != x.p
        x = findSet(x.p)
    end
    return x.p
end

function Link(x,y)
    if x.rank > y.rank
        y.p = x
    else
        x.p = y
        if x.rank == y.rank
            y.rank = y.rank + 1
        end
    end
end

function unionn!(x::DisjointSetNode, y::DisjointSetNode)
    Link(findset(x), findset(y))
end

#=
function generic-MST(G, w)
    A = #tom mengde
    while #A ikke er spenntre
        #finn kant (u, w) som er safe for A
        A = #A UNION {(u, v)}

end
=#

function hammingdistance(s1::String, s2::String)
    count = 0
    for i in 1:length(s1)
        if s1[i] != s2[i]
            count = count + 1
        end
    end
    return count
end

#println(hammingdistance("ATG", "GTA"))

function Kruskal(G, w)
    A = Set()
    for v in G.v
        makeset(v)
    end
    sort!(G.e)
    for u, v in G.e
        if findset(u) != findset(v)
            A = union!(A, {u, v})
            unionn!(u, v)
        end
    end
    return A
end

function findclusters(E::Vector{Tuple{Int, Int, Int}}, n::Int, k::Int)

end
