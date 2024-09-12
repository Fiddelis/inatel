package model

import (
	"time"

	"go.mongodb.org/mongo-driver/bson/primitive"
)

type Notice struct {
	ID        primitive.ObjectID `bson:"_id"`
	Title     string
	Content   string
	Category  string
	Date      time.Time
	ProfileID primitive.ObjectID `bson:"profile_id"`
}
