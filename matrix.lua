---@meta

local row = require("row")

---@class Matrix
---@field rows Row[]

Matrix = {}
Matrix.mt = {}

---@overload fun(tbl : table): Matrix
Matrix = setmetatable(Matrix, {
	__call = function(_, tbl)
		return Matrix.new(tbl)
	end,
})

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

return Matrix
