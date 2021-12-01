use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead};

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    /* Part 1
    if let Ok(lines) = read_lines("input.txt") {
        // Iterator
        let mut count: i32 = 0;
        let mut previous_altitude = i32::MAX;
        for line in lines {
            if let Ok(ip) = line {
                let current_altitude: i32 = ip.parse().unwrap();
                if current_altitude > previous_altitude {
                    count += 1;
                }
                previous_altitude = current_altitude
            }
        }
        println!("{}", count);
    }
    */

    if let Ok(lines) = read_lines("input.txt") {
        // Iterator
        let mut count: i32 = 0;
        let mut vec = Vec::<i32>::new();
        for line in lines {
            if let Ok(ip) = line {
                vec.push(ip.parse().unwrap());
            }
        }
        for i in 3..vec.len() {
            if vec[i] > vec[i - 3]{
                count += 1
            }
        }
        println!("{}", count);
    }



}
