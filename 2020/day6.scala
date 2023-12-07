import scala.io.Source

object Day6 extends App {
    val data: Array[String] = Source.fromFile("day6in").mkString.split("\\n\\n")
    val groups: Array[Array[Set[String]]] = data.map(_.split("\\n")).map(_.map(_.split("").toSet))

    def grouptransform(group: Array[Set[String]]): Int = {
        group.reduce(_.intersect(_)).size
    }
    println((groups map grouptransform).sum)
}
