package repository

import (
	"context"

	db "github.com/fiddelis/projeto_pratico_bd2/database"
	"github.com/fiddelis/projeto_pratico_bd2/internal/model"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

func CreateProfile(profile model.Profile) error {
	_, err := db.CollectionProfiles.InsertOne(context.TODO(), profile)
	return err
}

func FindProfileById(id primitive.ObjectID) (model.Profile, error) {
	var profile model.Profile
	err := db.CollectionProfiles.FindOne(context.TODO(), bson.M{"_id": id}).Decode(&profile)
	return profile, err
}

func FindAllProfiles() ([]model.Profile, error) {
	var profiles []model.Profile
	cursor, err := db.CollectionProfiles.Find(context.TODO(), bson.M{})
	if err != nil {
		return nil, err
	}
	defer cursor.Close(context.TODO())
	for cursor.Next(context.TODO()) {
		var profile model.Profile
		if err = cursor.Decode(&profile); err != nil {
			return nil, err
		}
		profiles = append(profiles, profile)
	}
	if err := cursor.Err(); err != nil {
		return nil, err
	}
	return profiles, nil
}

func UpdateProfile(id primitive.ObjectID, profile model.Profile) error {
	filter := bson.D{{Key: "_id", Value: id}}
	update := bson.D{
		{Key: "$set", Value: bson.D{
			{Key: "name", Value: profile.Name},
			{Key: "age", Value: profile.Age},
			{Key: "city", Value: profile.City},
		}},
	}

	_, err := db.CollectionProfiles.UpdateOne(context.TODO(), filter, update)
	return err
}

func DeleteProfile(id primitive.ObjectID) error {
	_, err := db.CollectionProfiles.DeleteOne(context.TODO(), bson.M{"_id": id})
	return err
}
