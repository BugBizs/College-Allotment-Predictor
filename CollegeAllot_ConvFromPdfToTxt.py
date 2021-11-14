from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator



password = ""
extracted_text = ""
fp = open("ct.pdf", "rb")  #input file
parser = PDFParser(fp)
document = PDFDocument(parser, password)
if not document.is_extractable:
	raise PDFTextExtractionNotAllowed
	
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.create_pages(document):
	interpreter.process_page(page)
	layout = device.get_result()
	for lt_obj in layout:
		if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
			extracted_text += lt_obj.get_text()			
fp.close()


with open("pdftext.txt", "wb") as my_log:  #output file
	my_log.write(extracted_text.encode("utf-8"))
print("Done !!")
