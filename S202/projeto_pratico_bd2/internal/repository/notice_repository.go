// notice_repository.go

package repository

import (
	"context"

	db "github.com/fiddelis/projeto_pratico_bd2/database"
	"github.com/fiddelis/projeto_pratico_bd2/internal/model"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
)

func CreateNotice(notice model.Notice) error {
	_, err := db.CollectionNotices.InsertOne(context.TODO(), notice)
	return err
}

func FindNoticeById(id primitive.ObjectID) (model.Notice, error) {
	var notice model.Notice
	err := db.CollectionNotices.FindOne(context.TODO(), bson.M{"_id": id}).Decode(&notice)
	return notice, err
}

func FindAllNotices() ([]model.Notice, error) {
	var notices []model.Notice
	cursor, err := db.CollectionNotices.Find(context.TODO(), bson.M{})
	if err != nil {
		return nil, err
	}
	defer cursor.Close(context.TODO())
	for cursor.Next(context.TODO()) {
		var notice model.Notice
		if err = cursor.Decode(&notice); err != nil {
			return nil, err
		}
		notices = append(notices, notice)
	}
	if err := cursor.Err(); err != nil {
		return nil, err
	}
	return notices, nil
}

func UpdateNotice(id primitive.ObjectID, notice model.Notice) error {
	filter := bson.D{{Key: "_id", Value: id}}
	update := bson.D{
		{Key: "$set", Value: bson.D{
			{Key: "title", Value: notice.Title},
			{Key: "content", Value: notice.Content},
			{Key: "category", Value: notice.Category},
			{Key: "date", Value: notice.Date},
			{Key: "profile_id", Value: notice.ProfileID},
		}},
	}

	_, err := db.CollectionNotices.UpdateOne(context.TODO(), filter, update)
	return err
}

func DeleteNotice(id primitive.ObjectID) error {
	_, err := db.CollectionNotices.DeleteOne(context.TODO(), bson.M{"_id": id})
	return err
}
