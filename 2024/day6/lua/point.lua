local Point = {
	mt = {},

	---@class Point
	---@field x integer
	---@field y integer
	prototype = {
		x = 0,
		y = 0,
	},
}

Point.mt.__index = Point.prototype
setmetatable(Point, {
	__call = function(_, x, y)
		return Point.new(x, y)
	end,
})

---move a point by a direction
---@param a Point
---@param b Direction
---@return Point
function Point.mt.__add(a, b)
	return Point(a.x + b.x, a.y + b.y)
end

---@param self Point
---@return string
function Point.mt.__tostring(self)
	return ("P(%d, %d)"):format(self.x, self.y)
end

function Point.mt.__eq(a, b)
	return a.x == b.x and a.y == b.y
end

---@param x integer
---@param y integer
---@return Point
function Point.new(x, y)
	local ret = {}
	ret.x = x
	ret.y = y

	setmetatable(ret, Point.mt)

	return ret
end

return Point
