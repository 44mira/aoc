local M = {}

local function scan1(mtrx, i, j)
	local count = 0

	for dx = -1, 1 do
		for dy = -1, 1 do
			local x_max_leng = i + dx * 3
			local y_max_leng = j + dy * 3
			if
				not (
					x_max_leng < 1
					or x_max_leng > #mtrx.rows
					or y_max_leng < 1
					or y_max_leng > #mtrx.rows[i]
					or dx == 0 and dy == 0
				)
			then
				local pattern = {}
				for c = 1, 3 do
					table.insert(pattern, mtrx.rows[i + dx * c][j + dy * c])
				end
				local scanned = table.concat(pattern)

				if scanned == "MAS" then
					count = count + 1
				end
			end
		end
	end

	return count
end

---@param mtrx Matrix
---@return integer
function M.part1(mtrx)
	local count = 0

	for i = 1, #mtrx.rows do
		for j = 1, #mtrx.rows[i] do
			if mtrx.rows[i][j] == "X" then
				count = count + scan1(mtrx, i, j)
			end
		end
	end

	return count
end

---@param mtrx Matrix
---@param i integer
---@param j integer
---@return integer
local function scan2(mtrx, i, j)
	local topl_botr = mtrx.rows[i + 1][j + 1] == "M" and mtrx.rows[i - 1][j - 1] == "S"
		or mtrx.rows[i + 1][j + 1] == "S" and mtrx.rows[i - 1][j - 1] == "M"

	local botl_topr = mtrx.rows[i + 1][j - 1] == "M" and mtrx.rows[i - 1][j + 1] == "S"
		or mtrx.rows[i + 1][j - 1] == "S" and mtrx.rows[i - 1][j + 1] == "M"

	if topl_botr and botl_topr then
		return 1
	end

	return 0
end

---@param mtrx Matrix
---@return integer
function M.part2(mtrx)
	local count = 0

	for i = 2, #mtrx.rows - 1 do
		for j = 2, #mtrx.rows[i] - 1 do
			if mtrx.rows[i][j] == "A" then
				count = count + scan2(mtrx, i, j)
			end
		end
	end

	return count
end

return M
