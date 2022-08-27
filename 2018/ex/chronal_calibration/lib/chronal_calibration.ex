defmodule ChronalCalibration do

  def read_input() do
    File.read!("assets/input.txt")
    |> String.trim()
    |> String.split()
    |> Enum.map(fn s -> String.to_integer(s) end)
  end

  #

  def part1() do
    read_input() |> Enum.sum()
  end

  #

  def part2() do
    _part2(read_input(), [], 0, MapSet.new([0]))
  end

  defp _part2(input, [], frequency, seen) do
    _part2(input, input, frequency, seen)
  end

  defp _part2(input, [head | tail], frequency, seen) do
    new_frequency = frequency + head
    if MapSet.member?(seen, new_frequency) do
      new_frequency
    else
      _part2(input, tail, new_frequency, MapSet.put(seen, new_frequency))
    end
  end

end
