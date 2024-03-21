package main

import (
	"fmt"
	"math"
)

func main() {
	a := 0
	b := 0
	c := 0
    escolha := 0
    
    for {
        fmt.Print("Primeiro numero: ")
    	fmt.Scanln(&a)
    	fmt.Print("Segundo numero: ")
    	fmt.Scanln(&b)
    	fmt.Print("Terceiro numero: ")
    	fmt.Scanln(&c)
    
    	delta := b*b - 4*a*c
    
    	if delta < 0 {
    		fmt.Println("Sem raizes reais")
    	} else if delta > 0 {
    		raiz_delta := math.Sqrt(float64(delta))
    		fmt.Println("Raiz 1:", (-float64(b)+raiz_delta)/(2*float64(a)))
    		fmt.Println("Raiz 2:", (-float64(b)-raiz_delta)/(2*float64(a)))
    	} else {
    	    raiz_delta := math.Sqrt(float64(delta))
    	    fmt.Println("Raizes iguais:", (-float64(b)+raiz_delta)/(2*float64(a)))   
    	}
    	
    	fmt.Print("Digite '1' para calcular novamente: ")
    	fmt.Scanln(&escolha)
    	if escolha != 1 {
    	    break
    	}
    }
}
