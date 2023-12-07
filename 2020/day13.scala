
object Day13 extends App {
    val start: Int = 1000434
    val busses: List[Int] = List(17,0,0,0,0,0,0,41,0,0,0,0,0,0,0,0,0,983,0,29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,23,0,0,0,0,0,0,0,397,0,0,0,0,0,37,0,0,0,0,0,0,13)
    val bustimes: List[Int] = List(17,41,983,29,19,23,397,37,13)

    def getMinTime(bus: Int): Int = {
        start + (bus - (start % bus))
    }

    //part 1
    val answer: (Int, Int) = bustimes.map(getMinTime(_)).zip(bustimes).minBy(_._1)
    println( (answer._1 - start) * answer._2 )

    //part 2
    //val buspattern: List[(Int, Int)] = busses.zipWithIndex.filter(_._1 != 0)

    //def checkBus(timestamp: Long, index: Int, bus: Int): Boolean = {
    //    (timestamp + index) % bus == 0
    //}

    //def checkPos(busses: List[(Int, Int)], timestamp: Long, jump: Int): Long = {
    //    busses.forall( { case (bus, index) => checkBus(timestamp, index, bus) } ) match {
    //        case false => checkPos(busses, timestamp + jump, jump)
    //        case true => timestamp
    //    }
    //}

    //println(checkPos(buspattern.tail, 0, buspattern.head._1))
}
