import scala.io.Source

object Day16 extends App {
    val List(rules, myticket, tickets) = Source.fromFile("day16in").mkString.split("\\n\\n").toList.map(_.split("\\n"))

    def parseTicket(values: String): List[Int] = {
        values.split(",").toList.map((s: String) => s.toIntOption).flatten
    }

    def parseRule(rules: String): Set[Int] = {
        rules match {
            case s"${rulename}: ${n1}-${n2} or ${n3}-${n4}" => ((n1.toInt to n2.toInt) ++ (n3.toInt to n4.toInt)).toSet
        }
    }
    val allTickets: List[List[Int]] = tickets.map(parseTicket(_)).toList
    val allRules: Set[Int] = rules.map(parseRule(_)).foldLeft(Set(): Set[Int])(_.union(_))

    println(allTickets.flatten.filter(!allRules.contains(_)).sum)
    //println(allTickets(1).size)
}
