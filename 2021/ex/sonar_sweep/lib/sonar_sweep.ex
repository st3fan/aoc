defmodule SonarSweep do

  def read_input!(path) do
    File.read!(path)
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end

  def part1() do
    read_input!("assets/input.txt")
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.count(fn [a,b] -> a < b end)
  end

  def part2() do
    read_input!("assets/input.txt")
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.count(fn [a, b] -> Enum.sum(b) > Enum.sum(a) end)
  end

  def part2_optimized() do
    read_input!("assets/input.txt")
    |> Enum.chunk_every(4, 1, :discard)
    |> Enum.count(fn [a, _, _, b] -> b > a end)
  end

end

# 1 2 3
#   2 3 4
