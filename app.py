
import os

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL


application = Flask(__name__)

# Database configuration
application.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST", "localhost")
application.config["MYSQL_USER"] = os.getenv("MYSQL_USER", "root")
application.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "root")
application.config["MYSQL_DB"] = os.getenv("MYSQL_DB", "devops")


database = MySQL(application)


def prepare_database():
    """Create the application table if it does not already exist."""

    with application.app_context():
        connection = database.connection.cursor()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS user_messages (
                message_id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT NOT NULL
            )
        """)

        database.connection.commit()
        connection.close()


@application.route("/")
def dashboard():
    """Display the application dashboard and stored messages."""

    cursor = database.connection.cursor()

    cursor.execute("""
        SELECT content
        FROM user_messages
        ORDER BY message_id ASC
    """)

    stored_messages = cursor.fetchall()
    cursor.close()

    return render_template(
        "index.html",
        messages=stored_messages
    )


@application.route("/submit", methods=["POST"])
def save_message():
    """Save a new message to MySQL."""

    content = request.form.get("new_message", "").strip()

    if not content:
        return jsonify({
            "error": "Message cannot be empty."
        }), 400

    cursor = database.connection.cursor()

    cursor.execute(
        "INSERT INTO user_messages (content) VALUES (%s)",
        (content,)
    )

    database.connection.commit()
    cursor.close()

    return jsonify({
        "message": content
    })


@application.route("/health")
def health_check():
    """Endpoint used by Docker to verify that Flask is running."""

    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    prepare_database()

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

