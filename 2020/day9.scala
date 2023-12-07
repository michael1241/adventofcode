import scala.io.Source
import util.control.Breaks._

object Day9 extends App {
    def twoSum(nums: List[Int], target: Int): Boolean = {
        for {
            (v1, i1) <- nums.zipWithIndex
            (v2, i2) <- nums.zipWithIndex
            if i1 < i2
            if v1 + v2 == target
            } yield true
        }.headOption.getOrElse(false)
    
    val data: List[Int] = Source.fromFile("day9in").mkString.split("\\n").flatMap(_.toIntOption).toList

    def part1(data: List[Int]): Int = {
        if (twoSum(data.take(25), data.lift(25).getOrElse(0)))
            part1(data.drop(1))
        else data.lift(25).getOrElse(0)
    }
    //println(part1(data))
    val weakness: Int = 14360655

    def contigSum(nums: List[Int], target: Int): IndexedSeq[Int] = {
        for {
            front <- 0 to nums.length
            back <- front to nums.length
            val section: List[Int] = nums.slice(front, back)
            if section.sum == target
        } yield (section.min + section.max)
    }
    println(contigSum(data, weakness))
}
