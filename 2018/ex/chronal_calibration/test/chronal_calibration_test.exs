defmodule ChronalCalibrationTest do
  use ExUnit.Case
  doctest ChronalCalibration

  test "Part 1" do
    assert ChronalCalibration.part1() == 490
  end

  test "Part 2" do
    assert ChronalCalibration.part2() == 70357
  end
end
