local automata = require("automata")
local p = require("point")

local part2 = {}

---comment
---@param automata_grid Grid
---@param guard_index Point
---@return boolean
---@return Point
local function can_loop(automata_grid, guard_index)
	local turns = {}
	local facing = automata_grid:at(guard_index)

	-- set front into obstacle
	local front = automata.direction[facing]
	local front_cell = front + guard_index

	if front_cell.x > #automata_grid[1] or front_cell.x < 1 or front_cell.y > #automata_grid or front_cell.y < 1 then
		return false, p(-1, -1)
	end

	automata_grid[front_cell.y][front_cell.x] = "#"

	automata_grid[guard_index.y][guard_index.x] = automata.turn[facing]

	while true do
		if automata.check_front(automata_grid, guard_index) then
			local current_state = automata_grid:at(guard_index)
			automata_grid[guard_index.y][guard_index.x] = automata.turn[current_state]
			turns[tostring(guard_index)] = true
		else
			guard_index = automata.move(automata_grid, guard_index)
			if guard_index == p(-1, -1) then
				break
			end

			if turns[tostring(guard_index)] then
				return true, guard_index
			end
		end
	end

	return false, guard_index
end

local function restore_grid(automata_grid, guard_index, init_guard_index, init_state)
	-- remove obstacle
	local front = automata.direction[init_state]
	local front_cell = front + init_guard_index

	if
		not (front_cell.x > #automata_grid[1] or front_cell.x < 1 or front_cell.y > #automata_grid or front_cell.y < 1)
	then
		automata_grid[front_cell.y][front_cell.x] = "."
	end

	if guard_index.x ~= -1 and guard_index.y ~= -1 then
		automata_grid[guard_index.y][guard_index.x] = "."
	end
	automata_grid[init_guard_index.y][init_guard_index.x] = init_state
end

---@param automata_grid Grid
---@param guard_index Point
---@return integer
function part2.solve(automata_grid, guard_index)
	local loops_count = 0

	while true do
		if automata.check_front(automata_grid, guard_index) then
			local current_state = automata_grid:at(guard_index)
			automata_grid[guard_index.y][guard_index.x] = automata.turn[current_state]
		else
			-- prepare restore point
			local init_guard_index = p(guard_index.x, guard_index.y)
			local init_state = automata_grid:at(guard_index)

			-- perform a hypothetical run to check for loop when we do a right turn
			local check, new_guard_index = can_loop(automata_grid, guard_index)
			if check then
				loops_count = loops_count + 1
			end

			-- revert mutations caused by check_loop
			restore_grid(automata_grid, new_guard_index, init_guard_index, init_state)

			guard_index = automata.move(automata_grid, init_guard_index)
			if guard_index == p(-1, -1) then
				break
			end
		end
	end

	return loops_count
end

return part2
