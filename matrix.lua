---@meta

local row = require("row")

---@overload fun(tbl: table): Matrix
local Matrix = {}

setmetatable(Matrix --[[@as table]], {
	__call = function(_, tbl)
		return Matrix.new(tbl)
	end,
})

Matrix.mt = {}

---@class Matrix
---@field rows Row[]
---@field transpose? fun(self: Matrix): Matrix
Matrix.prototype = {}
Matrix.mt.__index = Matrix.prototype

---@param self Matrix
---@return string
function Matrix.mt.__tostring(self)
	local ret = "[\n"

	for _, row_data in ipairs(self.rows) do
		ret = ret .. "  " .. tostring(row_data) .. "\n"
	end

	ret = ret .. "]"

	return ret
end

---@generic T
---@param matrix T[][]
---@return Matrix
function Matrix.new(matrix)
	local ret = { rows = {} }
	for _, v in ipairs(matrix) do
		local row_data = row(v)
		table.insert(ret.rows, row_data)
	end

	setmetatable(ret, Matrix.mt)

	return ret
end

---@param self Matrix
---@return Matrix
function Matrix.prototype.transpose(self)
	local ret = {}
	for _, v in ipairs(self.rows) do
		local row_data = {}
		for _, _ in ipairs(v) do
			table.insert(row_data, "")
		end
		table.insert(ret, row_data)
	end

	for i = 1, #ret do
		for j = 1, #ret[i] do
			ret[i][j] = self.rows[j][i]
			ret[j][i] = self.rows[i][j]
		end
	end

	return Matrix(ret)
end

return Matrix
