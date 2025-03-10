# app.py
from flask import Flask, request, jsonify
from recommendation import recommend_products

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    recommendations = recommend_products(user_id)
    return jsonify({'user_id': user_id, 'recommended_products': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
