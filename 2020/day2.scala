import scala.io.Source
import scala.util.matching.Regex

object Day2 extends App {
    case class Line(low: Int, high: Int, char: Char, password: String)

    def readFile(line: String): Option[Line] = {
        val info = "^([0-9]+)-([0-9]+) (.): ([^\\s]+)$".r
        line match {
            case info(low, high, char, password) =>
                for {
                    low <- low.toIntOption
                    high <- high.toIntOption
                    char <- char.lift(0)
                } yield Line(low, high, char, password)
            case _ => None
        }
    }

    val inputlines = Source.fromFile("day2in").getLines.toList

    val lines = inputlines.flatMap(readFile(_))

    def isValid(line: Line): Boolean = {
        val count = line.password.count(_ == line.char)
        (count >= line.low) && (count <= line.high)
    }

    def isValid2(line: Line): Boolean = {
        (line.password.charAt(line.low -1) == line.char) ^ (line.password.charAt(line.high -1) == line.char)
    }

    println(lines.count(isValid(_)))

    println(lines.count(isValid2(_)))
}
