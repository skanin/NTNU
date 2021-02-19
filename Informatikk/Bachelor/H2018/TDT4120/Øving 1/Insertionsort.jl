function insertionsort!(liste)
    for j in 2:length(liste)
    	key = liste[j]
        i = j - 1
        while i > 0 && liste[i] > key
        	liste[i + 1] = liste[i]
            i = i - 1
        end
        liste[i + 1] = key
        end
end
