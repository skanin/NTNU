/*object tasl2 {
    def function_that_returns_thread(callback: (Int, Int) => Int) {
        new Thread(new Runnable{
            callback()
        })
    }

    def main(args: Array[String]){
        val test = function_that_returns_thread((a: Int, b: Int) -> a*b)
        println(test(3, 5).start)
    }
}*/