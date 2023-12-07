import scala.io.Source

object Day11 extends App {

    case class Seat(x: Int, y: Int, occupied: Boolean)

    def validate(x: Int, y: Int, char: String): Option[Seat] =
            char match {
                case "#" => Some(Seat(x, y, true))
                case "L" => Some(Seat(x, y, false))
                case _ => None
            }

    val data: Vector[Vector[String]] = Source.fromFile("day11in").mkString.split("\\n").toVector.map(_.split("").toVector)

    val seats: Set[Seat] = { for {
            (y, yind) <- data.zipWithIndex
            (seat, xind) <- y.zipWithIndex
        } yield validate(xind, yind, seat)
    }.flatten.toSet

    def countNeighbors(current: Seat, seats: Set[Seat]): Int =
        seats count {
            seat: Seat =>
                seat != current &&
                math.abs(seat.x - current.x) <= 1 &&
                math.abs(seat.y - current.y) <= 1 &&
                seat.occupied
        }

    def nextSeat(seat: Seat, seats: Set[Seat]): Seat = {
        val neighbors: Int = countNeighbors(seat, seats)
        if (!seat.occupied && neighbors == 0) seat.copy(occupied = true)
        else if (seat.occupied && neighbors >= 4) seat.copy(occupied = false)
        else seat
    }

    def compute(seats: Set[Seat]): Int = {
        val newSeats = seats.map(nextSeat(_, seats))
        if (seats.count(_.occupied) == newSeats.count(_.occupied))
            return newSeats.count(_.occupied)
        else
            println(newSeats.count(_.occupied))
            compute(newSeats)
    }

    println(compute(seats))
}
