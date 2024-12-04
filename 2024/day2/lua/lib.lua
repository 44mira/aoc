local h = require("helper")

local M = {}

--- parse the input lines into integer[][]
---@param lines string[]
---@return integer[][]
function M.parse_input(lines)
	local ret = {}

	for _, line in ipairs(lines) do
		local row = {}
		local iter = line:gmatch("%d")

		for num in iter do
			table.insert(row, num)
		end

		table.insert(ret, row)
	end

	return ret
end

---@param row integer[]
---@return boolean
function M.is_safe(row)
	---@type integer[]
	local pairs = h.rolling_window(row, function(a, b)
		return b - a
	end)

	local increase_map = h.map(pairs, function(a)
		return a > 0
	end)
	local decrease_map = h.map(pairs, function(a)
		return a < 0
	end)
	local bound_map = h.map(pairs, function(a)
		return 3 >= math.abs(a) and math.abs(a) >= 1
	end)

	return (h.all(increase_map) or h.all(decrease_map)) and h.all(bound_map)
end

---@param matrix integer[][]
---@return integer
function M.part1(matrix)
	local safe = 0

	for _, row in ipairs(matrix) do
		if M.is_safe(row) then
			safe = safe + 1
		end
	end

	return safe
end

return M
