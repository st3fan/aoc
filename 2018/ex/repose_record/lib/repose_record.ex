defmodule ReposeRecord do

  # [1518-09-02 00:00] Guard #2137 begins shift
  # [1518-05-01 00:45] falls asleep
  # [1518-08-15 00:47] wakes up

  defmodule Event do
    defstruct datetime: nil, guard: nil, event: nil
  end

  def read_input() do
    File.read!("assets/input.txt")
    |> Enum.sort()
  end

end
