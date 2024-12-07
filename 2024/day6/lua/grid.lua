local p = require("point")

---@class Grid
---@field guard_index fun(self: Grid): Point
---@field new fun(grid: Grid | nil): Grid
---@field at fun(self: Grid, ...: Point | integer): any
local Grid = {}

-- [[ METAMETHODS ]] {{{
local grid_mt = {}
grid_mt.__index = Grid

---@generic T
---@param self Grid<T>
---@return string
function grid_mt.__tostring(self)
	local ret = "\n"

	for _, row in ipairs(self) do
		for _, element in ipairs(row) do
			ret = ret .. element .. " "
		end
		ret = ret .. "\n"
	end

	return ret
end
-- }}}

---@param grid Grid | nil
---@return Grid
function Grid.new(grid)
	local ret = {}

	if grid then
		for _, v in ipairs(grid) do
			local row = {}
			for _, e in ipairs(v) do
				table.insert(row, e)
			end
			table.insert(ret, row)
		end
	end

	setmetatable(ret, grid_mt)

	return ret
end

---@param self Grid
---@return Point
function Grid:guard_index()
	for y, row in ipairs(self) do
		for x, c in ipairs(row) do
			if c:find("[>^v<]") then
				return p(x, y)
			end
		end
	end

	return p(-1, -1)
end

---@param self Grid
---@param ... Point | integer
---@return any
function Grid:at(...)
	if #{ ... } > 1 then
		local x, y = ...

		return self[y][x]
	end

	local point = ...
	return self[point.y][point.x]
end

return Grid
