package.path = "../../../?.lua;" .. package.path

local matrix = require("matrix")
local solution = require("solution")

local filename = arg[1] or "../test.txt"

---@type string[]
local lines = {}
for line in io.lines(filename) do
	local row = {}
	for char in line:gmatch("%a") do
		table.insert(row, char)
	end
	table.insert(lines, row)
end

local parsed_input = matrix(lines)

local part1 = solution.part1(parsed_input)
local part2 = solution.part2(parsed_input)

print(part1)
print(part2)
