defmodule SonarSweepTest do
  use ExUnit.Case
  doctest SonarSweep

  test "part1" do
    assert SonarSweep.part1() == 1532
  end

  test "part2" do
    assert SonarSweep.part2() == 1571
  end

  test "part2 optimized" do
    assert SonarSweep.part2_optimized() == 1571
  end
end
