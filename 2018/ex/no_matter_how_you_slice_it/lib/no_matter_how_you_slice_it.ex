defmodule NoMatterHowYouSliceIt do

  defmodule ClaimParser do
    import NimbleParsec

    id =
      ignore(string("#"))
      |> integer(min: 1)

    position =
      integer(min: 1)
      |> ignore(string(","))
      |> integer(min: 1)

    size =
      integer(min: 1)
      |> ignore(string("x"))
      |> integer(min: 1)

    defparsec :claim, id |> ignore(string(" @ ")) |> concat(position) |> ignore(string": ")
      |> concat(size)
  end

  #

  defmodule Claim do
    defstruct id: 0, x: 0, y: 0, width: 0, height: 0

    def parse(s) do
      {:ok, [id, x, y, width, height], _, _, _, _} = ClaimParser.claim(s)
      %Claim{id: id, width: width, height: height, x: x, y: y}
    end

    def points(claim) do
      for y <- claim.y..claim.y+claim.height-1, x <- claim.x..claim.x+claim.width-1 do
        {x, y}
      end
    end
  end

  #

  def add_point(canvas, point) do
    Map.update(canvas, point, 1, fn v -> v + 1 end)
  end

  def add_claim(canvas, claim) do
    claim
    |> Claim.points()
    |> Enum.reduce(canvas, fn point, canvas -> add_point(canvas, point) end)
  end

  def claim_is_intact(canvas, claim) do
    claim
    |> Claim.points()
    |> Enum.all?(fn point -> Map.get(canvas, point) == 1 end)
  end

  #

  def read_input() do
    File.read!("assets/input.txt")
    |> String.split("\n", trim: true)
    |> Enum.map(&Claim.parse/1)
  end

  def part1() do
    read_input()
    |> Enum.reduce(%{}, fn claim, canvas -> add_claim(canvas, claim) end)
    |> Map.values()
    |> Enum.count(fn point -> point > 1 end)
  end

  def part2() do
    input = read_input()

    canvas =
      input
      |> Enum.reduce(%{}, fn claim, canvas -> add_claim(canvas, claim) end)

    claim_id =
      input
      |> Enum.find(fn claim -> claim_is_intact(canvas, claim) end)
      |> Map.get(:id)

    claim_id
  end

end
