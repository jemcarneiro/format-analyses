import collections

from src.util.variables import PREFIX_TXT, COMMON_KEYS_NAME


class FormatList:

    def __init__(self):
        self.f_list = []

    def add_format(self, f):
        self.f_list.append(f)

    def get_format_of_doc(self, doc):
        for f in self.f_list:
            if f.has_same_format(doc):
                return f
        return None

    def export_formats(self, output_dir):
        for f in self.f_list:
            f.export(output_dir)
            output_path = output_dir + f.name + PREFIX_TXT
            with open(output_path, 'w') as handler:
                handler.writelines("%s\n" % key for key in f.key_list)
                print("Successful: Format at " + output_path)

    def contains(self, format_list):
        for f in format_list.f_list:
            count = 0
            # verificar se este formato corresponde a algum da lista contida
            for f1 in self.f_list:
                if collections.Counter(f.key_list) == collections.Counter(f1.key_list):
                    count += 1
            if count == 0:
                return False
        return True

    def common_keys(self):
        common_keys = self.f_list[0].key_list
        for f in self.f_list:
            common_keys = list(set(common_keys).intersection(f.key_list))
        return common_keys

    def export_common_keys(self, output_dir):
        key_list = self.common_keys()
        output_path = output_dir + COMMON_KEYS_NAME + PREFIX_TXT
        with open(output_path, 'w') as handler:
            handler.writelines("%s\n" % key for key in key_list)
            print("Successful: Common keys at " + output_path)
