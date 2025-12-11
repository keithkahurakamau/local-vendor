from app import create_app

# The factory will automatically load DevelopmentConfig
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)