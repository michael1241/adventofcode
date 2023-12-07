import scala.io.Source

object Day10 extends App {
    val data: List[Int] = 0 +: Source.fromFile("day10in").mkString.split("\\n").toList.flatMap(_.toIntOption).sorted

    def getDiffs(l: List[Int], output: List[Int]): List[Int] = {
        l match {
            case a :: b :: Nil => output :+ (b-a)
            case a :: b :: rest => getDiffs(b :: rest, output :+ (b-a))
            case _ => output
        }
    }

    val result = getDiffs(data, Nil)
    println(result.count(_ == 1) * (result.count(_ == 3)+1))
}
