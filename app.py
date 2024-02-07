# Import the dependencies.
import pandas as pd
from flask import Flask, jsonify, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
import pickle

popular_df=pickle.load(open('Books-Recommendation-System\popular.pkl', 'rb'))
rating_input_df=pickle.load(open('Books-Recommendation-System/rating_input.pkl', 'rb'))
books_df=pickle.load(open('Books-Recommendation-System/books_df.pkl', 'rb'))
search_df=pickle.load(open('Books-Recommendation-System/search.pkl', 'rb'))
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
    df_books_ratigs_user=rating_input_df.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
    # filling n/a with 0 so far, assuming it means that no interest for a book by a user,
    df_books_ratigs_user=df_books_ratigs_user.fillna(0)
    # create a dictionary for mapping between row number ans Book-Title
    index_title_dict=dict(df_books_ratigs_user.reset_index()['Book-Title'])
    # apply cosine_similarity
    books_similarity = cosine_similarity(df_books_ratigs_user)
    # convert output of cosine_similarity into df
    books_similarity_df=pd.DataFrame(books_similarity)
    # introduce title here
    books_similarity_df=books_similarity_df.rename(columns=index_title_dict)
    books_similarity_df.index=books_similarity_df.index.map(index_title_dict)
    # find a similarity list for the book
    recommendations=pd.DataFrame(books_similarity_df.loc[user_book,:])
    # remove the actual book
    book_title_list=[user_book]
    recommendations=recommendations[~recommendations.index.isin(book_title_list)].sort_values(by=user_book, ascending=False)
    # select top top_X_recommendations
    top_recommendations=recommendations[:5].rename(columns={user_book:'similarity rate'})
    top_recommendations=top_recommendations.rename_axis('Book-Title', axis='index')
    recommendations_full_info=pd.merge(top_recommendations, books_df, left_on='Book-Title',right_on='Book-Title', how='left')
    dict_years=dict(recommendations_full_info.groupby('Book-Title')['Year-Of-Publication'].max())
    for i, row in recommendations_full_info.iterrows():
        if row['Year-Of-Publication']!=dict_years[row['Book-Title']]:
            recommendations_full_info.loc[i,'Year-Of-Publication']=0
    recommendations_full_info=recommendations_full_info[recommendations_full_info['Year-Of-Publication'] != 0]
    recommendations_full_info=recommendations_full_info.drop_duplicates(subset=['Book-Title'])
    data = recommendations_full_info.to_dict('recommendations')
    return render_template("recommend_by_book.html",data = data)

@app.route("/recommend_user_ui")
def recommend_user_ui():
    return render_template("recommend_by_user.html")

@app.route("/recommend_user", methods=['post'])
def recommend_user():
    user_id=request.form.get("user_id")
    return str(user_id)

@app.route('/search', methods=['GET'])
def view_books():
    search_query = request.args.get('search', '')      
    if search_query:
        filtered_books_df = search_df[search_df['Book-Title'].str.contains(search_query, case=False, na=False)]
        books = filtered_books_df.to_dict('records')
    else:
        books = search_df.to_dict('records')

    return render_template('search.html', books=books)



if __name__== "__main__":
    app.run(debug=True)