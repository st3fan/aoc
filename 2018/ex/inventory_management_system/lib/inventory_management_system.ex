defmodule InventoryManagementSystem do

  def read_input() do
    File.read!("assets/input.txt")
    |> String.split()
    |> Enum.map(&String.codepoints/1)
  end

  defp has_doubles?(frequencies) do
    frequencies
    |> Map.values()
    |> Enum.any?(fn v -> v == 2 end)
  end

  defp has_triples?(frequencies) do
    frequencies
    |> Map.values()
    |> Enum.any?(fn v -> v == 3 end)
  end

  def part1() do
    frequencies =
      read_input()
      |> Enum.map(&Enum.frequencies/1)
    
    doubles =
      frequencies
      |> Enum.count(&has_doubles?/1)

    triples =
      frequencies
      |> Enum.count(&has_triples?/1)

    doubles * triples
  end

  #

  def differences(a, b) do
    Enum.zip(a, b)
    |> Enum.count(fn {a, b} -> a != b end)
  end

  def remove_difference({a, b}) do
    Enum.zip(a, b)
    |> Enum.filter(fn {a, b} -> a == b end)
    |> Enum.map(fn {a, _} -> a end)
  end

  def part2() do
    input = read_input()

    combinations = for x <- input, y <- input do
      {x, y}
    end

    combinations
    |> Enum.find(fn {a, b} -> differences(a, b) == 1 end)
    |> remove_difference()
    |> Enum.join()
  end

end
