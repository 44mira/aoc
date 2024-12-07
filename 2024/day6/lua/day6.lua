local grid = require("grid")
local part1 = require("part1")
local part2 = require("part2")

local filename = arg[1] or "../input.txt"

local part1_grid = grid.new()
for line in io.lines(filename) do
	local row = {}
	for c in line:gmatch(".") do
		table.insert(row, c)
	end

	table.insert(part1_grid, row)
end

local part2_grid = grid.new(part1_grid)

print(part1.solve(part1_grid, part1_grid:guard_index()))
print(part2.solve(part2_grid, part2_grid:guard_index()))
