defmodule DiveTest do
  use ExUnit.Case

  test "part1" do
    assert Dive.part1() == 1855814
  end

  test "part2" do
    assert Dive.part2() == 1845455714
  end
end
