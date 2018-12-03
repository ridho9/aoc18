use std::fs;
use std::collections::HashSet;

fn main() {
    let s = fs::read_to_string("input_big").unwrap();
    // let s = include_str!("input_big");
    let words: Vec<_> = s.lines().collect();

    for j in 0..words[0].len() {
        let mut seen: HashSet<String> = HashSet::new();

        for word in words.iter() {
            let mut subword = String::from(&word[..j]);
            subword.push_str(&word[j+1..]);

            if seen.contains(&subword) {
                println!("{}", subword);
                return;
            }

            seen.insert(subword);
        }
    }
}