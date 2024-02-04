# Import the dependencies.
from flask import Flask, jsonify, render_template, request
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

@app.route("/recommend_book_ui")
def recommend_by_book_ui():
    return render_template("recommend_by_book.html")

@app.route("/recommend_book", methods=['post'])
def recommend_book():
    user_book=request.form.get("user_book")
    return str(user_book)

@app.route("/recommend_user_ui")
def recommend_user_ui():
    return render_template("recommend_by_user.html")

@app.route("/recommend_user", methods=['post'])
def recommend_user():
    user_id=request.form.get("user_id")
    return str(user_id)

if __name__== "__main__":
    app.run(debug=True)