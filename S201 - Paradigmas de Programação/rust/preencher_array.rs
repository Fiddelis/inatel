use std::io;

fn preencher_arr(arr: &mut [i32], x: i32) {
    for (i, elem) in arr.iter_mut().enumerate() {
        *elem = x * (i as i32);
    }
}

fn main() {
    let mut array = [0; 10];
    let mut input = String::new();

    println!("Digite um valor para multiplicar: ");
    io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler linha");

    let valor: i32 = input.trim().parse().expect("Digite um número válido");

    preencher_arr(&mut array, valor);

    println!("Array preenchido: {:?}", array);
}
