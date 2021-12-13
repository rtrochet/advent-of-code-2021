import attr
import re

from typing import List, Set

coord_pattern = re.compile("[0-9]{1,4},[0-9]{1,4}")


@attr.dataclass(frozen=True)
class Coordinates:
	x: int = attr.ib(converter=int)
	y: int = attr.ib(converter=int)

	def fold_along(self, line_eqtn: str) -> "Coordinates":
		value = int(line_eqtn[2:])
		if line_eqtn.startswith("y="):
			if self.y <= value:
				y = self.y
			else:
				y = -1 * self.y + 2 * value
			return Coordinates(self.x, y)
		elif line_eqtn.startswith("x="):
			if self.x <= value:
				x = self.x
			else:
				x = -1 * self.x + 2 * value
			return Coordinates(x, self.y)
		else:
			raise Exception("oh no")


def print_plane(coordinates: Set[Coordinates]) -> None:

	def row_factory(length: int) -> str:
	 	return "." * length

	plane = []

	for row in range(0, (max([coord.y for coord in coordinates]) + 1)):
		plane.append(row_factory(max([coord.x for coord in coordinates]) + 1))

	for y_idx in range(0, len(plane) + 2):
		for x_idx in range(0, len(plane[0]) + 2):
			if Coordinates(x_idx, y_idx) in coordinates:
				plane[y_idx] = plane[y_idx][:x_idx] + "#" + plane[y_idx][x_idx+1:]

	total_dots = 0
	for row in plane:
		print(row)
		total_dots += row.count("#")
	print(total_dots)
	print()


with open("input.txt") as f:
	lines = [line.strip() for line in f.readlines()]

coordinates = {Coordinates(*line.split(",")) for line in lines if re.match(coord_pattern, line)}
folding_eqtns = [line[len("fold along "):] for line in lines if line.startswith("fold along ")]

print_plane(coordinates)
for folding_eqtn in folding_eqtns:
	coordinates = {coord.fold_along(folding_eqtn) for coord in coordinates}
	print_plane(coordinates)
