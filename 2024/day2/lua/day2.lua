local lib = require("lib")

local filename = arg[1] or "../test.txt"

---@type string[]
local lines = {}
for line in io.lines(filename) do
	table.insert(lines, line)
end

local matrix = lib.parse_input(lines)

print(lib.part1(matrix))
