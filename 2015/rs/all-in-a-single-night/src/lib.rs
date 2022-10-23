use itertools::Itertools;
use std::{
    collections::{HashMap, HashSet},
    fs,
    path::Path,
};

//

fn read_input_lines<P, T>(path: P, transformer: fn(&'_ str) -> T) -> std::io::Result<Vec<T>>
where
    P: AsRef<Path>,
{
    let mut input: Vec<T> = vec![];
    let contents = fs::read_to_string(path).unwrap();
    for line in contents.lines() {
        input.push(transformer(line));
    }
    Ok(input)
}

//

#[derive(PartialEq, Eq, Debug)]
struct Route {
    from: String,
    to: String,
    distance: i32,
}

impl Route {
    fn from_str(s: &str) -> Self {
        let components: Vec<&str> = s.split_ascii_whitespace().collect();
        Self {
            from: components[0].to_string(),
            to: components[2].to_string(),
            distance: components[4].parse().unwrap(),
        }
    }
}

fn read_routes() -> Vec<Route> {
    let routes: Vec<Route> = read_input_lines("input.txt", Route::from_str).unwrap();
    routes
}

fn cities_from_routes(routes: &Vec<Route>) -> HashSet<String> {
    let mut cities: HashSet<String> = HashSet::new();
    for route in routes {
        cities.insert(route.from.clone());
        cities.insert(route.to.clone());
    }
    cities
}

fn distances_from_routes(routes: &Vec<Route>) -> HashMap<Leg, i32> {
    let mut distances: HashMap<Leg, i32> = HashMap::new();
    for route in routes {
        distances.insert(
            Leg {
                a: route.from.clone(),
                b: route.to.clone(),
            },
            route.distance,
        );
        distances.insert(
            Leg {
                a: route.to.clone(),
                b: route.from.clone(),
            },
            route.distance,
        );
    }
    distances
}

//

#[derive(Clone, PartialEq, Eq, Debug, Hash)]
struct Leg {
    a: String,
    b: String,
}

//

fn trip_distance(trip: Vec<&String>, distances: &HashMap<Leg, i32>) -> i32 {
    // let mut distance = 0;
    // for (a, b) in trip.iter().tuple_windows() {
    //     let leg = &Leg {
    //         a: (**a).clone(),
    //         b: (**b).clone(),
    //     };
    //     distance += distances.get(leg).unwrap();
    // }
    // distance

    trip.iter()
        .tuple_windows()
        .map(|(a, b)| {
            distances
                .get(&Leg {
                    a: (**a).clone(),
                    b: (**b).clone(),
                })
                .unwrap()
        })
        .sum()
}

//

pub fn part1() -> i32 {
    let routes = read_routes();
    let cities = cities_from_routes(&routes);
    let distances = distances_from_routes(&routes);

    // let mut min_distance = i32::MAX;
    // for trip in cities.iter().permutations(cities.len()).unique() {
    //     let distance = trip_distance(trip, &distances);
    //     if distance < min_distance {
    //         min_distance = distance;
    //     }
    // }
    // min_distance

    cities
        .iter()
        .permutations(cities.len())
        .unique()
        .map(|trip| trip_distance(trip, &distances))
        .min()
        .unwrap()
}

pub fn part2() -> i32 {
    let routes = read_routes();
    let cities = cities_from_routes(&routes);
    let distances = distances_from_routes(&routes);

    // let mut max_distance = i32::MIN;
    // for trip in cities.iter().permutations(cities.len()).unique() {
    //     let distance = trip_distance(trip, &distances);
    //     if distance > max_distance {
    //         max_distance = distance;
    //     }
    // }
    // max_distance

    cities
        .iter()
        .permutations(cities.len())
        .unique()
        .map(|trip| trip_distance(trip, &distances))
        .max()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_route_from_str() {
        assert_eq!(
            Route::from_str("Amsterdam to Toronto = 1234"),
            Route {
                from: "Amsterdam".to_string(),
                to: "Toronto".to_string(),
                distance: 1234
            }
        );
    }

    //

    #[test]
    fn test_part1() {
        assert_eq!(part1(), 141);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(), 736);
    }
}
