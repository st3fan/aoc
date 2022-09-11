defmodule Dive do

  defmodule Submarine do

    use GenServer

    def init(part) do
      {:ok, %{position: 0, depth: 0, aim: 0, part: part}}
    end

    def handle_cast({:up, distance}, %{part: :part1} = state) do
      {:noreply, %{state | depth: state.depth - distance}}
    end

    def handle_cast({:down, distance}, %{part: :part1} = state) do
      {:noreply, %{state | depth: state.depth + distance}}
    end

    def handle_cast({:forward, distance}, %{part: :part1} = state) do
      {:noreply, %{state | position: state.position + distance}}
    end

    def handle_cast({:up, units}, %{part: :part2} = state) do
      {:noreply, %{state | aim: state.aim - units}}
    end

    def handle_cast({:down, units}, %{part: :part2} = state) do
      {:noreply, %{state | aim: state.aim + units}}
    end

    def handle_cast({:forward, units}, %{part: :part2} = state) do
      {:noreply, %{state | position: state.position + units, depth: state.depth + (state.aim * units)}}
    end

    def handle_call(:position, _from, state) do
      {:reply, state.position, state}
    end

    def handle_call(:depth, _from, state) do
      {:reply, state.depth, state}
    end

    #

    def start_link(part)  do
      GenServer.start_link(__MODULE__, part)
    end

    def control(pid, message) do
      GenServer.cast(pid, message)
    end

    def position(pid) do
      GenServer.call(pid, :position)
    end

    def depth(pid) do
      GenServer.call(pid, :depth)
    end

  end

  def read_input!(path) do
    File.read!(path)
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [command, distance] -> [String.to_atom(command), String.to_integer(distance)] end)
    |> Enum.map(&List.to_tuple/1)
  end

  def part1() do
    {:ok, submarine_pid} = Submarine.start_link(:part1)
    read_input!("assets/input.txt")
    |> Enum.each(fn message -> Submarine.control(submarine_pid, message) end)
    Submarine.position(submarine_pid) * Submarine.depth(submarine_pid)
  end

  def part2() do
    {:ok, submarine_pid} = Submarine.start_link(:part2)
    read_input!("assets/input.txt")
    |> Enum.each(fn message -> Submarine.control(submarine_pid, message) end)
    Submarine.position(submarine_pid) * Submarine.depth(submarine_pid)
  end
end
