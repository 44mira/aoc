---@meta

---@class Row

Row = {}
Row.mt = {}

---@overload fun(tbl : table): Row
Row = setmetatable(Row, {
	__call = function(_, tbl)
		return Row.new(tbl)
	end,
})

---@param self Row
---@return string
function Row.mt.__tostring(self)
	local ret = "[ "

	for i, elem in ipairs(self) do
		ret = ret .. elem

		if i ~= #self then
			ret = ret .. ", "
		end
	end

	ret = ret .. " ]"

	return ret
end

---@generic T
---@param row T[]
---@return Row
function Row.new(row)
	setmetatable(row, Row.mt)

	return row
end

return Row
