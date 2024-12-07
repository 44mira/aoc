local grid = require("grid")
local part1 = require("part1")

local filename = arg[1] or "../test.txt"

local input_grid = grid.new()
for line in io.lines(filename) do
	local row = {}
	for c in line:gmatch(".") do
		table.insert(row, c)
	end

	table.insert(input_grid, row)
end

print(part1.solve(input_grid, input_grid:guard_index()))
