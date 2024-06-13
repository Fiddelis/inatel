package model

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type Profile struct {
	ID   primitive.ObjectID `bson:"_id"`
	Name string
	Age  int32
	City string
}
