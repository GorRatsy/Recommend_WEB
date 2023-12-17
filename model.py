import joblib

class Recommender:

    def __init__(self, user_id):
        self.model = joblib.load("static/knn_model.sav")
        self.data = joblib.load("static/trunc_data_knn.sav")
        self.user_id = user_id


    def return_top_three(self):

        try:
            self.user_id = int(self.user_id)

            # Make predictions for user with each element
            uid_predictions = []

            for item in self.data.itemid.unique():
                prediction = self.model.predict(uid=self.user_id, iid=item)

                if prediction.details['was_impossible'] == False:
                    uid_predictions.append(prediction)


            if len(uid_predictions)==0:
                return "There is no user with inserted ID"

            else:
                uid_predictions.sort(key=lambda x: x.est, reverse=True)
                recommendations = [i.iid for i in uid_predictions[:3]]
                return ' '.join(str(i) for i in recommendations)


        except TypeError:
            return "Ooops! You entered a wrong value. It must be integer"