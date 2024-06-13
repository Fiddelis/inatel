package view

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"time"

	"github.com/fiddelis/projeto_pratico_bd2/internal/model"
	"github.com/fiddelis/projeto_pratico_bd2/internal/repository"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

func Options() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("\n\n\n\n\n")
		fmt.Println("Bem vindo às Notícias!")
		fmt.Println("Digite 1 para criar uma nova notícia")
		fmt.Println("Digite 2 para encontrar uma notícia por ID")
		fmt.Println("Digite 3 para listar todas as notícias")
		fmt.Println("Digite 4 para atualizar uma notícia")
		fmt.Println("Digite 5 para deletar uma notícia")
		fmt.Println("Digite 6 para sair")
		fmt.Print("Escolha uma opção: ")

		option, _ := reader.ReadString('\n')
		option = strings.TrimSpace(option)

		fmt.Println("\n\n\n\n\n")

		switch option {
		case "1":
			createNotice(reader)
		case "2":
			findNoticeByID(reader)
		case "3":
			findAllNotices(reader)
		case "4":
			updateNotice(reader)
		case "5":
			deleteNotice(reader)
		case "6":
			fmt.Println("Saindo...")
			return
		default:
			fmt.Println("Opção inválida, por favor tente novamente.")
		}
	}
}

func createNotice(reader *bufio.Reader) {
	fmt.Print("Digite o título da notícia: ")
	title, _ := reader.ReadString('\n')
	title = strings.TrimSpace(title)

	fmt.Print("Digite o conteúdo da notícia: ")
	content, _ := reader.ReadString('\n')
	content = strings.TrimSpace(content)

	fmt.Print("Digite a categoria da notícia: ")
	category, _ := reader.ReadString('\n')
	category = strings.TrimSpace(category)

	fmt.Print("Digite o ID do perfil relacionado: ")
	profileIDStr, _ := reader.ReadString('\n')
	profileIDStr = strings.TrimSpace(profileIDStr)

	profileID, err := primitive.ObjectIDFromHex(profileIDStr)
	if err != nil {
		log.Fatalf("Formato de ID de perfil inválido: %v", err)
	}

	date := time.Now()

	notice := model.Notice{
		ID:        primitive.NewObjectID(),
		Title:     title,
		Content:   content,
		Category:  category,
		Date:      date,
		ProfileID: profileID,
	}

	err = repository.CreateNotice(notice)
	if err != nil {
		log.Fatalf("Erro ao criar notícia: %v", err)
	}

	fmt.Println("Notícia criada com sucesso!")
	reader.ReadString('\n')
}

func findNoticeByID(reader *bufio.Reader) {
	fmt.Print("Digite o ID da notícia: ")
	idStr, _ := reader.ReadString('\n')
	idStr = strings.TrimSpace(idStr)

	id, err := primitive.ObjectIDFromHex(idStr)
	if err != nil {
		log.Fatalf("Formato de ID inválido: %v", err)
	}

	notice, err := repository.FindNoticeById(id)
	if err != nil {
		log.Fatalf("Erro ao encontrar notícia: %v", err)
	}

	profile, _ := repository.FindProfileById(notice.ProfileID)

	fmt.Printf("\nData:    	%s\n", notice.Date.Format("02-Jan-06  15:04"))
	fmt.Printf("ID:      	%s\n", notice.ID.Hex())
	fmt.Printf("Categoria: 	%s\n", notice.Category)
	fmt.Printf("Título:  	%s\n", notice.Title)
	fmt.Printf("Conteúdo:	%s\n", notice.Content)
	fmt.Printf("			Perfil:	%s\n", notice.ProfileID.Hex())
	fmt.Printf("			Nome:	%s\n", profile.Name)
	fmt.Printf("			Idade:	%d\n", profile.Age)
	fmt.Printf("			Cidade:	%s\n\n", profile.City)

	reader.ReadString('\n')
}

func findAllNotices(reader *bufio.Reader) {
	notices, err := repository.FindAllNotices()
	if err != nil {
		log.Fatalf("Erro ao encontrar todas as notícias: %v", err)
	}

	fmt.Println("Notícias encontradas:")
	for _, notice := range notices {
		profile, _ := repository.FindProfileById(notice.ProfileID)

		fmt.Printf("\nData:    	%s\n", notice.Date.Format("02-Jan-06  15:04"))
		fmt.Printf("ID:      	%s\n", notice.ID.Hex())
		fmt.Printf("Categoria: 	%s\n", notice.Category)
		fmt.Printf("Título:  	%s\n", notice.Title)
		fmt.Printf("Conteúdo:	%s\n", notice.Content)
		fmt.Printf("			Perfil:	%s\n", notice.ProfileID.Hex())
		fmt.Printf("			Nome:	%s\n", profile.Name)
		fmt.Printf("			Idade:	%d\n", profile.Age)
		fmt.Printf("			Cidade:	%s\n\n", profile.City)
	}
	reader.ReadString('\n')
}

func updateNotice(reader *bufio.Reader) {
	fmt.Print("Digite o ID da notícia que deseja atualizar: ")
	idStr, _ := reader.ReadString('\n')
	idStr = strings.TrimSpace(idStr)

	id, err := primitive.ObjectIDFromHex(idStr)
	if err != nil {
		log.Fatalf("Formato de ID inválido: %v", err)
	}

	fmt.Print("Digite o novo título da notícia: ")
	title, _ := reader.ReadString('\n')
	title = strings.TrimSpace(title)

	fmt.Print("Digite o novo conteúdo da notícia: ")
	content, _ := reader.ReadString('\n')
	content = strings.TrimSpace(content)

	fmt.Print("Digite a nova categoria da notícia: ")
	category, _ := reader.ReadString('\n')
	category = strings.TrimSpace(category)

	fmt.Print("Digite o novo ID do perfil relacionado: ")
	profileIDStr, _ := reader.ReadString('\n')
	profileIDStr = strings.TrimSpace(profileIDStr)

	profileID, err := primitive.ObjectIDFromHex(profileIDStr)
	if err != nil {
		log.Fatalf("Formato de ID de perfil inválido: %v", err)
	}

	date := time.Now()

	update := model.Notice{
		Title:     title,
		Content:   content,
		Category:  category,
		Date:      date,
		ProfileID: profileID,
	}

	err = repository.UpdateNotice(id, update)
	if err != nil {
		log.Fatalf("Erro ao atualizar notícia: %v", err)
	}

	fmt.Println("Notícia atualizada com sucesso!")
	reader.ReadString('\n')
}

func deleteNotice(reader *bufio.Reader) {
	fmt.Print("Digite o ID da notícia que deseja deletar: ")
	idStr, _ := reader.ReadString('\n')
	idStr = strings.TrimSpace(idStr)

	id, err := primitive.ObjectIDFromHex(idStr)
	if err != nil {
		log.Fatalf("Formato de ID inválido: %v", err)
	}

	err = repository.DeleteNotice(id)
	if err != nil {
		log.Fatalf("Erro ao deletar notícia: %v", err)
	}

	fmt.Println("Notícia deletada com sucesso!")
	reader.ReadString('\n')
}
