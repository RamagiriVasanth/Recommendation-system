from flask import Flask, request, jsonify
from recommendation import recommend_products
import os

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    recommendations = recommend_products(user_id)
    return jsonify({'user_id': user_id, 'recommended_products': recommendations})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render will assign port 10000
    app.run(debug=True, host='0.0.0.0', port=port)
