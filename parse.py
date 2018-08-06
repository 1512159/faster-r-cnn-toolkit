import xmltodict
import glob
import os
from shutil import copyfile
LABEL  = 'dyed-resection-margin'
OUT_DIR = LABEL+'/'
OUT_META = OUT_DIR+'meta/'
OUT_IMAGE = OUT_DIR+'images/'
INP_DIR = 'input_xml_format/'


def read_xml(idx,path):
	print(path)
	with open(path) as fd:
		doc = xmltodict.parse(fd.read())
	annot = doc['annotation']
	copyfile(path.replace('.xml','.jpg'),OUT_IMAGE+str(idx).zfill(5)+'.jpg')
	fo = open(OUT_META+str(idx).zfill(5)+'.txt',"w")
	#folder = annot['folder']
	#filename = annot['filename']
	#path= annot['path']
	#source = annot['source']
	#size = annot['size']
	#width = size['width']
	#height = size['height']
	#depth = size['depth']
	#if not annot.has_key('object'):
	if 'object' not in annot.keys():
		return
	objects = annot['object']
	if type(objects) is not type([]):
		objects = [objects]

	for i in range(len(objects)):
		obj = objects[i]
		#if obj['name'] == 'person':
		#	continue
		# dest_dir = os.path.join(outdir, obj['name'])
		# if not os.path.exists(dest_dir):
			# os.makedirs(dest_dir)

		xmin = int(obj['bndbox']['xmin'])
		ymin = int(obj['bndbox']['ymin'])
		xmax = int(obj['bndbox']['xmax'])
		ymax = int(obj['bndbox']['ymax'])
		fo.write(str(xmin)+' '+str(ymin)+' '+str(xmax)+' '+str(ymax)+' '+LABEL+'\n')
	fo.close()
	# print(path, len(objects))

def main():
	xml_lists = glob.glob(INP_DIR+'*.xml')

	if not os.path.exists(OUT_DIR):
		os.makedirs(OUT_DIR)
	if not os.path.exists(OUT_META):
		os.makedirs(OUT_META)
	if not os.path.exists(OUT_IMAGE):
		os.makedirs(OUT_IMAGE)
	for idx,xml in enumerate(xml_lists):
		read_xml(idx,xml)

if __name__ == '__main__':
	main()