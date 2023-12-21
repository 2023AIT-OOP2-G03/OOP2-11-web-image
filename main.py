from modules.canny.canny import canny
from modules.face_frame.face_frame import face_frame
from modules.watchdoc import watchdoc
from web import main as web

def main():
    web.app.run(debug=False)
    directory_to_watch = "./img/before"

if __name__ == "__main__":
    main()