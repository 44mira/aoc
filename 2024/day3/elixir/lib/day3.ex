defmodule Day3 do
  alias Day3.Fsm, as: Fsm

  defp parse_input(filename) do
    filename
    |> File.read!()
    |> String.replace(~r{\n}, "")
  end

  def main() do
    %{ans: ans} =
      "../test.txt"
      |> parse_input()
      |> Fsm.handle_start()

    ans
  end
end
