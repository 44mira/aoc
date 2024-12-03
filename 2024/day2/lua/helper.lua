M = {}

---@generic T
---@generic G
---@param arr T[]
---@param zip_fn? fun(T, T): G
---@return table<[T,T] | G>
function M.rolling_window(arr, zip_fn)
	local ret = {}

	for i = 1, #arr - 1 do
		if zip_fn ~= nil then
			table.insert(ret, zip_fn(arr[i], arr[i + 1]))
		else
			table.insert(ret, { arr[i], arr[i + 1] })
		end
	end

	return ret
end

---@generic T
---@generic G
---@param arr T[]
---@param map_fn fun(T): G
---@return G[]
function M.map(arr, map_fn)
	local ret = {}

	for i, x in ipairs(arr) do
		ret[i] = map_fn(x)
	end

	return ret
end

---@param arr boolean[]
---@return boolean
function M.all(arr)
	local ret = true

	for _, e in ipairs(arr) do
		ret = ret and e
	end

	return ret
end

return M
