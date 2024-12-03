M = {}

---@param line string
---@return integer
function M.part1(line)
	local iter = line:gmatch("mul%((%d+),(%d+)%)")

	local result = 0
	for a, b in iter do
		result = result + a * b
	end

	return result
end

return M
