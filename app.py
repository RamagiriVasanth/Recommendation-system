from flask import Flask, request, jsonify
from recommendation import recommend_products

app = Flask(__name__)

# Root route (optional, for testing purposes)
@app.route('/')
def home():
    return "Welcome to the E-Commerce Recommendation System!"

# Recommendation route
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Get user_id from query parameters
    user_id = int(request.args.get('user_id'))
    
    # Get recommended products for the user
    recommendations = recommend_products(user_id)
    
    # Return recommendations as a JSON response
    return jsonify({'user_id': user_id, 'recommended_products': recommendations})

# Run the Flask app with host set to '0.0.0.0' for Render compatibility
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
