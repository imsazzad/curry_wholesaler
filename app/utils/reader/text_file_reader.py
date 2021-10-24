import logging

from utils.reader.reader import Reader

logging.basicConfig(level=logging.DEBUG)


class TextFileReader(Reader):
    # overriding abstract method
    def read(self, file_path):
        try:
            file = open(file_path, "r")
        except OSError:
            logging.error('Could not open/read file: - {}'.format(file_path))
            return None

        lines = []
        for line in file:
            lines.append(line.strip())  # remove /n
        file.close()
        logging.debug(lines)
        return lines
