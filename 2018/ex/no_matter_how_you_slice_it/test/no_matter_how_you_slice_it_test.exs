defmodule NoMatterHowYouSliceItTest do

  use ExUnit.Case

  alias NoMatterHowYouSliceIt.{Claim,ClaimParser}

  test "Parse a claim" do
    {:ok, [1, 1, 3, 4, 5], _, _, _, _} = ClaimParser.claim("#1 @ 1,3: 4x5")
    {:ok, [226, 440, 489, 28, 21], _, _, _, _} = ClaimParser.claim("#226 @ 440,489: 28x21")
    {:ok, [1295, 240, 934, 29, 28], _, _, _, _} = ClaimParser.claim("#1295 @ 240,934: 29x28")
  end

  test "Parse a claim into a Claim struct" do
    assert Claim.parse("#1 @ 1,3: 4x5") == %Claim{id: 1, width: 4, height: 5, x: 1, y: 3}
  end

  test "Part one" do
    assert NoMatterHowYouSliceIt.part1() == 105071
  end

  test "Part two" do
    assert NoMatterHowYouSliceIt.part2() == 222
  end

end
