import java.io.File

fun readIntegers(fileName: String): List<Int> = File(fileName).readLines().map { it.toInt() }

fun fuelRequired(mass: Int) = mass / 3 - 2

fun recursiveFuelRequired(fuel: Int): Int {
    val required = fuelRequired(fuel)
    if (required <= 0) {
        return 0
    }
    return fuel + recursiveFuelRequired(required)
}

fun one() {
    val total = readIntegers("Day01.data").map { fuelRequired(it) }.sum()
    println("Day 1.1: $total")
}

fun two() {
    val totalMass = readIntegers("Day01.data").map { fuelRequired(it) }.sum()
    val fuel = recursiveFuelRequired(totalMass)
    println("Day 1.2: $fuel")
}

fun main() {
    one()
    two()
}
