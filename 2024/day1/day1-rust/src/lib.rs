use std::collections::HashMap;

pub fn part1(left: &mut Vec<i32>, right: &mut Vec<i32>) -> i32 {
    left.sort_unstable();
    right.sort_unstable();

    left.into_iter()
        .zip(right)
        .map(|(a, b)| (*a - *b).abs())
        .sum()
}

pub fn part2(left: Vec<i32>, right: Vec<i32>) -> i32 {
    let right = right.iter().fold(HashMap::new(), |mut counter, elem| {
        *counter.entry(elem).or_insert(0) += 1;
        return counter;
    });

    return left
        .into_iter()
        .map(|elem| right.get(&elem).map(|v| v * elem).unwrap_or(0))
        .sum();
}

pub fn parse_input(lines: &Vec<String>) -> (Vec<i32>, Vec<i32>) {
    return lines
        .into_iter()
        .map(|line| {
            let mut it = line.split_ascii_whitespace();
            let parse_num = |x: &str| x.parse().ok();

            return (
                it.next().and_then(parse_num).unwrap(),
                it.next().and_then(parse_num).unwrap(),
            );
        })
        .fold((vec![], vec![]), |(mut left, mut right), (a, b)| {
            left.push(a);
            right.push(b);
            return (left, right);
        });
}

#[cfg(test)]
mod tests {
    use super::*;

    static TEST_INPUT: &[&str] = &["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"];

    fn get_test_input() -> Vec<String> {
        return TEST_INPUT.iter().map(|x| x.to_string()).collect();
    }

    #[test]
    fn test_part1() {
        let (mut left, mut right) = parse_input(&get_test_input());
        assert_eq!(part1(&mut left, &mut right), 11);
    }

    #[test]
    fn test_part2() {
        let (left, right) = parse_input(&get_test_input());
        assert_eq!(part2(left, right), 31);
    }
}
