import scala.io.Source
import scala.language.postfixOps
import java.lang.Integer

object Day5 extends App {
    def convert(ticket: String): Int = {
        def letterToDigit(letter: Char): Option[Char] = {
            letter match {
                case 'F'|'L' => Some('0')
                case 'B'|'R' => Some('1')
                case _ => None
            }
        }
    val binary = (ticket.flatMap(letterToDigit)).mkString
    Integer.parseInt(binary, 2)
    }

    val input: List[String] = Source.fromFile("day5in").getLines.toList
    val converted: List[Int] = input map convert
    println(converted.max)

    val actuals = converted.toSet
    val possibles = (converted.min to converted.max).toSet

    println(possibles diff actuals)
}
