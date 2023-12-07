import scala.io.Source

object Day3 extends App {

    def parse(data: List[Char]):List[Boolean] = {
        def convert(char: Char): Option[Boolean] = {
            char match {
                case '#' => Some(true)
                case '.' => Some(false)
                case _ => None
            }
        }
        data flatMap convert
    }

    val data = Source.fromFile("day3in").getLines.toList
    val chardata = data.map(_.toList)
    val parsed = chardata map parse

    def calculate(parsed: List[List[Boolean]], xstep: Int, ystep: Int): Int = {

        val ys: Range = Range(ystep, parsed.length + ystep, ystep)
        val xs: Range = Range(xstep, ys.length * xstep, xstep)
        val coords = xs zip ys
        coords count { case (x, y) => parsed(y)(x % 31) }
    }

    val directions: List[(Int, Int)] = List((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    val results = directions.map( { case (x, y) => calculate(parsed, x, y) } )
    val output: Long = results.map(_.toLong).product
    println(output)
}
