# Import the dependencies.
from flask import Flask, jsonify, render_template
import pickle

popular_df=pickle.load(open('Books-Recommendation-System\popular.pkl', 'rb'))
#################################################
# Flask Setup
#################################################
app=Flask(__name__)

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def index():
    return render_template("index.html",
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           ratings_count=list(popular_df['count_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

if __name__== "__main__":
    app.run(debug=True)