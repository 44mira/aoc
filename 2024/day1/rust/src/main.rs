use day1_rust as aoc;

fn main() {
    let lines: Vec<String> = include_str!("../../input.txt")
        .lines()
        .map(String::from)
        .collect();

    let (mut left, mut right) = aoc::parse_input(&lines);
    let ans1 = aoc::part1(&mut left, &mut right);
    let ans2 = aoc::part2(&left, &right);

    println!("Part1: {ans1}");
    println!("Part2: {ans2}");
}
