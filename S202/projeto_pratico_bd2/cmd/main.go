package main

import (
	"github.com/fiddelis/projeto_pratico_bd2/database"
	"github.com/fiddelis/projeto_pratico_bd2/internal/view"
)

func main() {
	database.ConnectDB()
	view.Options()
}
