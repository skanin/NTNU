object task1 {

    // b) Sum array not recursive
    val sumArr = (arr: Array[Int]) => {
        var sum = 0;
        for(x <- 0 to (arr.length -1)){
            sum = sum + arr(x);
        }
        sum
    }

    // c) Sum array recursive
    def sumArrRec(arr: Array[Int]): Int = {
        // If the array is empty, return 0
        if(arr.isEmpty) 0
        // Else, return the head + the tail recursive
        else arr.head + sumArrRec(arr.tail)
    }

    // d) Fibonacci (with BigInt)
    def fib(n: BigInt): BigInt = {
        if((BigInt(0) == n)|(BigInt(1) == n)) n 
        else fib(n-BigInt(1)) + fib(n-BigInt(2))
    }

    def main(args: Array[String]){
        // a)
        var arr = new Array[Int](51);

        for(x <- 0 to 50){
            arr(x) = x;
        }



        // Print b
        println(sumArr(arr));

        // Print c
        println(sumArrRec(arr))

        // Print d
        println(fib(BigInt(10)))
    }
}
