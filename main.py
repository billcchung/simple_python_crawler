import sys
import os

# append the lib folder to PYTHONPATH
lib_path = os.path.join(os.path.dirname(__file__), 'lib')
if not lib_path in sys.path:
    sys.path.append(lib_path)
import handler

config = {
    'dirs': {'output': 'outputs'}
}

def main(entry, depth):
    print("Entry: {w}, depth: {d}".format(w=entry, d=depth))
    hdlr = handler.Handler(config)
    hdlr.crawl(entry ,int(depth))


if __name__ == '__main__':
    print(sys.argv)
    main(*sys.argv[1:])