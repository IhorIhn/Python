import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def find_incoming_by_group_number(xml_file_path, target_number):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.findtext('number')
        if number == str(target_number):
            incoming = group.findtext('timingExbytes/incoming')
            if incoming:
                logging.info(f"Group number {target_number} incoming: {incoming}")
                return incoming
            logging.info(f"Group number {target_number} не має incoming")
            return None

    logging.info(f"Group number {target_number} не знайдено")
    return None

# Приклад виклику
find_incoming_by_group_number('groups.xml', 4)