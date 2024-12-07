local p = require("point")

---@class Direction
---@field x integer
---@field y integer

local Automata = {}

-- [[ ENUMS ]] {{{

---@enum states
Automata.states = {
	UP = "^",
	RIGHT = ">",
	DOWN = "v",
	LEFT = "<",
}
local states = Automata.states

---@type Direction[]
Automata.direction = {
	[states.UP] = { x = 0, y = -1 },
	[states.RIGHT] = { x = 1, y = 0 },
	[states.DOWN] = { x = 0, y = 1 },
	[states.LEFT] = { x = -1, y = 0 },
}

---@type states[]
Automata.turn = {
	[states.UP] = states.RIGHT,
	[states.RIGHT] = states.DOWN,
	[states.DOWN] = states.LEFT,
	[states.LEFT] = states.UP,
}
-- }}}

---Check if the front is an obstacle
---@param input_grid Grid
---@param guard_index Point
---@return boolean
function Automata.check_front(input_grid, guard_index)
	local current_state = input_grid:at(guard_index)

	local front = Automata.direction[current_state]
	local front_cell = guard_index + front

	if front_cell.y > #input_grid or front_cell.y < 1 or front_cell.x > #input_grid[1] or front_cell.x < 0 then
		return false
	end

	return input_grid:at(front_cell) == "#"
end

---@param input_grid Grid
---@param guard_index Point
---@return Point
function Automata.move(input_grid, guard_index)
	local current_state = input_grid:at(guard_index)

	local move = Automata.direction[current_state]
	local new_move = guard_index + move

	input_grid[guard_index.y][guard_index.x] = "."

	local invalid_y = new_move.y > #input_grid or new_move.y < 1
	local invalid_x = new_move.x > #input_grid[1] or new_move.x < 1

	if invalid_x or invalid_y then
		return p(-1, -1)
	end

	input_grid[new_move.y][new_move.x] = current_state

	return new_move
end

return Automata
