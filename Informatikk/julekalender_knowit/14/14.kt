import java.io.File
import java.util.Collections.max
import java.util.Collections.min

fun main(args: Array<String>) {
    val f = File("src/input-bounding-crisscross.txt").readText()
    val coordinates : MutableList<Pair<Int, Int>> = mutableListOf(Pair(1, 1))

    var count = 0

    for(i in 1 until f.length step 2){
        when(f[i]){
            'H' -> {
                for(j in 1 until f[i-1].toString().toInt() + 1){
                    val lastCoordinate = coordinates[coordinates.size-1]
                    val x = lastCoordinate.first
                    val y = lastCoordinate.second
                    coordinates.add(Pair(x+1, y))
                }
            }
            'F' -> {
                for(j in 1 until f[i-1].toString().toInt() + 1){
                    val lastCoordinate = coordinates[coordinates.size-1]
                    val x = lastCoordinate.first
                    val y = lastCoordinate.second
                    coordinates.add(Pair(x, y+1))
                }
            }
            'B' -> {
                for(j in 1 until f[i-1].toString().toInt() + 1){
                    val lastCoordinate = coordinates[coordinates.size-1]
                    val x = lastCoordinate.first
                    val y = lastCoordinate.second
                    coordinates.add(Pair(x, y-1))
                }
            }
            'V' -> {
                for(j in 1 until f[i-1].toString().toInt() + 1){
                    val lastCoordinate = coordinates[coordinates.size-1]
                    val x = lastCoordinate.first
                    val y = lastCoordinate.second
                    coordinates.add(Pair(x-1, y))
                }
            }
        }
        count += f[i-1].toString().toInt()
    }

    val x_coordinates : MutableList<Int> = mutableListOf()
    val y_coordinates : MutableList<Int> = mutableListOf()

    for(elem in coordinates.toSet()){
        x_coordinates.add(elem.first)
        y_coordinates.add(elem.second)
    }

    val max_x = max(x_coordinates)
    val min_x = min(x_coordinates)
    val min_y = min(y_coordinates)
    val max_y = max(y_coordinates)

    val area = (max_x-min_x + 1)*(max_y-min_y + 1)
    val space = area - coordinates.toSet().size
    println("Lengden på unik liste: ${coordinates.toSet().size}")
    println("Empty: $space")
    println("Count: $count")
    println("Areal: $area")
    println("%.16f".format(coordinates.toSet().size.toDouble()/space.toDouble()))
 }