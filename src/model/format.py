import collections
import json

from src.util.variables import PREFIX_JSON, FORMAT_BASE_NAME


class Format:

    COUNTER = 0

    def __init__(self, key_list):
        self.name = self.build_name()
        self.key_list = key_list
        self.doc_list = []
        Format.COUNTER += 1

    def has_same_format(self, doc):
        a = collections.Counter(Format.get_doc_keys(doc)) == collections.Counter(self.key_list)
        return a

    @staticmethod
    def checkList(ele, prefix, nameList):
        for i in range(len(ele)):
            if (isinstance(ele[i], list)):
                nameList = Format.checkList(ele[i], prefix + "[" + str(i) + "]", nameList)
            elif (isinstance(ele[i], str)):
                nameList.append(prefix + "[" + str(i) + "]")
            else:
                nameList = Format.checkDict(ele[i], prefix + "[" + str(i) + "]", nameList)
        return nameList

    @staticmethod
    def checkDict(jsonObject, prefix, nameList):
        for ele in jsonObject:
            if (isinstance(jsonObject[ele], dict)):
                nameList = Format.checkDict(jsonObject[ele], prefix + "." + ele, nameList)

            elif (isinstance(jsonObject[ele], list)):
                nameList= Format.checkList(jsonObject[ele], prefix + "." + ele, nameList)

            elif (isinstance(jsonObject[ele], str)):
                nameList.append(prefix + "." + ele)
        return nameList

    @staticmethod
    def get_doc_keys(doc):
    # Iterating all the fields of the JSON
        nameList = list()
        for element in doc:
            # If Json Field value is a Nested Json
            if (isinstance(doc[element], dict)):
                nameList=Format.checkDict(doc[element], element, nameList)
            # If Json Field value is a list
            elif (isinstance(doc[element], list)):
                nameList=Format.checkList(doc[element], element, nameList)
            # If Json Field value is a string
            elif (isinstance(doc[element], str)):
                nameList.append(element)
        return nameList

    def add_doc(self, doc):
        self.doc_list.append(doc)

    def export(self, output_dir):
        output_path = output_dir + self.name + PREFIX_JSON
        with open(output_path, 'w') as outfile:
            json.dump(self.doc_list, outfile)
            print("Successful: Alerts at " + output_path)

    def build_name(self):
        return FORMAT_BASE_NAME + str(self.COUNTER)
