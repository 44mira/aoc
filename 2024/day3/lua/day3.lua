local lib = require("lib")

local filename = arg[1] or "../test.txt"

local lines = ""
for line in io.lines(filename) do
	lines = lines .. line
end

print(lib.part1(lines))
