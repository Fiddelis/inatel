package database

import (
	"context"
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var (
	CollectionNotices  *mongo.Collection
	CollectionProfiles *mongo.Collection
)

func ConnectDB() {
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")

	Client, err := mongo.Connect(context.TODO(), clientOptions)

	if err != nil {
		log.Fatal(err)
	}

	err = Client.Ping(context.TODO(), nil)

	if err != nil {
		log.Fatal(err)
	}

	CollectionNotices = Client.Database("inatel").Collection("news")
	CollectionProfiles = Client.Database("inatel").Collection("profiles")

	fmt.Println("Connected to MongoDB!")
}
