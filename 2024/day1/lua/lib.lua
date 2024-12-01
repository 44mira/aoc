M = {}

---@param left integer[]
---@param right integer[]
---@return integer
function M.part1(left, right)
	table.sort(left)
	table.sort(right)

	local sum = 0
	for i = 1, #left do
		sum = sum + math.abs(left[i] - right[i])
	end

	return sum
end

---@param left integer[]
---@param right integer[]
---@return integer
function M.part2(left, right)
	local counts_right = {}
	local counts_left = {}

	-- hashmap for counts
	for i = 1, #left do
		if counts_right[right[i]] == nil then
			counts_right[right[i]] = 0
		end
		if counts_left[left[i]] == nil then
			counts_left[left[i]] = 0
		end

		counts_right[right[i]] = counts_right[right[i]] + 1
		counts_left[left[i]] = counts_left[left[i]] + 1
	end

	-- set default
	setmetatable(counts_right, {
		__index = function()
			return 0
		end,
	})

	local result = 0
	for k, v in pairs(counts_left) do
		result = result + (k * v * counts_right[k])
	end

	return result
end

---@param lines string[]
---@return integer[], integer[]
function M.parse_input(lines)
	local left = {}
	local right = {}

	for _, line in ipairs(lines) do
		local pair = line:gmatch("%d+")
		table.insert(left, pair())
		table.insert(right, pair())
	end

	return left, right
end

return M
