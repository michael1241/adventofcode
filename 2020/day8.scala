import scala.io.Source
import util.control.Breaks._

object Day8 extends App {
    case class Instruction(command: String, size: Int, traversed: Boolean, finished: Boolean)
    case class State(instrs: Vector[Instruction], index: Int, accumulator: Int)

    val data: Vector[Vector[String]] = Source.fromFile("day8in").mkString.split("\\n").toVector.map(_.split(" ").toVector)
    val instructions: Vector[Instruction] = (data collect {case Vector(a, b) => Instruction(a, b.toIntOption.getOrElse(0), false, false)}) :+ Instruction("nop", 1, true, true)

    def run(s: State): Int = {
        def nop(s: State): State =
            State(s.instrs.updated(s.index, s.instrs(s.index).copy(traversed=true)), s.index + 1, s.accumulator)
        def acc(s: State): State =
            State(s.instrs.updated(s.index, s.instrs(s.index).copy(traversed=true)), s.index + 1, s.accumulator + s.instrs(s.index).size)
        def jmp(s: State): State =
            State(s.instrs.updated(s.index, s.instrs(s.index).copy(traversed=true)), s.index + s.instrs(s.index).size, s.accumulator)

        s.instrs.lift(s.index).fold(-1) { instr =>
            if (instr.finished) s.accumulator
            if (instr.traversed) -1
            else instr.command match {
                case "nop" => run(nop(s))
                case "acc" => run(acc(s))
                case "jmp" => run(jmp(s))
                case _     => -1
            }
        }
    }

    def flip(command: String): String =
        if (command == "jmp") return "nop" else "jmp"

    for (i <- (0 to instructions.length)){
            val current = instructions(i)
            if (current.command == "acc") break
            else {
                val result = run(State(instructions.updated(i, current.copy(command=flip(current.command))), 0, 0))
                if (result != -1) println(result)
            }
    }

    //val result: Int = run(State(instructions, 0, 0)) 
    //println(result)
}
