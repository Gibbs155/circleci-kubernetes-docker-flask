from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def main_handler():
    version_info = os.environ.get('VERSION_INFO')
    build_date = os.environ.get('BUILD_DATE')
    return jsonify({'message': f'Hello World! (Version info: {version_info}, build date: {build_date})'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
