defmodule Day2 do
  @spec parse_input(String.t()) :: [[integer()]]
  def parse_input(filename) do
    filename
    |> File.read!()
    |> String.split(~r{\n}, trim: true)
    |> Enum.map(fn line ->
      line
      |> String.split()
      |> Enum.map(&String.to_integer/1)
    end)
  end

  @doc ~s"""
  Checks if a row is safe.

  ## Examples
    
    iex> Day2.is_safe? [1,2,3,4]
    true
    iex> Day2.is_safe? [4,3,2,1]
    true
    iex> Day2.is_safe? [1,5,6,7]
    false
    iex> Day2.is_safe? [1,2,1,3]
    false
    
  """
  @spec is_safe?([integer()]) :: boolean()
  def is_safe?(row) do
    deltas =
      row
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.map(fn [a, b] -> b - a end)

    increasing_map = deltas |> Enum.all?(&Kernel.<(0, &1))
    decreasing_map = deltas |> Enum.all?(&Kernel.>(0, &1))

    bounded_map =
      deltas
      |> Enum.all?(fn a ->
        3 >= abs(a) and abs(a) >= 1
      end)

    (increasing_map or decreasing_map) and bounded_map
  end

  def part1(matrix) do
    matrix
    |> Enum.map(&if is_safe?(&1), do: 1, else: 0)
    |> Enum.sum()
  end

  def main do
    matrix = Day2.parse_input("../test.txt")

    matrix
    |> part1()
    |> IO.puts()
  end
end

Day2.main()
