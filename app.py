from flask import Flask, request, jsonify
from recommendation import recommend_products
import os

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
    # Get the port from the environment variable, or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app on all network interfaces (0.0.0.0)
    app.run(host="0.0.0.0", port=port, debug=True)
