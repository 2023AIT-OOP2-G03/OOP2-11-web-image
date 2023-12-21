import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#ファイルのパスを表示する関数(デバック用)
#def process_image(image_path):
    #print(f"Processing image: {image_path}")

#ファイルが変更された場合に、そのファイルのパスを返すクラス
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        # ファイルが変更されたらそのファイルを処理する
        if event.event_type == 'modified':
            image_path = event.src_path
            #ここをコメントアウトすると表示されなくなる
            process_image(image_path)
            return image_path

#監視用の関数
def watch_directory(directory_path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    # 監視するディレクトリのパスを指定
    directory_to_watch = "./GitHub/OOP2-11-webimage/img/before"
    #正木の環境のデバッグ用パス
    directory_to_watch = "./img/before"
    watch_directory(directory_to_watch)