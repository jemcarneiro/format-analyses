from src.model.format_handler import FormatHandler
from src.util.variables import INPUT_FILE

handler = FormatHandler.instance_from_file(INPUT_FILE)
handler.export_format()
keys = handler.common_keys()
handler.export_common_keys()
