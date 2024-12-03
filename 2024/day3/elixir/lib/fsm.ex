defmodule Day3.Fsm do
  @spec handle_start(binary(), map()) :: map()
  def handle_start(inpt, state \\ %{ans: 0})
  def handle_start("", state), do: state
  def handle_start("m" <> tail, state) do
    new_state = Map.put(state, :prev, ?m)
    handle_mul(tail, new_state)
  end
  def handle_start(<<_::8>> <> tail, state), do: handle_start(tail, state)

  @spec handle_mul(binary(), map()) :: map()
  def handle_mul(inpt, state)
  def handle_mul("", state), do: state
  def handle_mul(<<head::8>> <> tail, state) do
    %{prev: previous} = state

    cond do
      String.contains?("mul", <<previous, head>>) ->
        handle_mul(tail, %{state | prev: head})

      <<previous, head>> == "l(" ->
        new_state = Map.put(state, :lhs, "")
        handle_param1(tail, new_state)

      true ->
        handle_start(tail, state)
    end
  end

  @spec handle_param1(binary(), map()) :: map()
  def handle_param1(inpt, state)
  def handle_param1("", state), do: state
  def handle_param1("," <> tail, state) do
    new_state = Map.put(state, :rhs, "")
    handle_param2(tail, new_state)
  end
  def handle_param1(<<head::8>> <> tail, state) when head in ?0..?9 do
    %{lhs: lhs} = state
    handle_param1(tail, %{state | lhs: lhs <> <<head>>})
  end
  def handle_param1(<<_::8>> <> tail, state), do: handle_start(tail, state)

  @spec handle_param2(binary(), map()) :: map()
  def handle_param2(inpt, state)
  def handle_param2("", state), do: state
  def handle_param2(")" <> tail, state) do
    %{lhs: lhs, rhs: rhs, ans: ans} = state
    val = String.to_integer(lhs) * String.to_integer(rhs)
    new_state = %{ans: ans + val}

    handle_start(tail, new_state)
  end
  def handle_param2(<<head::8>> <> tail, state) when head in ?0..?9 do
    %{rhs: rhs} = state
    handle_param2(tail, %{state | rhs: rhs <> <<head>>})
  end
  def handle_param2(<<_::8>> <> tail, state), do: handle_start(tail, state)
end
