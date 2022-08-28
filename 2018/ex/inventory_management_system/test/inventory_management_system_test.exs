defmodule InventoryManagementSystemTest do
  use ExUnit.Case
  doctest InventoryManagementSystem

  test "Part One" do
    assert InventoryManagementSystem.part1() == 5166
  end

  test "Part Two" do
    assert InventoryManagementSystem.part2() == "cypueihajytordkgzxfqplbwn"
  end
end
