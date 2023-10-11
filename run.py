import platform
import sys

import eel


@eel.expose
def test():
    print("hello eel")


def start_eel(develop):
    if develop:
        directory = "src"
        page = {"port": 3000}
    else:
        directory = "build"
        page = "index.html"

    eel.init(directory, [".tsx", ".ts", ".jsx", ".js", ".html"])

    eel_kwargs = dict(
        host="localhost",
        port=8080,
        size=(1280, 800),
    )

    try:
        eel.start(page, app=None, **eel_kwargs)
    except EnvironmentError:
        # chromeが見つからないときはwin10以降のedgeを呼び出す
        if sys.platform in ["win32", "win64"] and int(platform.release()) >= 10:
            eel.start(page, mode="edge", **eel_kwargs)
        else:
            raise


if __name__ == '__main__':
    import sys

    start_eel(develop=len(sys.argv) == 2)
