import os
from flask import Flask, request, jsonify
from recommendation import recommend_products

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the E-Commerce Product Recommendation System! Visit /recommendations?user_id=<user_id> to get product recommendations."

# Recommendations route
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    recommendations = recommend_products(user_id)
    return jsonify({'user_id': user_id, 'recommended_products': recommendations})

if __name__ == '__main__':
    # Use environment variable to get the correct port for Render or cloud provider
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if not set
    app.run(debug=True, host='0.0.0.0', port=port)
