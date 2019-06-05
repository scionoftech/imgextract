from imgextract import ImgExtractor
import sys

if __name__ == '__main__':
    ss = ImgExtractor()
    ss.extract(sys.argv[1], sys.argv[2], sys.argv[3])
