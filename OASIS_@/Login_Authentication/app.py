from website import create_application
if __name__=='__main__':
    app = create_application()
    app.run(debug=True,port=3000)
