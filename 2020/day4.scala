import scala.io.Source
import scala.util.matching.Regex

object Day4 extends App {
    case class Passport(byr: Int, iyr: Int, eyr: Int, hgt: String, hcl: String, ecl: String, pid: String)
    case class PassportWFields(line: Map[String, String])

    def parseLine(l: String): Map[String, String] =
        l.split(' ').map(_ split ':').collect { case Array(k, v) => (k, v) }.toMap

    def makePerson(l: Map[String, String]): Option[Passport] = {
        for {
            byr <- l.get("byr").flatMap(_.toIntOption)
            iyr <- l.get("iyr").flatMap(_.toIntOption)
            eyr <- l.get("eyr").flatMap(_.toIntOption)
            hgt <- l.get("hgt")
            hcl <- l.get("hcl")
            ecl <- l.get("ecl")
            pid <- l.get("pid")
        } yield Passport(byr, iyr, eyr, hgt, hcl, ecl, pid)
    }

    def hasFields(l: Map[String, String]): Option[PassportWFields] = {
        val keys: Set[String] = Set("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        keys.subsetOf(l.keySet) match {
            case true => Some(PassportWFields(l))
            case _ => None
        }
    }

    def checkFields(passport: Passport): Boolean = {
        val hgtval: Int = passport.hgt.filter(_.isDigit).toInt
        val hgttype: String = passport.hgt.filter(_.isLetter).toString
        (
            passport.byr >= 1920 && passport.byr <= 2002 &&
            passport.iyr >= 2010 && passport.iyr <= 2020 &&
            passport.eyr >= 2020 && passport.eyr <= 2030 &&
            ((hgttype == "cm" && hgtval >= 150 && hgtval <= 193) || (hgttype == "in" && hgtval >= 59 && hgtval <= 76)) &&
            passport.hcl.matches("#[0-9a-f]{6}") &&
            passport.ecl.matches("amb|blu|brn|gry|grn|hzl|oth") &&
            passport.pid.matches("[0-9]{9}")
        )
    }

    val data: Array[String] = Source.fromFile("day4in").mkString.split("\\n\\n").map(_.replace("\n"," "))
    val parsed: Array[Map[String, String]] = data map parseLine
    val hasfields: Array[PassportWFields] = parsed flatMap hasFields
    val validated: Array[Passport] = parsed flatMap makePerson
    println(hasfields.length)
    println(validated count checkFields)
}
