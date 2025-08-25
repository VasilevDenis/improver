from lxml import etree as ET


class Improver:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
    
    def change_first_angle(self, angle):
        self._change_text('ANGL', angle)
    
    def change_second_angle(self, angle):
        self._change_text('ANGR', angle)
    
    def show_program_count(self) -> None:
        program_count = len(self.root.findall('.//BAR'))
        print(program_count)


    def _change_text(self, node, text):
        nodes = self.root.findall('.//' + node)
        for elem in nodes:
            elem.text = text
    
    def delete_repeated_nodes_and_change_count(self):
        bars = {}

        # First pass: count and remove duplicates
        for bar in list(self.root.xpath(".//BAR")):
            barcode_node = bar.find(".//BCOD")
            if barcode_node is None or barcode_node.text is None:
                continue
            barcode_text = barcode_node.text.strip()

            if barcode_text in bars:
                bar.getparent().remove(bar)
                bars[barcode_text] += 1
            else:
                bars[barcode_text] = 1

        # Second pass: update MLT
        for bar in self.root.xpath(".//BAR"):
            barcode_node = bar.find(".//BCOD")
            if barcode_node is None or barcode_node.text is None:
                continue
            barcode_text = barcode_node.text.strip()

            counter = bar.find("MLT")
            if counter is not None:
                counter.text = str(bars[barcode_text])

    def save_xml(self):
        self.tree.write('Improved_CNCDATA.XML', pretty_print=True, encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    xml_file = 'CNCDATA.XML'
    improver = Improver(xml_file)
    improver.show_program_count()
    improver.delete_repeated_nodes_and_change_count()
    improver.change_first_angle('90')
    improver.change_second_angle('45')
    improver.show_program_count()
    improver.save_xml()


