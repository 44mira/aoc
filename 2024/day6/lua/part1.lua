local automata = require("automata")
local p = require("point")

local part1 = {}

---@param automata_grid Grid
---@param guard_index Point
---@return integer
function part1.solve(automata_grid, guard_index)
	local unique_points = {}
	local unique_count = 0

	while true do
		if automata.check_front(automata_grid, guard_index) then
			local current_state = automata_grid:at(guard_index)
			automata_grid[guard_index.y][guard_index.x] = automata.turn[current_state]
		else
			guard_index = automata.move(automata_grid, guard_index)
			if guard_index == p(-1, -1) then
				break
			end

			if unique_points[tostring(guard_index)] == nil then
				unique_points[tostring(guard_index)] = true
				unique_count = unique_count + 1
			end
		end
	end

	return unique_count
end

return part1
