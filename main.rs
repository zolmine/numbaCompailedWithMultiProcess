
fn main() {
    let mut allData = vec![];
    for i in 1..10000000 {
        if i % 2 == 0 {
            allData.push(i);
        } else {
            continue;
        }
    }
    println!("{}", allData.len());
}