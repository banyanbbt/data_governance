# coding=utf-8

import os, sys, logging
import utils.file_util as file_util
from services.text_service import TextService

class FileManage:
    def __init__(self):
        self.settings = dict(sources_path=os.path.join(os.path.dirname(__file__), "./data/sources"),
            results_path=os.path.join(os.path.dirname(__file__), "./data/results"),
            logs_path=os.path.join(os.path.dirname(__file__), "./logs"))

    def process(self):
        logging.info('Start process source files...')

        total_source_files = 0
        source_files = file_util.get_filepaths(self.settings['sources_path'])
        for sf in source_files:
            if sf.endswith(".txt"):
                logging.info('Parsing file: ' + sf)

                with open(sf) as tf:
                    for line in tf:
                        content = line.rstrip('\n')
                        if content != '' and content != None:
                            TextService.process_file(content)

                total_source_files += 1

        logging.info('Total %s source files been processed.' % total_source_files)
        logging.info('End process source files...')


def main():
    manage = FileManage()

    logs_path = manage.settings['logs_path']
    logging.basicConfig(filename=logs_path+'/sms.log', level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s')

    logging.info(manage.settings['sources_path'])
    logging.info(manage.settings['results_path'])
    logging.info(manage.settings['logs_path'])

    manage.process()


if __name__ == "__main__":
    main()