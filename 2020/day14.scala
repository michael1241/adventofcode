import scala.io.Source

object Day14 extends App {
    case class Instruction(address: Int, value: BigInt)

    def translate(char: Char): Option[Int] = {
        char match {
            case '1' => Some(1)
            case '0' => Some(0)
            case 'X' => None
            }
    }

    def toMask(maskstring: String): List[Option[Int]] = {
        {maskstring map translate}.toList
    }

    def parse(input: String): Either[List[Option[Int]], Instruction] = {
        input match {
            case s"mask = ${mask}" => Left(toMask(mask))
            case s"mem[${address}] = ${value}" => Right(Instruction(address.toIntOption.getOrElse(0), BigInt(value)))
        }
    }

    def compare(valbit: Option[Int], maskbit: Option[Int]): Int = {
        maskbit match {
            case None => valbit.get
            case _ => maskbit.get
        }
    }

    def applyMask(value: BigInt, mask: List[Option[Int]]): BigInt = {
        val binvalue: List[Option[Int]] = {value.toString(2) map translate}.toList
        val binstring: String = binvalue.reverse.zipAll(mask.reverse, Some(0), Some(0)).map { case (a, b) => compare(a, b) }.reverse.mkString
        BigInt(binstring, 2)
    }

    def addElement(memory: Map[Int, BigInt], instr: Instruction, mask: List[Option[Int]]): Map[Int, BigInt] = {
        val newMemory: Map[Int, BigInt] = memory ++ Map(instr.address -> applyMask(instr.value, mask))
        newMemory
    }

    def process(data: List[Either[List[Option[Int]], Instruction]], mask: List[Option[Int]], memory: Map[Int, BigInt]): Map[Int, BigInt] = {
        data match {
            case Nil => memory
            case Left(head) :: tail => process(tail, head, memory)
            case Right(head) :: tail =>
                val updatedmemory: Map[Int,BigInt] = addElement(memory, head, mask)
                process(tail, mask, updatedmemory)
        }
    }

    val data: List[Either[List[Option[Int]], Instruction]] = Source.fromFile("day14in").mkString.split("\\n").toList.map(parse(_))
    val initMask: List[Option[Int]] = List(None)
    val initMemory: Map[Int, BigInt] = Map()

    println(process(data, initMask, initMemory).foldLeft(0: BigInt)(_+_._2) )
}
