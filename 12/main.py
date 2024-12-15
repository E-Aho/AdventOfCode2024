from collections import deque

from shapely import Point, union_all, box

from utils import run_day, get_grid_from_input, grid_get, get_adjacent_points


def get_region_from_point(array, point):
    running_region = {point}
    new_points = deque([point])
    plant_type = grid_get(array, *point)
    while new_points:
        p = new_points.pop()
        running_region.add(p)
        adj = [p for p in get_adjacent_points(p, array) if p not in running_region]
        for a in adj:
            if grid_get(array, *a) == plant_type:
                new_points.append(a)
    return running_region

def get_score(region, p2=False):
    points = [Point(p) for p in region]
    shape = union_all([box(point.x, point.y, point.x+1, point.y+1) for point in points])
    if not p2:
        return shape.area * shape.boundary.length

    boundary = shape.boundary.normalize().simplify(0.0)
    if boundary.is_ring:
        return shape.area * (len(boundary.coords) - 1)

    res = 0
    for line in boundary.geoms:
        res += shape.area * (len(line.coords) -1)
    return res

def main(input: str):
    array = get_grid_from_input(input)
    regions = []
    seen_points = set()
    for x in range(len(array)):
        for y in range(len(array[0])):
            if (x, y) not in seen_points:
                new_region = get_region_from_point(array, (x, y))
                seen_points.update(new_region)
                regions.append(new_region)

    scores = [get_score(region) for region in regions]
    print(sum(scores))
    p2_scores = [get_score(region, p2=True) for region in regions]
    print(sum(p2_scores))

if __name__ == "__main__":
    run_day(main, run_dev=False)