"""Examples of set and dictionary syntax."""

pids: set[int] = {710000000, 712345678}
pids.add(730120710)

ice_cream: dict[str, int] = {
 "chocolate": 12,
 "vanilla": 8,
 "strawberry": 4,
}
ice_cream["vanilla"] += 110
ice_cream["mint"] = 3
print(ice_cream["chocolate"])
ice_cream["vanilla"] = 10

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")