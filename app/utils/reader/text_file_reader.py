from utils.reader.reader import Reader
import logging
logging.basicConfig(level=logging.DEBUG)


class TextFileReader(Reader):
    # overriding abstract method
    def read(self, file_path):
        try:
            f = open(file_path, "r")
        except OSError:
            logging.error('Could not open/read file: - {}'.format(file_path))
            return None

        lines = []
        for line in f:
            lines.append(line.strip())  # remove /n
        f.close()
        logging.debug(lines)
        return lines
