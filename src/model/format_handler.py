import json

from src.model.format import Format
from src.model.format_list import FormatList
from src.util.variables import OUTPUT_DIR


class FormatHandler:

    def __init__(self, format_list):
        self.__format_list = format_list

    def export_format(self, output_dir=OUTPUT_DIR):
        self.__format_list.export_formats(output_dir)

    def common_keys(self):
        return self.__format_list.common_keys()

    def export_common_keys(self, output_dir=OUTPUT_DIR):
        return self.__format_list.export_common_keys(output_dir)

    @staticmethod
    def instance_from_file(input_file):
        f_list = FormatList()
        with open(input_file) as json_file:
            data = json.load(json_file)
            for document in data:
                FormatHandler.__handle_document(f_list, document)
        return FormatHandler(f_list)

    @staticmethod
    def __handle_document(format_list, doc):
        f = format_list.get_format_of_doc(doc)
        if f is None:
            new_f = Format(Format.get_doc_keys(doc))
            new_f.add_doc(doc)
            format_list.add_format(new_f)
        else:
            f.add_doc(doc)


